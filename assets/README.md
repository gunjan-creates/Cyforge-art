# Asset Library

Reusable textures, lookup tables, color palettes, and reference sheets that support Cyforge Art experiments.

## Structure

- `previews/` – thumbnails and low-res outputs for quick browsing
- `textures/` – noise maps, brush patterns, overlays, etc.
- `palettes/` – color references in `.png`, `.ase`, `.cube`, or `.json`
- `references/` – moodboards, pose sheets, composition guides

## Usage

- Keep source files lightweight; link to large originals via external storage if needed.
- Document the origin or license of third-party assets in a `LICENSE.md` or inline note.
- Compress previews to stay under 500 KB per image.

## Contribution Notes

- Name assets with `YYYY-MM-DD_descriptor.ext` to keep the library tidy.
- Include a short README or metadata file when introducing a new subfolder.
- Avoid committing proprietary or restricted assets.
