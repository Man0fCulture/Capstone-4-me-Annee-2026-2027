import bpy, bmesh, math
from mathutils import Vector, Matrix
MATS=['MI_Grimoire_Leather','MI_Grimoire_Metal','MI_Grimoire_Page','MI_Grimoire_PageEdge','MI_Grimoire_EmblemGlow','MI_Grimoire_Ribbon']
for m in MATS:
    if m not in bpy.data.materials: bpy.data.materials.new(m)
def colmat(name,rgb,metal=0,rough=0.5,emit=0):
    m=bpy.data.materials[name]; m.use_nodes=True
    b=m.node_tree.nodes.get('Principled BSDF')
    b.inputs['Base Color'].default_value=(*rgb,1); b.inputs['Metallic'].default_value=metal; b.inputs['Roughness'].default_value=rough
    if emit: b.inputs['Emission Color'].default_value=(*rgb,1); b.inputs['Emission Strength'].default_value=emit
colmat('MI_Grimoire_Leather',(0.16,0.025,0.03),0,0.55)
colmat('MI_Grimoire_Metal',(0.85,0.62,0.3),1,0.3)
colmat('MI_Grimoire_Page',(0.8,0.72,0.56),0,0.8)
colmat('MI_Grimoire_PageEdge',(0.9,0.68,0.3),0.8,0.35)
colmat('MI_Grimoire_EmblemGlow',(0.9,0.05,0.08),0,0.2,3)
colmat('MI_Grimoire_Ribbon',(0.45,0.02,0.04),0,0.45)
L,MET,PAGE,EDGE,GLOW,RIB=range(6)
PARTS=[]
def new_obj(name,bm,mat):
    me=bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    o=bpy.data.objects.new(name,me); bpy.context.collection.objects.link(o)
    for m in MATS: o.data.materials.append(bpy.data.materials[m])
    for p in o.data.polygons: p.material_index=mat
    return o
def box(name,x0,x1,y0,y1,z0,z1,mat,bevel=0.0,seg=2):
    bm=bmesh.new(); bmesh.ops.create_cube(bm,size=1.0)
    for v in bm.verts:
        v.co.x=x0+(v.co.x+0.5)*(x1-x0); v.co.y=y0+(v.co.y+0.5)*(y1-y0); v.co.z=z0+(v.co.z+0.5)*(z1-z0)
    o=new_obj(name,bm,mat)
    if bevel>0:
        md=o.modifiers.new('b','BEVEL'); md.width=bevel; md.segments=seg; md.limit_method='ANGLE'
    return o
def prism(name,poly2d,z0,z1,mat,bevel=0.0,seg=2,flip=False):
    bm=bmesh.new()
    vs=[bm.verts.new((x,y,z0)) for x,y in poly2d]
    f=bm.faces.new(vs)
    bmesh.ops.recalc_face_normals(bm,faces=[f])
    if f.normal.z>0: f.normal_flip()
    r=bmesh.ops.extrude_face_region(bm,geom=[f])
    nv=[e for e in r['geom'] if isinstance(e,bmesh.types.BMVert)]
    for v in nv: v.co.z=z1
    bmesh.ops.recalc_face_normals(bm,faces=bm.faces[:])
    o=new_obj(name,bm,mat)
    if bevel>0:
        md=o.modifiers.new('b','BEVEL'); md.width=bevel; md.segments=seg; md.limit_method='ANGLE'
    return o
def sphere(name,c,r,mat,scale=(1,1,1)):
    bm=bmesh.new(); bmesh.ops.create_uvsphere(bm,u_segments=16,v_segments=10,radius=r)
    for v in bm.verts: v.co=Vector((v.co.x*scale[0]+c[0],v.co.y*scale[1]+c[1],v.co.z*scale[2]+c[2]))
    return new_obj(name,bm,mat)
