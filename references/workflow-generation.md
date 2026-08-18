# Workflow: Text-to-Image Generation

## Goal

Convert a rough idea into a coherent first-generation prompt without overfitting the brief.

## Procedure

1. Identify the subject, action/state, and purpose.
2. Add only the environmental details needed to support the subject.
3. Choose one clear composition and viewpoint.
4. Choose one coherent lighting setup.
5. Specify material/color/style details that matter.
6. Add exact text only if requested.
7. Add output geometry when useful.
8. Compile using the target model adapter.
9. Tighten the prompt by removing redundant praise or duplicate descriptors.

## Good defaults when unspecified

- one primary subject;
- readable separation from background;
- balanced composition;
- plausible light direction;
- moderate detail rather than maximum detail;
- no extra text/logos unless requested.

## Avoid

- inventing narrative characters or props that change the concept;
- choosing an extreme lens or Dutch angle without a reason;
- turning every night scene into cyberpunk;
- adding fog, sparks, bloom, bokeh, lens flare, rain, and neon simultaneously.
