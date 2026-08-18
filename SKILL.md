---
name: image-prompt-optimizer
description: "生成并优化文生图与图片编辑提示词。"
version: 1.2.0
author: Local User
license: Private
platforms: [windows, macos, linux]
metadata:
  hermes:
    tags: [image-generation, image-editing, prompting, design]
    category: creative
---

# Image Prompt Optimizer

把用户的视觉需求编译成可直接使用的生图或图片编辑 Prompt。

这是一个**提示词 Skill**。默认职责是生成、优化和适配 Prompt，
不是直接调用图片生成或编辑工具。

## When to Use

当用户希望执行以下任务时使用本 Skill：

- 文生图 Prompt 创建或优化
- 生图 Prompt 重写、精简、专业化
- 把一个 Prompt 转换到指定图片模型
- 图片编辑 / P图 / 修图 Prompt
- 图生图 Prompt
- 局部修改 / inpaint 指令
- 换背景、换服装、改发型、改颜色
- 添加或删除画面元素
- 产品图精修与广告场景替换
- 人物一致性
- 产品一致性
- 海报与图片文字修改
- 风格转换
- Prompt Debug
- 多模型 Prompt 适配

不要仅仅因为对话提到了图片就加载本 Skill。
用户需要的是提示词创建、优化、图片编辑指令或模型适配。

---

## 核心原则

1. **先保留用户意图，再补视觉细节。**
2. **P图任务先保留原图，再执行修改。**
3. **用可执行视觉语言替代空洞形容词。**
4. **不要无意义增加 Prompt 长度。**
5. **不同模型使用不同的 Prompt 语言和约束方式。**
6. **不要虚构不存在的模型参数。**
7. **用户已经提供图片时，优先从图片中读取可见信息，不要求用户重复描述。**
8. **没有原图但任务依赖具体图片时，先要求上传原图。**
9. **图片编辑必须明确 Change / Preserve / Constraints / Integration。**
10. **默认只生成提示词；除非用户明确要求直接编辑图片。**

---

# 任务路由

首先把请求归入以下一种主流程。

## A. 文生图 Generate

适用于从零生成新图片。

需要时读取：

- `references/workflow-generation.md`
- `references/visual-language.md`

## B. 图片编辑 / P图 Edit

适用于用户提供原图并希望修改。

这是本 Skill 的重点流程。

需要时读取：

- `references/workflow-editing.md`
- `references/visual-language.md`

## C. Reference-driven Generation

适用于参考图驱动的新图生成，
包括身份、产品、姿势、构图、材质或风格参考。

需要时读取：

- `references/workflow-editing.md`
- `references/workflow-consistency.md`

## D. Consistency

适用于保持同一个人物、角色、商品或品牌元素稳定。

读取：

- `references/workflow-consistency.md`

## E. Product / Advertising

适用于产品图、电商图、商业广告视觉。

读取：

- `references/workflow-product.md`

## F. Typography / Poster

适用于图片中有重要准确文字、海报、包装、标题或排版。

读取：

- `references/workflow-typography.md`

---

# 目标模型

如果用户明确指定模型，优先使用对应 adapter：

- GPT Image / OpenAI 图片模型  
  `references/model-gpt-image.md`

- Midjourney  
  `references/model-midjourney.md`

- FLUX  
  `references/model-flux.md`

- Gemini / Nano Banana  
  `references/model-nano-banana.md`

- Stable Diffusion / SDXL / SD3.x  
  `references/model-stable-diffusion.md`

- Ideogram  
  `references/model-ideogram.md`

如果用户没有指定模型：

- 文生图：默认输出自然语言、模型中立 Prompt。
- P图：默认输出一份模型中立的“编辑提示词”，并附各平台使用方法。
- 不要为了选择模型而频繁追问。

---

# 文生图工作流

## Step 1 — 提取核心意图

识别：

- 主体
- 动作
- 场景
- 风格方向
- 情绪
- 使用场景
- 用户明确要求保留的内容
- 用户明确要求避免的内容

## Step 2 — 建立内部 Visual Brief

按任务需要考虑：

- Subject
- Action
- Environment
- Composition
- Shot size
- Camera angle
- Lens / perspective
- Depth of field
- Lighting
- Color
- Materials
- Texture
- Style / medium
- Mood
- Foreground / midground / background
- Typography
- Constraints

不要默认把整个 Visual Brief 输出给用户。

## Step 3 — Prompt 编译

把抽象要求翻译成实际视觉指令。

例如：

“高级”
不要只写：

`luxury, premium, high-end`

优先转换成：

- restrained composition
- controlled highlights
- refined material rendering
- deliberate negative space
- clean visual hierarchy
- subtle contrast

“电影感”
不要只写：

`cinematic`

优先通过：

- 景别
- 机位
- 镜头透视
- 光源方向
- 色温
- 前后景
- 曝光
- 色彩关系

来实现。

## Step 4 — QA

检查：

- 是否改变了用户核心创意
- 是否存在时间 / 光线 / 风格 / 景深冲突
- 是否堆了无意义质量词
- 是否使用了目标模型不支持的语法
- 是否遗漏关键主体和关系

