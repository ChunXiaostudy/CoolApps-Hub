# CoolApps-Hub

每日有趣新产品：AI 原生应用、效率工具、硬件、消费生活、开发者工具、独立开发。

- 网站: https://chunxiaostudy.github.io/CoolApps-Hub/
- 每日 07:30（北京时间）由 GitHub Actions 自动抓取 → LLM 中文摘要/分类/打分 → 构建静态站 → 发布到 GitHub Pages。
- 数据源见 `config.py`，历史数据保存在 `data/items.json`（保留 30 天）。

## 运行
```
pip install feedparser
LLM_API_KEY=... LLM_BASE_URL=... python hub.py   # 输出到 site/
```
Secrets: `LLM_API_KEY`, `LLM_BASE_URL`；可选变量 `LLM_MODEL`（默认 deepseek-v4-flash）。

## 致谢
思路参考 [wuyoscar/AISafetyHot-Hub](https://github.com/wuyoscar/AISafetyHot-Hub)（内容 CC BY-NC 4.0）与 [KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT)（MIT）。本仓库代码为独立重写，未复制其内容。条目版权归原始来源所有。

代码以 MIT 许可发布。
