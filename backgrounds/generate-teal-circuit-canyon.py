#!/usr/bin/env python3
"""Render an original 3840×2160 Teal Circuit Canyon desktop background."""
from __future__ import annotations

import html
import random
from pathlib import Path

W, H = 3840, 2160
OUT = Path(__file__).with_name("02-teal-circuit-canyon.jpg")
SVG = Path(__file__).with_name("02-teal-circuit-canyon.svg")
rng = random.Random(20260916)

# Screen-space axonometric projection.
def p(x: float, y: float, z: float = 0) -> tuple[float, float]:
    return (1920 + (x - y) * 48, 390 + (x + y) * 26 - z * 1.42)

def pts(points: list[tuple[float, float]]) -> str:
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)

def poly(points: list[tuple[float, float]], fill: str, stroke: str = "none", sw: float = 1) -> str:
    return f'<polygon points="{pts(points)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'

def line(points: list[tuple[float, float]], stroke: str, sw: float, opacity: float = 1) -> str:
    return f'<polyline points="{pts(points)}" fill="none" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}" stroke-linecap="square" stroke-linejoin="miter"/>'

def block(x: float, y: float, w: float, d: float, z: float, h: float, accent: bool = False, amber: bool = False) -> str:
    a, b, c, e = p(x, y, z), p(x + w, y, z), p(x + w, y + d, z), p(x, y + d, z)
    aa, bb, cc, ee = p(x, y, z + h), p(x + w, y, z + h), p(x + w, y + d, z + h), p(x, y + d, z + h)
    # Right and left facades first, then the roof.
    s = [poly([b, c, cc, bb], "#07161d"), poly([e, a, aa, ee], "#0a222c"), poly([aa, bb, cc, ee], "#123542")]
    # A very restrained top-plane sheen yields physical depth without gradients.
    if h > 70 and rng.random() < 0.44:
        inner = [p(x + w*.12, y + d*.12, z+h+.7), p(x+w*.86, y+d*.12, z+h+.7), p(x+w*.86, y+d*.86, z+h+.7), p(x+w*.12, y+d*.86, z+h+.7)]
        s.append(poly(inner, "#0e2d38"))
    if accent:
        col = "#18d6e6" if not amber else "#ff785d"
        s.append(line([aa, bb, cc], col, 4.2, .88))
        if h > 110:
            # Vertical luminescent well, deliberately asymmetric.
            q = p(x+w*.12 if amber else x+w*.88, y+d*.14, z+h*.12)
            q2 = p(x+w*.12 if amber else x+w*.88, y+d*.14, z+h*.82)
            s.append(line([q, q2], col, 4.6, .90))
    if rng.random() < 0.26:
        s.append(line([aa, bb], "#55e6ef", 1.4, .52))
    return "".join(s)

parts: list[str] = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
 <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#020609"/><stop offset=".55" stop-color="#050c10"/><stop offset="1" stop-color="#010405"/></linearGradient>
 <radialGradient id="mist" cx="70%" cy="45%" r="65%"><stop stop-color="#0b2530" stop-opacity=".32"/><stop offset=".58" stop-color="#071116" stop-opacity=".10"/><stop offset="1" stop-color="#000000" stop-opacity="0"/></radialGradient>
 <filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="100%" height="100%" fill="url(#bg)"/>
<rect width="100%" height="100%" fill="url(#mist)"/>
''']

# Low-contrast substrate channels. The empty left third is intentionally preserved.
for gx in range(-20, 25):
    for gy in range(-8, 25):
        if rng.random() < .24:
            x, y = gx*2.1, gy*2.0
            a, b = p(x, y), p(x+1.55, y+1.35)
            parts.append(line([a, b], "#0d2b35", 2, .36))

# Center-to-right mass: group blocks across three terraced terraces.
positions: list[tuple[float, float, float, float, float, float]] = []
for band, (xmin, xmax, ymin, ymax, base) in enumerate([(-7, 20, -4, 22, 35), (-1, 28, -10, 13, 95), (8, 35, 4, 29, 50)]):
    for _ in range(54 if band != 1 else 45):
        x = rng.uniform(xmin, xmax)
        y = rng.uniform(ymin, ymax)
        # Preserve a diagonal void/canyon and a calm left-side margin.
        if -2 < (y - x) < 4 or (x < -3 and y < 12):
            continue
        w, d = rng.choice([1.4, 1.7, 2.1, 2.6, 3.1]), rng.choice([1.3, 1.7, 2.2, 2.7])
        z = rng.choice([0, 0, 20, 34])
        h = base + rng.uniform(38, 250) + (150 if band == 1 and rng.random() < .25 else 0)
        positions.append((x, y, w, d, z, h))

# Draw order follows depth (projected y) to prevent foreground from being covered.
positions.sort(key=lambda q: q[0]+q[1])
for i, (x, y, w, d, z, h) in enumerate(positions):
    cyan = (i % 7 == 0) or (h > 300 and i % 3 == 0)
    amber = (i % 23 == 0)
    parts.append(block(x, y, w, d, z, h, cyan or amber, amber))

# Tall pylons give the scene a different silhouette from the reference: a corridor, not a dense city core.
for x, y, h, cyan in [(7,-3,550,True),(11,1,460,False),(16,7,590,True),(18,-4,390,False),(22,9,510,True),(3,14,430,False)]:
    parts.append(block(x, y, 1.35, 1.5, 0, h, True, not cyan))

# Suspended bridges cross the canyon without closing it.
for x, y, length, amber in [(-3,10,9,False),(5,3,8,True),(9,15,7,False),(13,-1,7,False)]:
    z=255 if not amber else 330
    parts.append(block(x, y, length, .52, z, 34, True, amber))

# Routed signal traces / amber junctions on the floor and facades.
traces = [
 [(-14,13),(-9,13),(-9,8),(-4,8),(-4,4)],
 [(-4,22),(2,22),(2,18),(7,18),(7,13)],
 [(5,-8),(5,-3),(10,-3),(10,3),(15,3)],
 [(14,21),(20,21),(20,15),(27,15)],
 [(20,-9),(25,-9),(25,-3),(31,-3)],
]
for n, route in enumerate(traces):
    pp = [p(x,y,6) for x,y in route]
    parts.append(line(pp, "#ff735b" if n in (0,3) else "#13bccd", 4.2, .86))
    # subtle glow only below the crisp trace
    parts.append(f'<polyline points="{pts(pp)}" fill="none" stroke="{"#ff735b" if n in (0,3) else "#13bccd"}" stroke-width="13" opacity=".15" filter="url(#glow)"/>')

# Isolated cyan stations in the calm margins offer depth without visual noise.
for x,y in [(-17,6),(-12,20),(26,-10),(30,2),(23,27)]:
    a,b,c,d = p(x,y,8), p(x+1.5,y,8), p(x+1.5,y+1.2,8), p(x,y+1.2,8)
    parts.append(poly([a,b,c,d], "#0f4d5b"))
    parts.append(line([a,b,c], "#20d4e4", 3, .76))

# Hairline architectural fragments at the outer perimeter.
for _ in range(40):
    x, y = rng.choice([rng.uniform(-26,-15), rng.uniform(27,39)]), rng.uniform(-14,30)
    a=p(x,y, rng.uniform(0,40)); b=p(x+rng.uniform(.5,2.7),y, rng.uniform(0,40))
    parts.append(line([a,b], "#113946", 2, .55))

parts.append('</svg>')
SVG.write_text("".join(parts), encoding="utf-8")
print(SVG)
print(OUT)
