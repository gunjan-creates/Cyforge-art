# Cyforge Art

Cyforge Art is a creative playground for experimenting with generative art pipelines, tooling, and assets. The repository collects reusable workflows, example prompts, and automation scripts that streamline the process of crafting stylized visuals with modern AI-assisted techniques.

## Why This Repo Exists
- explore generative art techniques with a repeatable, open workflow
- document lessons learned while iterating on different visual styles
- share reusable assets (brushes, prompt templates, node graphs, etc.) for the community

## What's Inside
- `prompts/` — curated prompt snippets organized by style, subject, and medium
- `workflows/` — automation scripts and notebooks for batch rendering or upscaling
- `assets/` — shared textures, LUTs, and reference palettes
- `docs/` — deep dives on experiments, configuration notes, and gallery pieces

*(Folder names are illustrative — adjust to match the actual structure as it evolves.)*

## Getting Started

1. Clone the repo:
	```bash
	git clone https://github.com/gunjan-creates/Cyforge-art.git
	cd Cyforge-art
	```
2. Spin up the development container (or install the dependencies defined in `docs/setup.md`).
3. Explore the `prompts/` and `workflows/` directories to kick off your own render experiments.

## Suggested Workflow
- start with a base prompt from `prompts/`
- iterate in your generator of choice (ComfyUI, Stable Diffusion WebUI, Midjourney, etc.)
- document successful iterations in `docs/experiments/<experiment-name>.md`
- commit reference outputs or thumbnails to keep a visual changelog

## Contributing
- open an issue describing the visual style or tooling you are adding
- use concise commit messages that describe the experiment or asset
- include preview images (compressed) whenever possible

## Roadmap Ideas
- publish ready-to-run ComfyUI graphs alongside sample renders
- bundle frequent color palettes as `.cube` or `.ase` files
- script post-processing recipes (e.g., automatic denoising + upscaling)

## License

Specify how you want others to use the art and code here (e.g., Creative Commons, MIT, or custom). Update this section once a licensing decision is made.

---

Questions or collaboration ideas? Open an issue or reach out at `hello@gunjancreates.art`.
