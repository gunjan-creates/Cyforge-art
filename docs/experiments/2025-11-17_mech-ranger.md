# Experiment: 2025-11-17 Mech Ranger Portrait

## Goal
- Explore lighting and finish variations for the Mech Ranger character prompt.

## Inputs
- Prompt: `prompts/subjects/2025-11-17_mech-ranger.md`
- Palette: `assets/palettes/2025-11-17_mech-ranger.json`
- Post Workflow: `workflows/post/mech_ranger_grade.py`
- Model: `SDXL 1.0`
- Sampler: Euler a
- Steps: 30
- CFG Scale: 8
- Resolution: 832x1024

## Process
- Generated base renders for three environments (`sunset desert`, `snowy ridge`, `overgrown ruins`).
- Tweaked armor finish between `weathered` and `battle scarred` per environment.
- Applied the grading script to all outputs; results saved under `assets/previews/mech_ranger_graded/` (pending actual renders).

## Results
- Raw renders directory (create and populate): `assets/previews/mech_ranger_raw/`
- Graded outputs: `assets/previews/mech_ranger_graded/`
- Representative thumbnails to be added as `assets/previews/2025-11-17_mech-ranger_<variant>.jpg`.

## Learnings
- Amber visor highlight clips when CFG exceeds 8; consider local adjustments in ControlNet.
- Snowy environment benefits from slight blue temperature shift post grade; adjust script or palette.
- Next steps: experiment with alternate samplers (Heun) and add weapon-specific control poses.
