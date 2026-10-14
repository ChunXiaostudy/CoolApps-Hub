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
 dict(name="Google News · 新产品", url="https://news.google.com/rss/search?q=%E6%96%B0%E4%BA%A7%E5%93%81+%E5%8F%91%E5%B8%83+App+when:2d&hl=zh-CN&gl=CN&ceid=CN:zh-Hans", limit=15),
]
PROMPT = """你是轻松有趣的新产品编辑。根据给定条目（仅依据其中信息）生成中文介绍，语气轻快但不夸张，必须点出亮点。
规则：只陈述来源中的事实，绝不编造数字、价格、用户量；不确定的字段留空字符串或空数组。
若条目不是一个具体的产品/应用/工具/硬件/开源项目（例如纯新闻评论、融资八卦、招聘），keep=false。"""
FIELDS = """keep(bool), name(产品名), summary(一句话介绍,≤80字), why(有意思在哪,≤30字), audience(目标用户,≤15字), section(从可选section选一), tags(分类标签数组≤3), platform(平台数组, 如 Web/iOS/Android/Mac/Windows/CLI/硬件, 不确定则空), pricing(免费/订阅/开源/付费/未知 之一), score(1-10 有趣程度整数)"""
