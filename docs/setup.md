# Environment Setup

## 1. Prerequisites

- Python 3.11+
- Git 2.45+
- CUDA-compatible GPU (optional but recommended for local rendering)
- Conda or `uv` (preferred) for environment management

## 2. Create Environment

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

If you favor Conda:

```bash
conda create -n cyforge python=3.11
conda activate cyforge
pip install -r requirements.txt
```

## 3. Tooling

- Stable Diffusion WebUI or ComfyUI installed locally, or access to a cloud-based generator.
- Optional: `imagemagick`, `ffmpeg`, and `exiftool` for batch post-processing.

## 4. Configuration Files

- Place model checkpoints in `models/` (ignored by default).
- Update `.env` or `config/*.yaml` (to be added) with API keys for external services.

## 5. Verification

1. Run a smoke test workflow from `workflows/` using sample inputs.
2. Render a prompt from `prompts/styles/` to confirm end-to-end setup.
3. Document the run in `docs/experiments/`.

> Update this document as the toolchain evolves.