def ring(name,c,r_in,r_out,z0,z1,mat,n=64,bevel=0.0):
    bm=bmesh.new()
    outer=[bm.verts.new((c[0]+r_out*math.cos(2*math.pi*i/n),c[1]+r_out*math.sin(2*math.pi*i/n),z0)) for i in range(n)]
    inner=[bm.verts.new((c[0]+r_in*math.cos(2*math.pi*i/n),c[1]+r_in*math.sin(2*math.pi*i/n),z0)) for i in range(n)]
    for i in range(n):
        j=(i+1)%n; bm.faces.new([outer[i],outer[j],inner[j],inner[i]])
    r=bmesh.ops.extrude_face_region(bm,geom=bm.faces[:])
    for v in [e for e in r['geom'] if isinstance(e,bmesh.types.BMVert)]: v.co.z=z1
    bmesh.ops.recalc_face_normals(bm,faces=bm.faces[:])
    o=new_obj(name,bm,mat)
    if bevel>0:
        md=o.modifiers.new('b','BEVEL'); md.width=bevel; md.segments=2; md.limit_method='ANGLE'
    return o
def rrect(x0,x1,y0,y1,r,n=6):
    pts=[]
    for cx,cy,a0 in ((x1-r,y1-r,0),(x0+r,y1-r,90),(x0+r,y0+r,180),(x1-r,y0+r,270)):
        for i in range(n+1):
            a=math.radians(a0+90*i/n); pts.append((cx+r*math.cos(a),cy+r*math.sin(a)))
    return pts
def frame_strip(name,x0,x1,y0,y1,w,z0,z1,mat,r=0.004):
    # rectangular outline strip made of 4 boxes + corner discs
    objs=[box(name+'a',x0,x1,y0,y0+w,z0,z1,mat),box(name+'b',x0,x1,y1-w,y1,z0,z1,mat),
          box(name+'c',x0,x0+w,y0,y1,z0,z1,mat),box(name+'d',x1-w,x1,y0,y1,z0,z1,mat)]
    for cx,cy in ((x0,y0),(x0,y1),(x1,y0),(x1,y1)):
        objs.append(ring(name+'r',(cx,cy),r-w*0.5,r+w*0.5,z0,z1,mat,24))
    return objs
def star(cx,cy,r1,r2,n=8,rot=0):
    return [(cx+(r1 if i%2==0 else r2)*math.cos(rot+math.pi*i/n), cy+(r1 if i%2==0 else r2)*math.sin(rot+math.pi*i/n)) for i in range(2*n)]
def corner_piece(name,cx,cy,sx,sy,zface,dz,mat=MET):
    # sx,sy: +/-1 direction pointing inward from the corner; dz: +1 ornaments upward, -1 downward
    leg=0.038
    pts=[(0,0),(leg,0),(leg*0.55,leg*0.18),(leg*0.42,leg*0.42),(leg*0.18,leg*0.55),(0,leg)]
    poly=[(cx+sx*x,cy+sy*y) for x,y in pts]
    z0=zface; z1=zface+dz*0.0016
    objs=[prism(name,poly,min(z0,z1),max(z0,z1),mat,0.0006)]
    for px,py in ((0.009,0.009),(0.026,0.006),(0.006,0.026)):
        objs.append(sphere(name+'rv',(cx+sx*px,cy+sy*py,z1),0.0017,mat,(1,1,0.6)))
    objs.append(sphere(name+'gem',(cx+sx*0.0135,cy+sy*0.0135,z1),0.0034,GLOW,(1,1,0.55)))
    return objs
