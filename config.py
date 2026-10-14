SITE = dict(mode="apps", title="CoolApps Hub · 每日有趣新产品", wordmark="Cool<b>Apps</b>", tagline="每天发现好玩的新产品",
  url="https://chunxiaostudy.github.io/CoolApps-Hub/", repo="https://github.com/ChunXiaostudy/CoolApps-Hub", disclaimer="内容由程序自动抓取并经 LLM 摘要，信息以官方页面为准。")
SECTIONS = ["AI 原生应用", "效率工具", "硬件与设备", "消费与生活", "开发者工具", "独立开发/小而美"]
SOURCES = [
 dict(name="Product Hunt", url="https://www.producthunt.com/feed", limit=40),
 dict(name="Show HN", url="https://hnrss.org/show?points=30", limit=30),
 dict(name="GitHub", kind="github", q="stars:>50", days=7, limit=20),
 dict(name="BetaList", url="https://feeds.feedburner.com/BetaList", limit=25),
 dict(name="少数派", url="https://sspai.com/feed", limit=20),
 dict(name="The Verge", url="https://www.theverge.com/rss/index.xml", keywords=["launch","launches","app","gadget","device","announces","new"], limit=30),
 dict(name="Google News · 新产品", title_only=True, url="https://news.google.com/rss/search?q=%E6%96%B0%E4%BA%A7%E5%93%81+%E5%8F%91%E5%B8%83+App+when:2d&hl=zh-CN&gl=CN&ceid=CN:zh-Hans", limit=15),
]
PROMPT = """你是轻松有趣的新产品编辑。根据给定条目（仅依据其中信息）生成中文介绍，语气轻快但不夸张，必须点出亮点。
规则：只陈述来源中的事实，绝不编造数字、价格、用户量；不确定的字段留空字符串或空数组。
若条目不是一个具体的产品/应用/工具/硬件/开源项目（例如纯新闻评论、融资八卦、招聘），keep=false。"""
FIELDS = """keep(bool), name(产品名), summary(一句话介绍,≤80字), why(有意思在哪,≤30字), audience(目标用户,≤15字), section(从可选section选一), tags(从可选 tags 中选 1-3 个), platform(平台数组, 如 Web/iOS/Android/Mac/Windows/CLI/硬件, 不确定则空), pricing(免费/订阅/开源/付费/未知 之一), score(1-10 有趣程度整数)"""

SECTION_SLUGS = ["ai-native", "productivity", "hardware", "lifestyle", "developer", "indie"]
TAGS = ["AI Agent", "AI 编程", "AI 创作", "本地 AI", "开源", "隐私安全", "笔记知识", "写作", "设计", "音频音乐", "视频", "图像", "搜索", "浏览器",
        "生产力", "日程时间", "沟通协作", "开发运维", "数据与数据库", "终端 CLI", "金融记账", "健康运动", "学习教育", "游戏娱乐", "硬件", "智能家居", "出行", "购物", "社交"]
TAG_SYNONYMS = {"Agent": "AI Agent", "Agent Skill": "AI Agent", "MCP": "AI Agent", "AI编程": "AI 编程", "代码评审": "AI 编程", "AI视频": "视频", "短视频": "视频",
  "本地AI": "本地 AI", "隐私": "隐私安全", "安全": "隐私安全", "音乐": "音频音乐", "音频分离": "音频音乐", "播客": "音频音乐", "TTS": "音频音乐", "DAW": "音频音乐",
  "记谱法": "音频音乐", "转录": "音频音乐", "有声书": "音频音乐", "插画": "设计", "SVG": "设计", "CAD": "设计", "本地搜索": "搜索", "运维": "开发运维", "监控": "开发运维",
  "发布管理": "开发运维", "代码质量": "开发运维", "TUI": "终端 CLI", "CLI": "终端 CLI", "记账": "金融记账", "支付": "金融记账", "稳定币": "金融记账", "专注": "生产力",
  "目标管理": "生产力", "日历": "日程时间", "协作": "沟通协作", "会议": "沟通协作", "内容创作": "AI 创作", "笔记": "笔记知识", "知识管理": "笔记知识", "游戏": "游戏娱乐", "健身": "健康运动"}
SOURCE_WEIGHTS = {"Product Hunt": 2.0, "Show HN": 2.0, "GitHub": 1.5, "BetaList": 1.0, "少数派": 1.5, "The Verge": 1.0, "Google News · 新产品": 0.5}
