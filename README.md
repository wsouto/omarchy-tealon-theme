# Omarchy Tealon Theme

<p>
  <a href="https://github.com/tcballard/omarchy-badges"><img alt="Built for Omarchy: Theme" height="20" src="https://raw.githubusercontent.com/tcballard/omarchy-badges/75975e5b5bf75e7ede3764bcd2950046f7abfe2c/badges/v1/omarchy-theme.svg"></a>
  <img alt="Target: Omarchy 4" height="20" src="https://img.shields.io/badge/target-Omarchy_4-24967E?style=flat-square">
  <img alt="Status: development preview" height="20" src="https://img.shields.io/badge/status-development_preview-D06A55?style=flat-square">
</p>

Status: development preview  
Intended Omarchy target: 4.x / Quattro  
Tested installed Omarchy version: 4.0.3-1

A dark architectural theme derived from the supplied geometric artwork: near-black voids, deep teal structures, electric cyan focus states, and coral signals.

The category badge is a community label, not certification. The target range is not a future-compatibility guarantee.

## Supplied reference

![Supplied color reference and development wallpaper; not a desktop screenshot and not newly generated](backgrounds/01-geometric-leader.jpg)

## Design

`colors.toml` is the authoritative theme source. Omarchy generates shell, terminal, editor, browser, and application configurations from it, avoiding copied app files that drift from the semantic palette or are discarded during Git-installed staging.

- Primary focus and accent: electric cyan
- Background hierarchy: near-black through deep teal
- Error and attention: coral
- Warning: warm amber
- Success: green-teal
- Selection text: bright foreground on deep teal
- Icons: `Yaru-blue`

## Install

For local development, link or copy this directory to an unused `~/.config/omarchy/themes/tealon`, record the current theme and background, then run:

```bash
omarchy theme set tealon
```

Do not overwrite a modified installed copy. A future published repository should document its exact URL for `omarchy theme install`; installation can replace an existing destination and immediately applies the theme.

## Rollback

Run `omarchy theme set <previous-theme>`, restore the recorded background with `omarchy theme bg next` if necessary, and remove the development copy only after switching away. This procedure was exercised successfully on Omarchy 4.0.3-1.

## Included

- Complete semantic dark palette in `colors.toml`
- Wallpaper/reference image in `backgrounds/`
- `Yaru-blue` icon selection
- Palette-driven Omarchy-generated integrations rather than copied terminal, editor, shell, or legacy CSS files

## Validation limits

On Omarchy 4.0.3-1, the theme was applied from both a local development symlink and a Git-marked staging copy. Both generated identical top-level theme files. The shell survived a restart, and the bar, root menu, notification, Ghostty ANSI palette, Neovim syntax theme, wallpaper, active borders, and GTK dark-mode/icon integration were observed. The previous theme and recorded wallpaper were restored.

Helix was not tested because it is not installed. Lock-screen interaction, disabled controls, mixed display scales, registry validation, and wallpaper redistribution rights remain unverified. GTK applications receive Omarchy's dark/light mode and icon selection; they do not receive a full Tealon GTK color stylesheet.

See [validation evidence](evidence/checks.tsv) and [the implementation report](REPORT.md).

## Credits and licensing

See [CREDITS.md](CREDITS.md). Wallpaper redistribution permission and a code-license choice remain pending, so this development tree is not release-ready.
