// Fond animé des menus STEEZY.
// Tout est calculé ici, sans texture. UV va de 0 à 1, Time en secondes.
// Les couleurs sont pensées comme on les voit à l'écran, Gamma les remet en linéaire à la fin.
struct SteezyBackground
{
    float Hash(float2 p)
    {
        p = frac(p * float2(123.34, 456.21));
        p += dot(p, p + 45.32);
        return frac(p.x * p.y);
    }

    float2 Hash2(float2 p)
    {
        float n = Hash(p);
        return float2(n, Hash(p + n + 17.17));
    }

    // bruit lissé de base
    float Noise(float2 p)
    {
        float2 i = floor(p);
        float2 f = frac(p);
        float2 u = f * f * (3.0 - 2.0 * f);
        float a = Hash(i);
        float b = Hash(i + float2(1.0, 0.0));
        float c = Hash(i + float2(0.0, 1.0));
        float d = Hash(i + float2(1.0, 1.0));
        return lerp(lerp(a, b, u.x), lerp(c, d, u.x), u.y);
    }

    // plusieurs couches de bruit pour la fumée
    float Fbm(float2 p)
    {
        float v = 0.0;
        float a = 0.5;
        for (int k = 0; k < 5; k++)
        {
            v += a * Noise(p);
            p = float2(1.6 * p.x + 1.2 * p.y, -1.2 * p.x + 1.6 * p.y);
            a *= 0.5;
        }
        return v;
    }

    // une couche de braises qui montent, une braise au plus par case
    float Embers(float2 p, float t, float scale, float speed, float seed)
    {
        float2 q = p * scale;
        q.y += t * speed;
        q.x += sin(q.y * 0.35 + seed) * 0.6;
        float2 cell = floor(q);
        float2 f = frac(q) - 0.5;
        float2 rnd = Hash2(cell + seed);
        float alive = step(rnd.x, 0.28);
        float2 pos = (rnd - 0.5) * 0.7;
        // étirée à la verticale comme une étincelle en mouvement
        float d = length((f - pos) * float2(1.0, 0.42));
        float size = 0.018 + 0.03 * rnd.y;
        float flicker = 0.55 + 0.45 * sin(t * (2.0 + rnd.y * 4.0) + rnd.x * 40.0);
        float core = smoothstep(size, 0.0, d);
        float glow = smoothstep(size * 3.5, 0.0, d) * 0.12;
        return (core + glow) * flicker * alive;
    }
};

SteezyBackground B;
float2 p = float2(UV.x * Aspect, UV.y);
float t = Time * Speed;

// fond, plus chaud derrière le titre
float2 centre = float2(0.5 * Aspect, 0.30);
float r = length((p - centre) * float2(0.8, 1.0));
float3 col = lerp(float3(0.13, 0.016, 0.028), float3(0.022, 0.008, 0.012), saturate(r * 1.2));

// fumée déformée qui dérive lentement
float2 sp = p * 1.6 + float2(t * 0.012, t * 0.02);
float2 w = float2(B.Fbm(sp + float2(0.0, t * 0.03)), B.Fbm(sp + float2(5.2, 1.3) - t * 0.025));
float smoke = smoothstep(0.35, 0.95, B.Fbm(sp + 2.2 * w));
float smokeMask = 0.35 + 0.65 * smoothstep(0.15, 1.0, UV.y);
col += float3(0.30, 0.035, 0.055) * smoke * smokeMask * 0.6;

// nappe de brume au ras du sol qui glisse vers la droite
float fog = B.Fbm(p * float2(1.1, 3.4) + float2(t * 0.045, w.y * 0.6));
col += float3(0.24, 0.03, 0.045) * smoothstep(0.35, 0.9, fog) * smoothstep(0.55, 1.0, UV.y) * 0.55;

// deuxième fumée plus sombre pour donner de la profondeur
float smoke2 = B.Fbm(p * 3.2 - float2(t * 0.03, t * 0.015) + w);
col *= lerp(0.7, 1.08, smoke2);

// rayons de lumière qui tombent d'au-dessus du titre
float2 dv = p - float2(0.5 * Aspect, -0.35);
float ang = atan2(dv.x, dv.y);
// des sinus plutôt que du bruit, pour des faisceaux doux sans arêtes
float rays = (0.5 + 0.5 * sin(ang * 6.0 + t * 0.11)) * (0.5 + 0.5 * sin(ang * 13.0 - t * 0.07 + 2.0));
rays = pow(rays, 2.5) * (0.6 + 0.4 * B.Noise(float2(ang * 3.0, t * 0.05)));
col += float3(0.35, 0.05, 0.08) * rays * saturate(1.0 - length(dv) * 0.85) * 0.35;

// halo qui respire derrière le titre
float halo = exp(-dot((p - float2(0.5 * Aspect, 0.28)) * float2(0.9, 1.6), (p - float2(0.5 * Aspect, 0.28)) * float2(0.9, 1.6)) * 6.0);
col += float3(0.24, 0.03, 0.05) * halo * (0.75 + 0.25 * sin(t * 0.6));

// braises sur trois profondeurs, elles s'éteignent en montant
float e = B.Embers(p, t, 9.0, 0.55, 1.0) * 0.55;
e += B.Embers(p + 3.1, t, 15.0, 0.9, 7.0) * 0.4;
e += B.Embers(p + 7.7, t, 26.0, 1.4, 13.0) * 0.28;
e *= smoothstep(0.0, 0.75, UV.y);
col += float3(1.0, 0.33, 0.12) * e * Embers;

// vignette
float2 vu = (UV - 0.5) * float2(1.15, 1.35);
col *= lerp(0.3, 1.0, saturate(1.0 - dot(vu, vu) * 1.35));

// grain de film très léger
col += (B.Hash(UV * 1931.7 + frac(t * 0.37) * 97.0) - 0.5) * 0.014;

return pow(max(col, 0.0), Gamma) * Intensity;
