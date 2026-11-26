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

    // une couche de poussières qui montent doucement, une au plus par case
    float Embers(float2 p, float t, float scale, float speed, float seed)
    {
        float2 q = p * scale;
        q.y += t * speed;
        q.x += sin(q.y * 0.35 + seed) * 0.6;
        float2 cell = floor(q);
        float2 f = frac(q) - 0.5;
        float2 rnd = Hash2(cell + seed);
        float alive = step(rnd.x, 0.10);
        float2 pos = (rnd - 0.5) * 0.7;
        float d = length(f - pos);
        float size = 0.010 + 0.012 * rnd.y;
        float flicker = 0.6 + 0.4 * sin(t * (0.6 + rnd.y) + rnd.x * 40.0);
        float core = smoothstep(size, 0.0, d);
        float glow = 0.0;
        return (core + glow) * flicker * alive;
    }
};

SteezyBackground B;
float2 p = float2(UV.x * Aspect, UV.y);
float t = Time * Speed;

// fond presque noir, à peine plus chaud au centre
float2 centre = float2(0.5 * Aspect, 0.42);
float r = length((p - centre) * float2(0.75, 1.0));
float3 col = lerp(float3(0.030, 0.012, 0.014), float3(0.008, 0.006, 0.007), saturate(r * 1.1));

// fumée très discrète qui dérive lentement, on la devine plus qu'on ne la voit
float2 sp = p * 1.3 + float2(t * 0.010, t * 0.004);
float2 w = float2(B.Fbm(sp + float2(0.0, t * 0.015)), B.Fbm(sp + float2(5.2, 1.3) - t * 0.012));
float smoke = smoothstep(0.45, 0.95, B.Fbm(sp + 1.8 * w));
col += float3(0.035, 0.010, 0.012) * smoke;

// quelques poussières qui flottent, rares et à peine visibles
float e = B.Embers(p, t, 11.0, 0.12, 1.0) * 0.5;
e += B.Embers(p + 7.7, t, 19.0, 0.2, 13.0) * 0.3;
col += float3(0.55, 0.30, 0.28) * e * Embers;

// vignette
float2 vu = (UV - 0.5) * float2(1.1, 1.3);
col *= lerp(0.45, 1.0, saturate(1.0 - dot(vu, vu) * 1.3));

// grain de film très léger
col += (B.Hash(UV * 1931.7 + frac(t * 0.37) * 97.0) - 0.5) * 0.008;

return pow(max(col, 0.0), Gamma) * Intensity;
