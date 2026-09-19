# Resume

A single-page, fully responsive résumé for 李建緯 (Wei Lee), built in a cyberpunk / holographic-HUD visual style: dark navy field, neon-cyan frame with an animated light streak, magenta accents, scanline grid background, and an animated radar graphic.

**Live site:** see repository "About" / GitHub Pages link.

## Stack

Plain HTML + CSS, no build step, no dependencies. Fonts loaded from Google Fonts (Orbitron, Poppins, Noto Sans TC).

## Structure

```
index.html            page markup
assets/style.css       all styling, tokens, keyframes
assets/avatar3.jpg     portrait
assets/*.ico, *.png    favicon / apple-touch-icon / android icons
site.webmanifest       PWA/home-screen manifest
```

## Accessibility

- Reduced motion: every decorative animation is disabled under `prefers-reduced-motion: reduce`.
- The glitch-text name duplicates are `aria-hidden` so screen readers announce "Wei Lee" once.
- Visible focus rings on the three contact links.

## Responsive behavior

Fully fluid (`clamp()`-based type and spacing, no fixed widths). The two-column body collapses to a single column via flex-basis below ~700–770px. Verified at 360 / 768 / 1120 / 1600px.

## Local preview

```bash
python3 -m http.server 8843
```

Then open `http://localhost:8843`.