def ornaments(prefix,zface,dz,x0,x1,y0,y1,center_medallion=True):
    objs=[]
    zz=lambda a,b:(min(zface+dz*a,zface+dz*b),max(zface+dz*a,zface+dz*b))
    # embossed leather panel
    a,b=zz(0,0.0009); objs.append(prism(prefix+'panel',rrect(x0+0.024,x1-0.024,y0+0.024,y1-0.024,0.008),a,b,L,0.0007))
    # gold fillets
    a,b=zz(0,0.0007); objs+=frame_strip(prefix+'f1',x0+0.011,x1-0.011,y0+0.011,y1-0.011,0.0018,a,b,MET,0.005)
    a,b=zz(0.0009,0.0015); objs+=frame_strip(prefix+'f2',x0+0.03,x1-0.03,y0+0.03,y1-0.03,0.0011,a,b,MET,0.004)
    # corners
    for cx,sx in ((x0,1),(x1,-1)):
        for cy,sy in ((y0,1),(y1,-1)):
            objs+=corner_piece(prefix+'c',cx,cy,sx,sy,zface,dz)
    # fore-edge clasp plate (y1 side)
    a,b=zz(0,0.0018); objs.append(prism(prefix+'clasp',[(-0.018,y1),(0.018,y1),(0.012,y1-0.022),(0,y1-0.03),(-0.012,y1-0.022)],a,b,MET,0.0006))
    a,b=zz(0.0018,0.0032); objs.append(sphere(prefix+'claspgem',(0,y1-0.014,(a+b)/2),0.0035,GLOW,(1,1,0.5)))
    if center_medallion:
        cx,cy=0,(y0+y1)/2
        a,b=zz(0.0009,0.0028); objs.append(ring(prefix+'med',(cx,cy),0.03,0.035,a,b,MET,96,0.0004))
        a,b=zz(0.0009,0.0022); objs.append(ring(prefix+'med2',(cx,cy),0.022,0.0238,a,b,MET,96))
        a,b=zz(0.0009,0.0024); objs.append(prism(prefix+'star',star(cx,cy,0.021,0.008,8),a,b,MET,0.0004))
        a,b=zz(0.0024,0.0034); objs.append(prism(prefix+'star2',star(cx,cy,0.012,0.005,4,math.pi/4),a,b,MET,0.0003))
        a,b=zz(0.0034,0.0045); objs.append(sphere(prefix+'ruby',(cx,cy,(a+b)/2),0.0055,GLOW,(1,1,0.55)))
        for i in range(8):
            ang=2*math.pi*i/8+math.pi/8
            a,b=zz(0.0028,0.0036); objs.append(sphere(prefix+'stud',(cx+0.0325*math.cos(ang),cy+0.0325*math.sin(ang),(a+b)/2),0.0016,MET,(1,1,0.7)))
    return objs
def join(name,objs,origin_z=0.0):
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs:
        o.select_set(True); bpy.context.view_layer.objects.active=o
        for m in list(o.modifiers):
            bpy.ops.object.modifier_apply(modifier=m.name)
    bpy.context.view_layer.objects.active=objs[0]
    bpy.ops.object.join()
    o=bpy.context.active_object; o.name=name; o.data.name=name
    # origin
    bpy.context.scene.cursor.location=(0,0,origin_z)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles(threshold=0.00001)
    bpy.ops.uv.smart_project(angle_limit=math.radians(66),island_margin=0.003,scale_to_bounds=False)
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.shade_auto_smooth(angle=math.radians(40)) if hasattr(bpy.ops.object,'shade_auto_smooth') else None
    return o
def bump(y):
    t=(y-0.004)/0.18
    return math.sin(math.pi*min(1,t/0.18)*0.5)**2*(1-0.65*max(0,(t-0.18)/0.82))
