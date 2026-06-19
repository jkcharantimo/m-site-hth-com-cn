def load_site_data():
    """返回内置站点资料列表"""
    return [
        {
            "title": "华体会体育",
            "url": "https://m-site-hth.com.cn",
            "keywords": ["华体会", "体育", "赛事", "投注"],
            "tags": ["体育", "在线娱乐", "实时比分"],
            "description": "华体会体育平台提供丰富的体育赛事和投注服务，涵盖足球、篮球、网球等多个热门项目。"
        },
        {
            "title": "华体会电竞",
            "url": "https://m-site-hth.com.cn/esports",
            "keywords": ["华体会", "电竞", "比赛", "战队"],
            "tags": ["电竞", "游戏", "直播"],
            "description": "华体会电竞板块汇聚全球电竞赛事，支持实时观看与互动竞猜。"
        },
        {
            "title": "华体会娱乐",
            "url": "https://m-site-hth.com.cn/casino",
            "keywords": ["华体会", "娱乐", "棋牌", "老虎机"],
            "tags": ["棋牌", "娱乐城", "老虎机"],
            "description": "华体会娱乐平台提供多种经典棋牌和老虎机游戏，体验极致乐趣。"
        }
    ]


def format_site_summary(site):
    """格式化单个站点摘要"""
    kw_str = "、".join(site["keywords"])
    tag_str = "、".join(site["tags"])
    lines = [
        f"站点名称：{site['title']}",
        f"访问地址：{site['url']}",
        f"核心关键词：{kw_str}",
        f"所属标签：{tag_str}",
        f"简短说明：{site['description']}",
        "---"
    ]
    return "\n".join(lines)


def generate_structured_summary(sites):
    """生成完整结构化摘要"""
    header = "===== 站点资料结构化摘要 =====\n"
    separator = "==============================\n"
    body_parts = [format_site_summary(s) for s in sites]
    body = "\n".join(body_parts)
    count = len(sites)
    footer = f"共 {count} 个站点条目，数据截止于最新版本。"
    return header + body + separator + footer


def display_summary():
    """输出摘要到控制台"""
    data = load_site_data()
    summary = generate_structured_summary(data)
    print(summary)


def write_summary_to_file(filepath="site_summary_output.txt"):
    """将摘要写入文本文件"""
    data = load_site_data()
    summary = generate_structured_summary(data)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"摘要已写入文件：{filepath}")


def main():
    """主入口"""
    display_summary()
    # 如需写入文件可取消下面注释
    # write_summary_to_file()


if __name__ == "__main__":
    main()