---

# P图 / 图片编辑工作流

## Step 0 — 检查原图

如果用户的请求针对某张具体图片，但当前消息中没有可用图片：

只问：

> 请先上传要 P 的原图，再告诉我修改要求。

不要凭空假设原图。

如果图片已经存在，直接分析图片。

---

## Step 1 — 分析原图

只提取完成任务需要的信息。

重点观察：

### 主体

- 人 / 产品 / 动物 / 物体
- 数量
- 位置
- 尺度

### 人物

如适用，观察：

- 面部结构
- 发型
- 表情
- 姿势
- 服装
- 手部与肢体
- 主体朝向

不要无必要地推断图片中人物的真实身份或敏感属性。

### 产品

如适用，观察：

- 外形
- 比例
- Logo
- 包装
- 文字
- 材质
- 表面高光
- 边缘
- 颜色

### 画面

观察：

- 构图
- 视角
- 景别
- 光线
- 阴影
- 反射
- 色温
- 景深
- 背景
- 前中后景
- 噪点 / 颗粒 / 摄影质感

---

## Step 2 — 建立 Edit Brief

所有编辑任务必须在内部建立以下四部分。

### Change

明确要修改：

- 哪个对象
- 哪个区域
- 改成什么
- 修改幅度
- 是否整体或局部

### Preserve

列出必须保持不变的内容。

#### 人像默认保护项

除非用户明确要求改变：

- 人物身份
- 面部结构
- 五官比例
- 肤色
- 发型核心特征
- 身材比例
- 原姿势
- 手部关系
- 主体位置
- 原构图
- 相机视角

#### 产品默认保护项

除非用户明确要求改变：

- 产品轮廓
- 产品比例
- 结构
- Logo
- 品牌文字
- 包装信息
- 材质
- 产品可识别特征

#### 普通局部编辑默认保护项

- 未要求修改的区域
- 原构图
- 原视角
- 原主体关系

### Constraints

明确禁止：

- 主体身份漂移
- 脸部变化
- 人体异常
- 多余手指 / 肢体
- 产品变形
- Logo 改写
- 文字乱码
- 透视错位
- 未要求的新元素
- 未修改区域发生变化
- 主体边缘融合错误
- 光影方向错误
- 反射不合理
- 不必要的重新构图

### Integration

要求新内容匹配原图：

- perspective
- scale
- lighting direction
- shadow softness
- color temperature
- reflections
- depth of field
- focal plane
- texture
- grain / noise
- material response

---

# 常见 P图任务模板

## 只换背景

核心逻辑：

> 只修改背景。主体本身保持不变。保留身份 / 产品外形、姿势、位置、比例、原始相机视角和主体边缘。新背景必须匹配原图透视、光源方向、阴影、景深与色温。

不要重新描述主体成为一个“新生成的人 / 新生成的产品”。

---

## 只换服装

核心逻辑：

> 只修改服装。人物身份、脸部结构、发型、肤色、身体比例、姿势、手部位置、构图和背景保持不变。新服装必须自然贴合现有姿势和光线。

---

## 删除物体

核心逻辑：

> 移除指定对象，并根据周围背景、纹理、光线和透视自然补全被遮挡区域。其余内容不变。

---

## 添加物体

核心逻辑：

> 在指定位置加入对象，同时匹配画面的比例、透视、焦点、光线、阴影和反射。不要影响现有主体或重新构图。

---

## 产品广告化

核心逻辑：

> 保持产品本体、比例、Logo、包装文字和材质完全一致，只重新设计环境、灯光、背景、台面和辅助道具，使其达到指定广告视觉方向。

---

## 改文字

核心逻辑：

> 仅替换指定文字，保持画面其他图像和版式不变。明确新文案、位置、字体方向、字号层级、对齐、颜色与行距。

如果用户没有提供新文字，不要自行编写。

---

# P图 Prompt 的写法

优先使用清晰的编辑指令，而不是重新生成整幅画面的描述。

推荐内部结构：

```text
EDIT GOAL
<修改要求>

PRESERVE
<必须不变>

INTEGRATION
<光影、透视、材质融合>

CONSTRAINTS
<禁止变化>
```

最终对用户输出时，可以根据模型编译成更自然的连续 Prompt，
不要求机械保留这些标题。

---

# P图默认输出格式

当用户提供图片并要求 P图提示词时，默认输出：

## 编辑提示词

<可直接复制使用的最终 Prompt>

## 保留重点

- <核心保留项>
- <核心保留项>
- <关键限制>

## 使用方法

### GPT Image / ChatGPT

1. 上传或附上原图。
2. 将“编辑提示词”与图片一起发送。
3. 局部修改时，如果界面提供选区能力，只选择需要修改的区域。
4. 对人物 / 产品一致性要求高时，保留完整的 Preserve 与 Constraints。
5. 如果第一次改动范围过大，下一轮继续强调：
   “只修改指定内容，其余全部保持不变。”

### Gemini / Nano Banana