def page_block(name,z_flat,sign,mat_top=PAGE):
    # grid block: x[-0.124,0.124], y[0.004,0.184]; flat face at z_flat, curved face at z_flat + sign*(0.018+0.0025*bump)
    nx,ny=24,36
    bm=bmesh.new()
    xs=[-0.124+0.248*i/nx for i in range(nx+1)]; ys=[0.004+0.18*j/ny for j in range(ny+1)]
    top=[[bm.verts.new((x,y,z_flat+sign*(0.018+0.0025*bump(y)))) for y in ys] for x in xs]
    bot=[[bm.verts.new((x,y,z_flat)) for y in ys] for x in xs]
    F=[]
    for i in range(nx):
        for j in range(ny):
            F.append((bm.faces.new([top[i][j],top[i+1][j],top[i+1][j+1],top[i][j+1]]),'top'))
            F.append((bm.faces.new([bot[i][j],bot[i][j+1],bot[i+1][j+1],bot[i+1][j]]),'bot'))
    for i in range(nx):
        F.append((bm.faces.new([bot[i][0],bot[i+1][0],top[i+1][0],top[i][0]]),'spine'))
        F.append((bm.faces.new([bot[i][ny],top[i][ny],top[i+1][ny],bot[i+1][ny]]),'edge'))
    for j in range(ny):
        F.append((bm.faces.new([bot[0][j],top[0][j],top[0][j+1],bot[0][j+1]]),'edge'))
        F.append((bm.faces.new([bot[nx][j],bot[nx][j+1],top[nx][j+1],top[nx][j]]),'edge'))
    bmesh.ops.recalc_face_normals(bm,faces=bm.faces[:])
    mats={'top':mat_top,'bot':PAGE,'spine':PAGE,'edge':EDGE}
    lay=[(f,mats[k]) for f,k in F]
    me=bpy.data.meshes.new(name); bm.to_mesh(me)
    o=bpy.data.objects.new(name,me); bpy.context.collection.objects.link(o)
    for m in MATS: o.data.materials.append(bpy.data.materials[m])
    for idx,(f,k) in enumerate(F): o.data.polygons[idx].material_index=mats[k]
    bm.free()
    return o
# ---------------- delete old
for n in ['SM_Grimoire_BackCover','SM_Grimoire_PagesRight','SM_Grimoire_PagesLeft','SM_Grimoire_TurnPage','SM_Grimoire_FrontCover']:
    if n in bpy.data.objects: bpy.data.objects.remove(bpy.data.objects[n],do_unlink=True)
X0,X1=-0.13,0.13; Y0,Y1=0.006,0.19
# ---------------- BACK COVER (outer face = bottom z=-0.0025)
objs=[prism('bc_board',rrect(X0,X1,Y0,Y1,0.006,4),-0.0025,0.007,L,0.0016,3)]
# spine arc under the gutter (open configuration)
n=24; bm=bmesh.new(); ring_v=[]
for i in range(n+1):
    t=i/n; ang=math.pi*t
    yo=0.010*math.cos(ang); zo=-0.0025-0.011*math.sin(ang)
    yi=0.007*math.cos(ang); zi=0.0035-0.010*math.sin(ang)
    ring_v.append(((yo,zo),(yi,zi)))
grid=[]
for (yo,zo),(yi,zi) in ring_v:
    grid.append((bm.verts.new((X0+0.001,yo,zo)),bm.verts.new((X1-0.001,yo,zo)),bm.verts.new((X0+0.001,yi,zi)),bm.verts.new((X1-0.001,yi,zi))))
for i in range(n):
    a,b=grid[i],grid[i+1]
    bm.faces.new([a[0],a[1],b[1],b[0]]); bm.faces.new([a[2],b[2],b[3],a[3]])
    bm.faces.new([a[0],b[0],b[2],a[2]]); bm.faces.new([a[1],a[3],b[3],b[1]])
bm.faces.new([grid[0][0],grid[0][2],grid[0][3],grid[0][1]]); bm.faces.new([grid[n][0],grid[n][1],grid[n][3],grid[n][2]])
bmesh.ops.recalc_face_normals(bm,faces=bm.faces[:])
objs.append(new_obj('bc_spine',bm,L))
# spine raised bands
for k,x in enumerate([-0.09,-0.045,0.0,0.045,0.09]):
    bm=bmesh.new(); m=20; vv=[]
    for i in range(m+1):
        ang=math.pi*i/m; r=0.0118; vv.append((0.010*math.cos(ang)*1.08, -0.0025-r*math.sin(ang)))
    prof=[]
    for (y,z) in vv:
        prof.append((bm.verts.new((x-0.0035,y,z)),bm.verts.new((x+0.0035,y,z))))
    for i in range(m):
        bm.faces.new([prof[i][0],prof[i][1],prof[i+1][1],prof[i+1][0]])
    o=new_obj('band',bm,L); sd=o.modifiers.new('s','SOLIDIFY'); sd.thickness=0.0018; objs.append(o)
    bm=bmesh.new(); prof=[]
    for (y,z) in vv:
        prof.append((bm.verts.new((x+0.0055,y*1.02,z-0.0002)),bm.verts.new((x+0.0068,y*1.02,z-0.0002))))
    for i in range(m): bm.faces.new([prof[i][0],prof[i][1],prof[i+1][1],prof[i+1][0]])
    o=new_obj('gline',bm,MET); sd=o.modifiers.new('s','SOLIDIFY'); sd.thickness=0.0008; objs.append(o)
