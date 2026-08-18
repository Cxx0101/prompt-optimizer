# Image Prompt Optimizer

A cross-agent Skill for turning rough visual ideas into production-ready image-generation or image-editing prompts.

Designed for:

- Claude Code
- OpenAI Codex
- Hermes Agent
- other clients compatible with the Agent Skills open format

## What it does

- preserves the user's original creative intent;
- builds an internal Universal Visual Brief;
- upgrades composition, camera language, lighting, color, materials, and spatial relationships;
- handles generation, image edits, references, character/product consistency, product advertising, posters, and typography;
- compiles prompts into model-appropriate dialects instead of using one prompt format everywhere;
- avoids generic prompt bloat and blind negative-prompt copying.

Included adapters:

- GPT Image
- Midjourney
- FLUX
- Gemini / Nano Banana
- Stable Diffusion / SDXL / SD3.x
- Ideogram

## Package structure

```text
image-prompt-optimizer/
├── SKILL.md
├── README.md
├── LICENSE
├── SOURCES.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── visual-language.md
│   ├── evaluation.md
│   ├── examples.md
│   ├── model-gpt-image.md
│   ├── model-midjourney.md
│   ├── model-flux.md
│   ├── model-nano-banana.md
│   ├── model-stable-diffusion.md
│   ├── model-ideogram.md
│   ├── workflow-generation.md
│   ├── workflow-editing.md
│   ├── workflow-consistency.md
│   ├── workflow-product.md
│   └── workflow-typography.md
└── scripts/
    ├── install.sh
    └── validate.py
```

## Install — Claude Code

Project-scoped skills live under `.claude/skills/<name>/SKILL.md`.

From this package directory:

```bash
./scripts/install.sh claude /path/to/your/project
```

Or copy the folder manually to:

```text
YOUR_PROJECT/.claude/skills/image-prompt-optimizer/
```

Then start Claude Code in that project. The skill can be invoked explicitly as `/image-prompt-optimizer` and may also activate automatically when the request matches its description.

## Install — Codex

### User-wide

```bash
./scripts/install.sh codex-user
```

This installs to:

```text
~/.agents/skills/image-prompt-optimizer/
```

### Project-scoped

```bash
./scripts/install.sh codex-project /path/to/your/project
```

This installs to:

```text
YOUR_PROJECT/.agents/skills/image-prompt-optimizer/
```

Codex can invoke the skill explicitly through its skills UI/mention flow and may also activate it implicitly from the description.

## Install — Hermes Agent

```bash
./scripts/install.sh hermes
```

This installs to:

```text
~/.hermes/skills/creative/image-prompt-optimizer/
```

Start a new Hermes session, or refresh skill discovery according to your Hermes version. The skill is available as a slash-command-style skill and can also be selected automatically.

## Validate

```bash
python3 scripts/validate.py
```

The validation script checks the Agent Skills naming/frontmatter basics, SKILL.md length, and referenced files.

## Example usage

### Generic

```text
优化成生图提示词：
一个女生在东京深夜便利店门口吃冰淇淋，安静、有点疏离，真实摄影，不要赛博朋克。
```

### Model-specific

```text
/image-prompt-optimizer
目标模型：Midjourney
把这个概念优化成 16:9 的电影剧照感提示词：
雨夜东京，一个人撑透明伞走过小巷，克制、写实，不要过度霓虹。
```

### Image edit

```text
Use the image-prompt-optimizer skill.
把参考图的白天背景改成雨夜。人物的脸、衣服、姿势、构图完全不变。
目标模型：GPT Image
```

### Multi-model

```text
把同一个产品广告 brief 分别编译成 GPT Image、Midjourney 和 FLUX 三个版本。
```

## Design choices

The main `SKILL.md` is intentionally compact. Detailed visual vocabulary, model dialects, workflows, and examples live in `references/` and are loaded only when needed. This follows progressive-disclosure principles and keeps routine invocations efficient.

Model-specific files avoid hard-coding volatile version numbers when not required. Update one adapter when a platform changes rather than rewriting the whole skill.
