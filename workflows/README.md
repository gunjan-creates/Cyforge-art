# Workflow Library

Automation scripts, node graphs, and notebooks that streamline rendering batches, post-processing, and upscaling.

## Structure

- `batch/` – pipelines for bulk prompt execution or queue management
- `upscaling/` – super-resolution and enhancement recipes
- `post/` – post-processing automation (color grading, denoising, etc.)

## Usage

1. Review each workflow's prerequisites in its local README or header comments.
2. Install dependencies with `pip install -r requirements.txt` or via the provided environment files.
3. Run the workflow on sample assets before adapting it to new prompts or models.

## Contribution Notes

- Provide a short description, expected inputs, and output formats.
- Keep configuration values in `.json` or `.yaml` when possible to separate code from presets.
- Include a thumbnail or link to renders that demonstrate the workflow's results.
