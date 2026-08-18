# Workflow: Image Editing and Reference-Based Generation

## Core pattern

**Change → Preserve → Constraints**

## Surgical edit

When only part of an image should change:

1. Name the exact region/object to change.
2. State the intended replacement/transformation.
3. List what must remain identical.
4. Require light, shadow, perspective, scale, and reflections to integrate with the original.
5. Prevent unintended collateral edits.

## Reference roles

For multiple input images, assign roles explicitly:

- identity reference;
- product reference;
- pose/composition reference;
- material reference;
- color/style reference;
- background/location reference.

Do not say only "combine these images".

## Style transfer

Separate content from style:

- preserve geometry/identity/composition;
- transfer palette, mark-making, material treatment, line quality, lighting behavior, or print/process characteristics.

If exact style copying is unsuitable, translate the style into descriptive visual traits.

## Outpainting

State:

- extension direction;
- new content needed outside the original frame;
- continuity of horizon, perspective, lighting, texture, and repeating patterns;
- what central content must remain untouched.
