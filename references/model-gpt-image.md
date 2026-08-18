# GPT Image Adapter

Use for OpenAI image generation/editing models, especially GPT Image family.

## Prompt dialect

Prefer clear natural language with explicit relationships and constraints. Write like an art director giving a precise visual brief, not like a tag list.

Recommended order:

1. goal / image type;
2. subject and action;
3. environment and relationships;
4. framing and composition;
5. lighting and color;
6. materials and visual finish;
7. exact text/layout when needed;
8. preservation rules for edits.

## Strengths to exploit

- complex natural-language instructions;
- image editing with explicit preservation;
- text rendering when exact copy and hierarchy are specified;
- multi-part scenes when relationships are described unambiguously;
- high-fidelity use of image inputs when the host exposes them.

## Editing pattern

Use direct, operational language:

"Using the provided image, change X. Keep Y exactly unchanged. Preserve Z. Match the new lighting/reflections to the existing camera and perspective."

Do not restate the entire desired image as if generating from scratch when only one element changes.

## Text in image

Quote exact copy and specify:

- position;
- hierarchy;
- type category;
- case;
- approximate scale;
- what other text must not appear.

## Negative constraints

Prefer positive, direct constraints inside the natural-language prompt:

- "an empty background" rather than a long generic negative list;
- "natural skin texture and anatomically plausible hands" rather than quality-tag spam.

Use a separate negative section only if the user's interface explicitly supports one.

## Output form

Return one coherent natural-language prompt. Do not append Midjourney flags, Stable Diffusion weights, or invented API parameters.
