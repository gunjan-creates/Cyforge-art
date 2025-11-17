# Prompt Library

This folder collects prompt snippets organized by style, subject, and medium. Each subfolder focuses on a specific aesthetic direction so you can quickly jump into experimentation.

## Structure

- `styles/` – genre-driven prompts (sci-fi neon, painterly, low-poly, etc.)
- `subjects/` – character, environment, and object-focused seeds
- `techniques/` – prompts that highlight workflows such as photobashing, glitching, or line-art extraction

## Usage

1. Copy a prompt into your preferred generator (ComfyUI, Stable Diffusion WebUI, Midjourney, etc.).
2. Tweak the prompt variables marked in **bold** or inside `{{curly_braces}}` to customize outputs.
3. When a prompt produces a result you like, document the render parameters in `../docs/experiments/` and drop a thumbnail into `../assets/previews/`.

## Contribution Notes

- Keep prompts concise and annotated with resolution, sampler, and CFG scale when applicable.
- Include links to reference images or palettes if they influenced the prompt.
- Follow the naming convention: `YYYY-MM-DD_keyword.md` for standalone prompt files.
