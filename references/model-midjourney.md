# Midjourney Adapter

Use when the user targets Midjourney.

## Prompt dialect

Keep the prompt visually dense but readable. Front-load the subject and most important visual facts. Use commas or short clauses rather than a long explanatory essay.

Useful order:

Subject + action → environment → composition/viewpoint → lighting/color → style/material → mood → parameters

## Parameters

Parameters belong at the end of the prompt.

Use only when helpful:

- `--ar W:H` for aspect ratio;
- `--raw` when the user wants tighter control / less automatic house styling;
- `--s N` or `--stylize N` when the user explicitly wants a stylization level;
- `--c N` or `--chaos N` for controlled variation;
- `--no ...` for simple exclusions;
- `--sref ...` when the user supplies a style reference compatible with their Midjourney workflow;
- `--oref ...` for V7-era omni reference workflows when the user supplies a compatible reference;
- `--seed N` only when reproducibility/testing is useful.

Do not invent reference URLs or profile codes.

## Version drift

Midjourney evolves quickly. If the user names a specific current version or feature and exact syntax matters, prefer the syntax they supplied or verified documentation. Do not force `--v 7` or any version flag unless requested.

## Negative instructions

Use `--no` for simple objects/elements. Prefer positive wording for nuanced constraints because multi-word exclusions may be interpreted token by token.

## Prompt cleanup

Avoid legacy keyword soup such as:

"masterpiece, best quality, 8k, ultra detailed, award-winning"

Replace it with concrete visual direction.

## Output form

Return the text prompt followed by a single parameter suffix. Keep all parameters after the descriptive prompt.
