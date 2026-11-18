# 袁烨 · 作品集 2026

交互设计师（B 端）· 复杂信息架构与多角色界面 · 从研究到前端实现独立跑通。

线上地址：<https://ymataz.github.io/portfolio-2026/>

## 这本册子在讲什么

五个项目，按「最像工作」到「最像作业」排。每个项目先给背景、约束、我的角色，再给判断页——写的是「我以为 → 实际是 → 所以我改了 → 代价」。

| 页 | 项目 | 性质 |
|---|---|---|
| `work/kkh.html` | KKH 妇女儿童医院 · 多指标患者体验看板 | 真实机构项目 · 独立完成 |
| `work/eodd.html` | EODD · 可解释 AI 决策界面 | 团队研究 · 参与非主导 |
| `work/minimal-design.html` | minimal-design · 前端设计规则书 | 个人项目 · MIT 开源 |
| `work/digest.html` | AI 开源日报 · 端到端自动化 | 个人项目 · MIT 开源 |
| `work/chair.html` | 人宠共处公共座椅 · 形态概念 | 课程项目 · 小组 |

另有 16 页 A4 横版全册 PDF：`assets/portfolio-2026.pdf`（两版简历也在 `assets/`）。

## 技术

手写 HTML + CSS，没有框架、没有构建步骤、没有追踪脚本。

- 手写 HTML/CSS，无框架、无构建、无依赖
- 图片为 WebP，全部 `loading="lazy"`
- 响应式断点 1000px / 720px，移动端无横向溢出
- 遵循本站自建的 minimal-design 规则：每屏 ≤5 色、主色唯一、正文对比 ≥4.5:1、字重只用 400/600、标题上方不加 eyebrow、等分只用 12 栏、每页只有一个焦点动效（并遵守 `prefers-reduced-motion`）

字重说明：规则书原文写 400/500，本站改用 400/600——Windows 的微软雅黑没有 500 字面，500 会回落到 Regular，标题与正文将失去层级；600 在 macOS 与 Windows 两端都能落到真实 Bold。

## 本地跑

```bash
python -m http.server 8000
# 打开 http://127.0.0.1:8000/
```

## 口径

KKH 一律写「交付后进入院方内部对接流程」，不写已落地 / 已采纳 / 临床使用；EODD 写「团队项目，参与非主导」「投稿状态待确认」；界面内数字为示例值，结构与真实看板一致。

---

© 2026 袁烨 YUAN YE · Yachin.HCD@outlook.com
