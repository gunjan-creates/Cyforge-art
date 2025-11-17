# Prompt: Mech Ranger Portrait

## Metadata
- Date: 2025-11-17
- Subject: Character portrait
- Style: Hard-surface / Ranger hybrid
- Recommended Sampler: Euler a
- CFG Scale: 8
- Steps: 28–32
- Resolution: 832x1024
- Base Model: `SDXL 1.0`

## Base Prompt
```
hero portrait of a battle-ready mech ranger, sleek armor plates with matte olive drab finish, glowing amber visor, cape fluttering in desert wind, dramatic rim lighting, shallow depth of field, intricate mechanical joints, cinematic composition, concept art, artstation trending, detailed hard-surface render
```

## Negative Prompt
```
blurry, low detail, extra limbs, helmet off, distorted face, text, watermark, logo, grainy, sketch
```

## Variation Hooks
- **{{environment}}** — `sunset desert`, `snowy ridge`, `overgrown ruins`
- **{{armor_finish}}** — `weathered`, `sleek`, `battle scarred`
- **{{weapon_pose}}** — `longbow ready`, `energy spear held low`, `tactical pistol holstered`

## Notes
- Pair with the post-processing workflow `../../workflows/post/mech_ranger_grade.py` for tone mapping and sharpening.
- Use `../../assets/palettes/2025-11-17_mech-ranger.json` to keep earth tones balanced with accent highlights.
