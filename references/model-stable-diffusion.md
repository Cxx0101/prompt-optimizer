# Stable Diffusion / SDXL / SD3.x Adapter

Use when the user targets a Stable Diffusion-family workflow.

## First identify the interface assumptions

Stable Diffusion behavior varies by model, UI, sampler, ControlNet/Adapter support, LoRAs, and prompt parser. If the user specifies Automatic1111, ComfyUI, Invoke, Fooocus, or another interface, respect its syntax.

If no interface is named, return a portable positive prompt and an optional conservative negative prompt.

## Positive prompt

Use a structured description rather than pure tag soup:

subject/action → environment → composition → lighting → materials → style/medium → technical finish

For older tag-oriented checkpoints, concise comma-separated descriptors may work better than prose. Adapt to the checkpoint if the user names it.

## Weighting

Do not invent weighting syntax for an unknown parser. If the user's workflow supports `(term:1.2)` or similar syntax, use weights sparingly for genuinely important concepts.

## Negative prompt

A separate negative prompt can be useful in diffusion workflows. Keep it targeted to likely failure modes rather than copying a universal 50-term list.

Example categories:

- anatomy failures when people are present;
- text/watermarks when unwanted;
- low-resolution artifacts;
- clutter when clean composition matters;
- style leakage when a specific medium is required.

## Control tools

If the user uses ControlNet/OpenPose/depth/canny/IP-Adapter/LoRA:

- describe appearance and semantic intent in text;
- let the control input define geometry/pose/style where appropriate;
- do not fight the control signal with contradictory prompt language.

## Output form

Return:

1. Positive Prompt
2. Negative Prompt, only if useful
3. Optional workflow notes only when the user asks for node/settings guidance
