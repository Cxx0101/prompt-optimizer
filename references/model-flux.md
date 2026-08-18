# FLUX Adapter

Use for Black Forest Labs FLUX models.

## Prompt dialect

Prefer clear natural language. A strong portable structure is:

Subject + Action + Style/medium + Context

Then add composition, lighting, material, color, typography, or camera language only as needed.

## Important rule

For current FLUX.2 workflows, do not create a separate generic negative prompt. Describe the desired state positively.

Examples:

- use "sharp focus throughout" instead of "no blur";
- use "an empty gallery with no visible visitors" only when the absence is semantically necessary;
- use "clean uncluttered background" instead of a long negative list.

## Photorealism

Camera/lens references can be useful when they describe perspective and rendering character. Do not add them mechanically.

## Text and brand color

- Put visible text in quotation marks.
- Attach exact colors to exact objects: "the label is #1E40AF" rather than a detached palette list.

## Structured prompts

If the user's FLUX interface explicitly supports JSON structured prompting and the scene is complex, a structured object can be useful. Otherwise return natural language.

## Multi-reference editing

State the role of each image:

- image 1 = subject identity;
- image 2 = clothing/product;
- image 3 = background or style.

Then explain how they should combine.

## Output form

Return a natural-language prompt. Only include API-specific parameters when the user provides the interface/model and asks for them.
