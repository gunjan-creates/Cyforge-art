"""Batch render helper for the Neon City Dreamscape prompt.

This script expands prompt variables and serializes a job queue that can be fed into
ComfyUI or another automation layer. It avoids direct integration with rendering
APIs so it can serve as a portable starting point.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Iterable
import json

ROOT = Path(__file__).resolve().parents[2]
PROMPT_FILE = ROOT / "prompts" / "styles" / "2025-11-17_neon-city.md"
QUEUE_OUTPUT = ROOT / "workflows" / "batch" / "neon_city_queue.json"
PALETTE_FILE = ROOT / "assets" / "palettes" / "2025-11-17_neon-city.json"


@dataclass(frozen=True)
class PromptConfig:
    weather: str
    crowd_density: str
    hero_element: str

    def render(self) -> str:
        base_prompt = "ultra wide shot of a neon-lit mega city at dusk, reflective rain-soaked streets, " \
            "volumetric fog, glowing holographic billboards, cinematic lighting, vibrant magenta and cyan " \
            "color palette, sharp focus, detailed architecture, 35mm lens, film grain"
        return (
            f"{base_prompt}, {self.weather}, {self.crowd_density}, {self.hero_element}"
        )


def expand_configs() -> Iterable[PromptConfig]:
    weathers = ["soft rain", "humid haze", "light snowfall"]
    crowds = ["empty boulevard", "hover traffic", "rush hour crowds"]
    heroes = [
        "solitary figure holding an umbrella",
        "sleek hover car trail",
        "street vendor stall with warm lanterns",
    ]
    for weather, crowd, hero in product(weathers, crowds, heroes):
        yield PromptConfig(weather=weather, crowd_density=crowd, hero_element=hero)


def build_queue(configs: Iterable[PromptConfig]) -> list[dict[str, str]]:
    queue = []
    for config in configs:
        queue.append(
            {
                "prompt": config.render(),
                "negative_prompt": (
                    "low detail, deformed, distorted, text, watermark, logo, "
                    "low resolution, oversaturated, noisy background, monochrome"
                ),
                "steps": 35,
                "cfg_scale": 7.5,
                "sampler": "DPM++ 2M Karras",
                "resolution": "768x512",
                "palette": str(PALETTE_FILE.relative_to(ROOT)),
            }
        )
    return queue


def save_queue(queue: list[dict[str, str]]) -> None:
    QUEUE_OUTPUT.write_text(
        json.dumps({"jobs": queue}, indent=2),
        encoding="utf-8",
    )


def main() -> None:
    configs = list(expand_configs())
    queue = build_queue(configs)
    save_queue(queue)
    print(f"Saved {len(queue)} jobs to {QUEUE_OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
