# 邵艾伦操作系统（AI 薄肌版）

> 薄肌是身体版本答案，AI 是时代版本答案。

一个可安装的人物操作系统 Skill：以邵艾伦公开内容中“版本答案、薄肌、后天更新、先立观点再补教程”的表达与行动逻辑为底座，加入有来源的 AI 素养框架。

它不是邵艾伦本人，也不代表本人授权或认可。项目会明确区分：

- 邵艾伦公开表达；
- 基于真实模型做出的框架推断；
- “AI 薄肌版”的原创时代延伸。

## 它能做什么

- 判断 AI 时代的个人升级重点；
- 制定“身体在线 × 认知更新”的可持续计划；
- 诊断“收藏了很多 AI 工具，但没有真实产出”；
- 用“观点片 → 教程片”设计内容与个人 IP；
- 输出一本正经、带一点荒诞自嘲的幽默建议；
- 在健身、AI 与人物事实问题上主动标注证据边界。

## 安装

克隆仓库：

```bash
git clone https://github.com/XiaoSiKe/shao-alan-operating-system.git
```

复制 Skill 目录到 Codex：

```bash
cp -R shao-alan-operating-system/shao-alan-operating-system ~/.codex/skills/
```

或复制到支持 Agent Skills 的其他客户端对应 skills 目录。Skill 根目录是：

```text
shao-alan-operating-system/
├── SKILL.md
├── references/
├── scripts/
└── tests/
```

## 触发示例

- “用邵艾伦操作系统分析我现在该学什么。”
- “切换到 AI 薄肌版。”
- “我收藏了 100 个 AI 工具，算不算懂 AI？”
- “把这个个人成长计划薄肌化。”
- “给这个选题一个版本答案，再补教程片。”
- “别玩梗，认真告诉我这个方案的问题。”

## 设计原则

1. **先回答，再表演人设。**
2. **标题可以像教父，建议必须像教练。**
3. **每次一个主梗、一个回扣梗。**
4. **删掉笑点后，建议仍然成立。**
5. **项目原创绝不冒充本人观点。**

## 调研规模

调研截止 2026-09-09。仓库包含：

- 六维人物调研与一份 AI 时代参考；
- 111 个跨文件去重来源 URL；
- 4 支本人长视频的公开音轨/平台字幕分析；
- 33 个表达样本；
- 两支核心视频约 2,660 条弹幕与 410 条去重热门评论的传播分析；
- 2018—2026 公开时间线与正反观点。

所有动态数据只是调研日快照。完整证据位于 [`shao-alan-operating-system/references/research/`](shao-alan-operating-system/references/research/)。

## 测试

```bash
python3 shao-alan-operating-system/tests/test_skill.py
python3 shao-alan-operating-system/scripts/quality_check.py \
  shao-alan-operating-system/SKILL.md
```

行为测试题见 [`tests/PROMPTS.md`](shao-alan-operating-system/tests/PROMPTS.md)。

## 许可与免责声明

代码与原创 Skill 文本采用 MIT License。第三方视频、文章、人物姓名与平台内容归各自权利人所有；仓库只保存研究笔记、链接和有限必要分析，不重新分发原视频或完整版权内容。

本项目仅供教育、创作与思维实验，不构成医疗、营养、训练、财务或法律建议。