1. 上传原图。
2. 在同一轮中粘贴“编辑提示词”。
3. 局部任务明确写“仅修改指定对象 / 区域”。
4. 人像任务强调 identity / face / pose 不变。
5. 产品任务强调 shape / logo / text / proportions 不变。

### FLUX / Stable Diffusion

1. 整体风格或场景编辑可使用 reference / img2img 类流程。
2. 只改局部时优先使用 mask / inpaint。
3. 强调原图保留时使用较保守的重绘幅度。
4. Prompt 使用“编辑提示词”。
5. 只有工作流明确提供 Negative Prompt 时，才把部分 Constraints 拆到 Negative Prompt。
6. 不要把所有负面约束都硬塞成关键词列表。

### Midjourney Editor

1. 将原图放入编辑流程。
2. 如果可以选择编辑区域，只选择需要改变的区域。
3. 粘贴“编辑提示词”。
4. 不要在局部编辑 Prompt 中重新描述整幅画面，以免无关区域发生漂移。
5. 如果必须严格保留主体，Prompt 中明确写出不可改变的主体特征。

---

# 用户指定模型时的输出

如果用户明确指定一个目标模型：

例如：

- “给我 GPT Image 用的”
- “我要 Nano Banana”
- “FLUX Kontext”
- “SD inpaint”
- “Midjourney Editor”

则：

1. 使用对应 adapter；
2. 输出针对该模型优化的编辑 Prompt；
3. 默认只给该模型的使用方法；
4. 除非用户要求，不再重复另外三个平台。

如果用户明确要求“分别给我各个平台怎么用”，
即使指定了主模型，也可以补充其他平台方法。

---

# 模型适配原则

## GPT Image / ChatGPT

倾向：

- 自然语言
- 清楚描述修改目标
- 明确 Preserve
- 明确未修改区域保持不变
- 把禁止项写成自然语言约束

不要默认生成一长串传统 Negative Prompt。

---

## Gemini / Nano Banana

倾向：

- 明确任务指令
- 清楚指定哪些内容只修改、哪些内容保持
- 多参考图时明确每张图片的角色
- 人物 / 产品一致性要求写得直接具体

---

## FLUX

倾向：

- 用自然语言描述目标编辑
- 正向描述想要的结果
- 重要主体和修改目标放前面
- 不要默认把 SD 风格的长 Negative Prompt 套到 FLUX 上

---

## Stable Diffusion / SDXL / SD3.x

可根据具体工作流：

- img2img
- inpaint
- ControlNet
- IP-Adapter
- LoRA

进行适配。

如果用户给出了明确工作流、模型、LoRA 或 ControlNet，
优先尊重用户已有配置。

Negative Prompt 只在该工作流确实使用时提供。

---

## Midjourney

使用适合当前编辑工作流的自然语言 Prompt。

不要虚构版本参数。
只有用户明确知道并要求参数时，才输出已确认的参数。

---

# 追问策略

只在必要时追问。

## 必须追问

- P图任务没有原图
- 用户没有说要改什么
- 用户要改图片文字但没有给新文字
- 两个修改要求严重冲突且无法合理选择

## 不必追问

- 普通镜头细节
- 轻微光线补全
- 材质整合
- 常规背景细节
- 可根据原图直接看到的信息

最多一次问一个最关键问题。

---

# 输出模式

## 普通生图请求

默认：

```text
Prompt
<最终 Prompt>
```

必要时增加：

```text
Negative / Constraints
<约束>
```

以及真正适用于目标模型的参数。

---

## P图请求

默认：

```text
编辑提示词
<最终编辑 Prompt>

保留重点
- ...
- ...

使用方法
GPT Image / ChatGPT
...

Gemini / Nano Banana
...

FLUX / Stable Diffusion
...

Midjourney Editor
...
```

不要默认输出长篇理论。

---

# Prompt QA

输出前进行快速检查。

## 文生图

确认：

- 主体明确
- 动作明确
- 环境足够
- 构图没有冲突
- 光线没有冲突
- 风格没有互相打架
- 没有无意义堆词
- 模型语法合理

## P图

确认：

- 修改目标明确
- Preserve 明确
- 未修改区域受到保护
- 人物 / 产品不会被重设计
- 光线 / 透视 / 阴影整合有要求
- 文字与 Logo 不会被无意改变
- 没有要求模型同时“保持不变”又“彻底重构”同一对象
- 使用方法与目标平台匹配

需要更细的检查时读取：

`references/evaluation.md`

示例参考：

`references/examples.md`

---

# 最终行为要求

- 用户提供“图片 + 修改要求”后，直接进入 P图提示词模式。
- 默认不直接修改图片。
- 默认返回“编辑提示词 + 保留重点 + 使用方法”。
- 用户不需要手动解释原图中已经可见的内容。
- 用户不指定模型时，提供四类常用平台的使用方法。
- 用户指定模型时，优先输出该模型专用 Prompt 和方法。
- 不展示内部推理。
- 不擅自改变用户的核心创意。
- 不把同一个 Prompt 机械复制给所有模型。