objs+=ornaments('bk',-0.0025,-1,X0,X1,Y0,Y1,True)
bc=join('SM_Grimoire_BackCover',objs,0.0)
# ---------------- PAGES RIGHT
pr=page_block('SM_Grimoire_PagesRight',0.007,1)
# ribbons (attached to right pages): lie on page from gutter, over tail edge (+X), hang down
rib=[]
for k,(yy,mat,ln) in enumerate(((0.03,RIB,0.085),(0.045,MET,0.07))):
    bm=bmesh.new(); pts=[]
    N=30
    for i in range(N+1):
        s=i/N
        if s<0.35:
            x=0.07+(0.124-0.07)*(s/0.35); z=0.025+0.0025*bump(yy)+0.0003
        else:
            u=(s-0.35)/0.65
            x=0.124+0.012*math.sin(u*1.4)+0.004*math.sin(u*6+k); z=0.025-u*ln
        pts.append((x,z))
    w=0.0035
    rows=[(bm.verts.new((x,yy-w,z)),bm.verts.new((x,yy+w,z))) for x,z in pts]
    for i in range(N): bm.faces.new([rows[i][0],rows[i][1],rows[i+1][1],rows[i+1][0]])
    tip=bm.verts.new((pts[-1][0],yy,pts[-1][1]+0.006))
    o=new_obj('rib',bm,mat); sd=o.modifiers.new('s','SOLIDIFY'); sd.thickness=0.0005; rib.append(o)
bpy.ops.object.select_all(action='DESELECT')
pr=join('SM_Grimoire_PagesRight',[pr]+rib,0.0)
# ---------------- PAGES LEFT (closed config above hinge; visible face is the bottom one)
pl=page_block('SM_Grimoire_PagesLeft',0.043,-1)
pl=join('SM_Grimoire_PagesLeft',[pl],0.025)
# ---------------- TURN PAGE
bm=bmesh.new(); nx,ny=16,30
xs=[-0.122+0.244*i/nx for i in range(nx+1)]; ys=[0.005+0.178*j/ny for j in range(ny+1)]
g=[[bm.verts.new((x,y,0.0254+0.0025*bump(y))) for y in ys] for x in xs]
for i in range(nx):
    for j in range(ny): bm.faces.new([g[i][j],g[i+1][j],g[i+1][j+1],g[i][j+1]])
tp=new_obj('tp',bm,PAGE); sd=tp.modifiers.new('s','SOLIDIFY'); sd.thickness=0.0004
tp=join('SM_Grimoire_TurnPage',[tp],0.025)
# ---------------- FRONT COVER (closed config; outer face = top z=0.0537)
objs=[prism('fc_board',rrect(X0,X1,Y0,Y1,0.006,4),0.043,0.0537,L,0.0016,3)]
objs+=ornaments('fr',0.0537,1,X0,X1,Y0,Y1,False)
fc=join('SM_Grimoire_FrontCover',objs,0.025)
for o in bpy.data.objects:
    bb=[o.matrix_world @ Vector(c) for c in o.bound_box]
    print(o.name, len(o.data.polygons), [round(min(v[i] for v in bb),4) for i in range(3)], [round(max(v[i] for v in bb),4) for i in range(3)], tuple(round(x,4) for x in o.location))
