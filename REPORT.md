# Tealon Theme Build Report

## Reference analysis

The source `omarchy-lumon-theme` was analyzed as a coordinated multi-surface theme. Its main implementable elements were: semantic palette, shell tokens, Hyprland borders/decoration, hyprlock, GTK, Walker, notifications, OSD, Waybar, terminal palettes, and application/editor integrations. Its non-config elements included branded ASCII art, launcher/icon files and scripts, multiple wallpapers, a video, and a desktop preview.

The supplied geometric reference is dominated by near-black (`#060708`), deep teal/blue architectural surfaces (`#081B24`, `#0F2832`, `#103848`, `#144557`), electric cyan traces (`#13738C`, `#158CA3`, `#24C4D3`), and coral/orange signal accents (`#AA4C37`, `#CB6551`, `#E18A72`). Tealon uses those roles in a dark semantic palette with light text for readable UI states.

## Built

- Replaced the starter moss palette with a complete dark Tealon palette in `colors.toml`, including semantic roles, ANSI normal/bright colors, selection, muted text, and background hierarchy.
- Ported and recolored the source theme's supported text/config integrations: `shell.toml`, `hyprland.conf`, `hyprlock.conf`, `gtk.css`, `walker.css`, `mako.ini`, `swayosd.css`, `hyprland-preview-share-picker.css`, `colors.css`, `waybar.css`, terminal configs, and application/editor configs.
- Updated `README.md`, `CREDITS.md`, and media metadata to describe the implementation honestly and keep the scaffold's development status.
- Kept the existing scaffold evidence directory and did not claim live or registry validation.

## Not built / intentionally excluded

- No new background was generated, copied, or transformed. The supplied `backgrounds/01-geometric-leader.jpg` remains only a reference in the scaffold.
- No video, wallpaper set, contact sheet, desktop screenshot, a fabricated desktop preview, branded Lumon artwork, ASCII logo, launcher desktop entry, application icons, or install/uninstall launcher scripts were taken.
- No live theme application, desktop screenshot capture, Git-installed staging test, or registry submission was performed.
- App-specific files are included as source integrations, but Git-installed Omarchy staging may omit several root terminal/Lua/VS Code files; generated built-in templates should be preferred at runtime. This needs live verification.
- Wallpaper redistribution permission remains pending and is not asserted.

## Verification

- Local scaffold helper check and handoff are recorded after implementation in `evidence/checks.tsv`.
- Static TOML syntax, image decoding/dimensions, and repository layout are checked locally where tooling is available.
- Live and registry checks remain `not-run` because no live desktop or submission authorization was provided.
