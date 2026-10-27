"""
Campus Radar 配置文件
修改这里的配置来定制你的秋招监控。
"""

# ==================== 监控公司开关 ====================
# 把不想监控的公司设为 False 即可
ENABLED_COMPANIES = {
    "京东": True,
    "快手": True,
    "小红书": True,
    "拼多多": True,
    "淘宝": True,
    "offerstar": True,   # 聚合平台，补充行业动态
}

# ==================== 岗位关键词 ====================
# 简报会优先按"职位类别"过滤，再用关键词对岗位标题做兜底匹配
# 想加方向直接往里加关键词即可
KEYWORDS = {
    "电商": [
        "采销", "采销管培", "商家运营", "行业运营", "品类运营",
        "电商运营", "商品运营", "店铺运营", "平台运营", "招商",
        "供应链", "采购", "贸易", "跨境", "电商", "商家拓展",
        "行业BD", "商业化", "渠道运营", "分销",
    ],
    "产品": [
        "产品经理", "产品策划", "产品助理", "产品实习生",
        "数据产品", "商业化产品", "策略产品", "产品运营",
        "用户产品", "平台产品", "B端产品", "C端产品",
    ],
    "运营": [
        "用户运营", "内容运营", "活动运营", "社群运营",
        "新媒体运营", "社区运营", "增长运营",
        "海外运营", "国际化运营", "直播运营",
        "APP运营",
    ],
    "数据分析": [
        "数据分析", "业务分析", "用户分析", "用户行为分析", "用户研究",
        "增长分析", "产品分析", "营销分析", "销售分析", "流量分析",
        "交易分析", "客户分析", "数据洞察", "数据策略", "统计分析",
        "商业智能", "BI分析", "BI 分析", "BI Analyst",
        "Data Analyst", "Data Analysis", "Data Analytics", "Business Intelligence",
    ],
    "数据运营": [
        "数据运营", "运营分析", "运营数据分析", "数据化运营", "数字化运营",
        "经营运营", "业务运营", "策略运营", "增长策略", "增长运营",
        "用户增长", "用户策略", "精细化运营", "数据驱动运营",
        "Data Operations", "Operations Analyst", "Operations Analytics",
    ],
    "商业分析": [
        "商业分析", "商务分析", "经营分析", "经营数据分析", "经营管理",
        "经营计划", "经营策略", "战略分析", "策略分析", "战略研究",
        "行业研究", "市场研究", "市场分析", "竞争分析", "商业洞察",
        "商业策略", "商业规划", "商业化分析", "业务规划", "业务策略",
        "Business Analyst", "Business Analysis", "Business Analytics",
        "Strategy Analyst", "Strategic Analyst", "Market Analyst",
    ],
}

# 命中关键词的类别名（各公司 API 返回的类别字段里，含这些字就算命中）
CATEGORY_KEYWORDS = [
    "产品", "运营", "电商", "采销", "商家", "行业",
    "数据分析", "业务分析", "经营分析", "商业分析", "商务分析",
    "战略分析", "策略分析", "商业智能", "用户研究", "市场研究",
    "Data Analyst", "Data Analytics", "Business Analyst",
    "Business Analytics", "Business Intelligence",
]

# ==================== 目标城市 ====================
# 留空 [] 表示全国都看；填了就只看这些城市
# 注意：部分公司（如小红书）按城市过滤，填这里会精确过滤
TARGET_CITIES = ["上海", "北京", "杭州", "深圳", "广州"]

# ==================== 各公司专属参数 ====================
COMPANY_CONFIG = {
    "京东": {
        # 应届生招聘类型，type=present 表示应届生
        "type": "present",
    },
    "快手": {
        # 27届校招项目代码（从官网 URL 里提取）
        "recruit_sub_project_codes": ["20271779425607"],
    },
    "小红书": {
        # term_regular = 应届生校招
        "campus_recruit_types": ["term_regular"],
        # workplace 城市编码（4401=上海）。留空则不限城市
        "workplaces": [],  # [] = 全国
    },
    "拼多多": {
        # t=null 表示全部类别，也可填具体类别 job code
        "t": None,
    },
    "淘宝": {
        # batchId 会自动获取，这里留默认即可
        "batch_channel": "campus_group_official_site",
    },
    "offerstar": {
        # 聚合平台查询参数
        "title": "2027",
        # 分别查询各方向并合并去重，避免只搜索产品/运营而漏掉分析岗位
        "positions": ["产品", "运营", "电商", "数据分析", "数据运营",
                      "商业分析", "经营分析", "策略分析", "商业智能"],
        "channel": "校招",
    },
}

# ==================== 通用抓取源（零代码添加新公司）====================
# 后续添加新公司，只需在这里加一段配置即可，无需写代码！
# 配置格式见 scrapers/generic.py 文件顶部说明。
#
# 示例（取消注释并修改即可启用）：
#
# GENERIC_SOURCES = [
#     {
#         "name": "某公司",
#         "type": "api",                          # api 或 html
#         "url": "https://example.com/api/jobs",
#         "method": "POST",
#         "headers": {"Content-Type": "application/json"},
#         "body_template": {"page": "{page}", "size": 100},
#         "pagination": {"page_start": 1, "page_key": "page", "stop_when": "less_than_size"},
#         "response": {"list_path": "data.list", "total_path": "data.total"},
#         "fields": {
#             "job_id": "id", "title": "positionName", "category": "jobType",
#             "location": "workCity", "publish_time": "createTime",
#         },
#         "detail_url_template": "https://example.com/jobs/{job_id}",
#         "timestamp_field": "createTime",
#     },
# ]
GENERIC_SOURCES = []

# ==================== 运行参数 ====================
# 请求超时（秒）
REQUEST_TIMEOUT = 20
# 失败重试次数
MAX_RETRIES = 2
# 每页抓取条数（尽量大，减少翻页）
PAGE_SIZE = 100
# User-Agent
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
