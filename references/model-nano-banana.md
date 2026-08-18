# Gemini / Nano Banana Adapter

Use for Google's native Gemini image generation models commonly referred to as Nano Banana.

## Prompt dialect

Use natural, conversational visual direction. Rich scene descriptions, edits, iterative refinements, and mixed text+image instructions are appropriate.

## Generation

Describe:

- what the image is for;
- primary subject/action;
- scene relationships;
- composition;
- lighting/color/material;
- exact text if present;
- aspect ratio or intended format when useful.

## Editing

Use direct instructions that distinguish changed and preserved content:

"Use the supplied image as the base. Replace only the background with X. Keep the person, pose, face, clothing, crop, and lens perspective unchanged. Match the new background light to the existing subject."

## Reference images

State each reference's role. Do not rely on "same style" without describing what should transfer.

## Typography and layouts

Quote exact required text and specify hierarchy. For dense magazine/poster layouts, keep copy concise enough to fit the composition.

## Model choice

If the user has access to multiple Nano Banana variants and asks for a recommendation, choose based on their stated priority: speed/cost vs complex professional asset production. Do not silently switch models.

## Output form

Return one natural-language prompt. Do not append Midjourney flags or diffusion weights.
