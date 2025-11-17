"""Post-processing recipe for Mech Ranger Portrait renders.

Applies tone mapping, contrast, and adaptive sharpening using pillow.
This script is intentionally lightweight so artists can adapt it quickly.
"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

from PIL import Image, ImageEnhance, ImageFilter

INPUT_DIR = Path("assets/previews/mech_ranger_raw")
OUTPUT_DIR = Path("assets/previews/mech_ranger_graded")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def iter_images(paths: Iterable[Path]) -> Iterable[Path]:
    for path in paths:
        if path.suffix.lower() in {".png", ".jpg", ".jpeg"}:
            yield path


def grade_image(image: Image.Image) -> Image.Image:
    graded = image.convert("RGB")
    graded = ImageEnhance.Color(graded).enhance(0.9)  # mute oversaturated highlights
    graded = ImageEnhance.Contrast(graded).enhance(1.1)
    graded = ImageEnhance.Brightness(graded).enhance(1.05)
    graded = graded.filter(ImageFilter.UnsharpMask(radius=2, percent=130, threshold=3))
    return graded


def process() -> None:
    input_paths = list(iter_images(INPUT_DIR.glob("*.png"))) + list(iter_images(INPUT_DIR.glob("*.jpg")))
    if not input_paths:
        print(f"No images found in {INPUT_DIR}. Populate the folder and rerun.")
        return

    for path in input_paths:
        with Image.open(path) as img:
            graded = grade_image(img)
            output_path = OUTPUT_DIR / path.name
            graded.save(output_path)
            print(f"Saved graded render to {output_path}")


def main() -> None:
    process()


if __name__ == "__main__":
    main()
