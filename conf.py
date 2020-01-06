# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Blog-With-GitHub-Boilerplate/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "<hanna1122>/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "杳然拱廊中"
site_logo = "${static_prefix}fn logotype.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "Flaneur"
email = "18503044960@163.com"
author_homepage = "https://www.imalan.cn"
description = "吾本乘兴而起，兴尽而归，何必见戴。"
key_words = ['Flaneur', '杳然', '写字', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "写作值得",
        "url": "https://matters.news/@Han_nah",
        "brief": "在 Matters 写一些计划公开、期待回应的字。"
    },
    {
        "name": "语言失地",
        "url": "https://hannahtranslate.typlog.io/",
        "brief": "科学哲学设计译文集合。"
    }
]
nav = [
    {
        "name": "首页 HOME",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档 ARCHIVE",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于 ABOUT",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
