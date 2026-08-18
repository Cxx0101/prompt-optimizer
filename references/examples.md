# Examples

These examples demonstrate behavior, not mandatory wording.

## Example 1 — Rough Chinese idea → portable prompt

Input:

> 一个女生坐在咖啡馆窗边，很有电影感，外面下雨。

Output:

### Final Prompt

A quiet cinematic photograph of a young woman sitting alone beside a cafe window on a rainy evening, turned slightly toward the glass with a calm, introspective expression. Medium shot at eye level, subject placed on the right third with negative space toward the rain-streaked window. Warm practical cafe light softly shapes her face while cool blue-gray street light enters from outside, creating restrained warm-cool separation. Natural skin texture, subtle fabric wrinkles, realistic reflections and droplets on the glass, softly layered city lights outside, low-saturation color grade, intimate and understated rather than glossy or theatrical.

## Example 2 — Midjourney

Input:

> Midjourney，做一个高端香水广告，黑色玻璃瓶，极简，16:9。

Output:

### Final Prompt

luxury fragrance campaign, a single black glass perfume bottle centered on a low matte stone pedestal, precise silhouette and crisp label area, large negative space, minimal architectural studio set, controlled softbox highlight tracing the bottle edges, subtle reflected light revealing the glass thickness, charcoal and warm gray palette with one restrained amber accent, premium editorial product photography, clean shadow geometry, no decorative clutter --ar 16:9 --raw

## Example 3 — Surgical edit

Input:

> 把这张白天街拍改成雨夜，人物完全不要动。

Output:

### Final Prompt

Using the provided image as the base, change only the environment from daytime to a rainy night street. Keep the person exactly unchanged: same face, identity, body proportions, pose, clothing, hairstyle, position, crop, and camera perspective. Replace the daylight background with realistic wet pavement, restrained storefront and street lighting, and subtle rain. Add physically consistent cool ambient night light and soft practical-light reflections to the environment while preserving the subject's original form and detail; integrate only the minimum lighting shift needed to make the subject belong in the new night scene. Do not add people, change clothing, alter facial features, or modify the framing.

## Example 4 — Typography

Input:

> 做一张爵士音乐节海报，标题必须是 “MIDNIGHT BLUE”，副标题 “TOKYO JAZZ WEEK 2026”。

Output:

### Final Prompt

Vertical jazz festival poster with the exact headline "MIDNIGHT BLUE" dominating the upper third in a tall condensed sans-serif display type, and the exact subtitle "TOKYO JAZZ WEEK 2026" directly below in much smaller uppercase lettering. Deep midnight-blue field with a restrained cream and muted brass color system, abstract saxophone-like curves and geometric stage-light shapes forming a rhythmic asymmetrical composition, generous margins, sophisticated modernist editorial layout, subtle paper grain, strong typographic hierarchy, no additional text.

## Example 5 — Prompt diagnosis

Input:

> 为什么这个词不稳定：beautiful woman, cinematic, 8k, masterpiece, neon, bokeh, dramatic, realistic, Tokyo

Diagnosis:

- The subject has no action, identity, or placement.
- "cinematic", "dramatic", and "beautiful" are outcomes rather than controllable instructions.
- "neon" and "bokeh" are effects without a lighting or camera setup.
- Tokyo is not defined as street, interior, era, weather, or visual role.
- Quality tags consume prompt space without solving composition.

Corrected prompt:

A natural nighttime street portrait of a woman walking past a small Tokyo neighborhood restaurant after rain, medium shot at eye level, 50mm-like perspective, subject on the left third with warm lantern light from the storefront shaping one side of her face and cool ambient street light on the other. Wet asphalt carries restrained reflections, background signage is soft but readable as environmental texture rather than the focal point, natural skin and hair detail, low-saturation color grade, quiet documentary mood, realistic depth of field.
