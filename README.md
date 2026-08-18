# Prompt Optimizer

一个面向多模态参考素材的 Agent Skill：分析参考图、参考视频、音频、脚本、文案或粗略创意，并转换为可直接使用的图像 / 视频生成提示词。

支持模型：

- GPT Image
- Seedream 5.0
- Seedance 2.0

## 能做什么

- 为每份参考素材分配清晰角色，例如主体、构图、风格、动作、运镜、节奏或声音；
- 从参考图提取身份、产品、空间、光影、材质和版式锚点；
- 按时间分析参考视频的动作链、镜头轨迹、剪辑节奏和声音事件；
- 完成图 → 图、图 → 视频、视频 → 图、视频 → 视频以及脚本 / 文案 → 图或视频的跨模态转换；
- 为图片或视频编辑明确 Change / Preserve / Integration / Constraints；
- 根据 GPT Image、Seedream 5.0 和 Seedance 2.0 的差异编译专用 Prompt。

这个 Skill 默认只输出提示词，不直接生成或编辑媒体。

## 结构

```text
prompt-optimizer/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── reference-analysis.md
│   ├── visual-language.md
│   ├── model-gpt-image.md
│   ├── model-seedream-5.md
│   ├── model-seedance-2.md
│   ├── evaluation.md
│   └── examples.md
└── scripts/
    ├── install.sh
    └── validate.py
```

## 安装

### Claude Code 项目级

```bash
./scripts/install.sh claude /path/to/project
```

### Codex 用户级

```bash
./scripts/install.sh codex-user
```

### Codex 项目级

```bash
./scripts/install.sh codex-project /path/to/project
```

### Hermes 用户级

```bash
./scripts/install.sh hermes
```

安装器不会覆盖已存在的 Skill 目录。

## 校验

```bash
python3 scripts/validate.py
```

校验脚本只依赖 Python 标准库，检查 frontmatter、文件引用、过时模型名称和基础结构。

## 示例

```text
使用 $prompt-optimizer。
图 1 参考人物，图 2 参考服装，视频 1 只参考动作与运镜。
生成一段 10 秒雨夜天台写实短片，目标模型 Seedance 2.0。
```

```text
使用 $prompt-optimizer，把这段参考视频里最有冲击力的瞬间转换成 GPT Image 海报主视觉提示词，不要文字。
```
