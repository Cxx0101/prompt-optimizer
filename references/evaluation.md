# Prompt Evaluation Rubric

Use this for difficult prompts, prompt diagnosis, or before returning a high-stakes production prompt.

Score each dimension 0–2.

## 1. Intent fidelity

- 0: changes the concept;
- 1: mostly preserved with drift;
- 2: central idea and hard constraints preserved.

## 2. Subject clarity

- 0: ambiguous focus;
- 1: subject named but weakly controlled;
- 2: subject/action/identity are visually clear.

## 3. Spatial grammar

- 0: list of objects with no relationships;
- 1: partial layout;
- 2: foreground/background/placement/scale relationships are clear where needed.

## 4. Composition

- 0: no framing guidance when important;
- 1: generic framing;
- 2: framing, viewpoint, crop, and negative space match purpose.

## 5. Lighting/color coherence

- 0: contradictory or decorative;
- 1: plausible but generic;
- 2: intentional light source, contrast, and palette.

## 6. Material/style specificity

- 0: empty adjectives;
- 1: some useful descriptors;
- 2: material and medium choices are concrete and coherent.

## 7. Model fit

- 0: wrong/deprecated syntax or blind negative prompt;
- 1: portable but not optimized;
- 2: adapter-appropriate language and parameters.

## 8. Constraint handling

- 0: ignores preserve/text/count constraints;
- 1: partially encoded;
- 2: hard constraints are explicit and testable.

## 9. Efficiency

- 0: heavy keyword soup/repetition;
- 1: some redundancy;
- 2: nearly every phrase controls an output property.

## 10. Generate-readiness

- 0: requires major interpretation;
- 1: usable with likely drift;
- 2: can be pasted into the target model with minimal ambiguity.

A strong production prompt should usually score at least 16/20 without relying on generic quality tags.
