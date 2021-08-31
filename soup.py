"""
    --掲示板の最新投稿１０件を表示する--
    >手軽に報酬最低ライン情報を取得できると便利だと思ったから
    >API探しした中で自分がやりたいことと一致するものが探し
     きれず、WEBスクレイピングに
"""

import requests
from bs4 import BeautifulSoup

# サイト取り込み
url = "https://gamewith.jp/kuronekowiz/bbs/threads/show/118#bbs-form"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")


# ユーザー名のみ表示
users = [user.get_text() for user in soup.select("#bbs-posts span.bbs-post-user-name")]


# 投稿内容のみ表示
text = [user.get_text() for user in soup.select("#bbs-posts p.bbs-post-body")]


# 投稿者名と投稿内容を関連させる
matrix = list(zip(users, text))


# 掲示板タイトルと投稿内容を出力
print("---魔道杯ボーダー/ポイント/順位報告掲示板---", end="\n\n")

for bbs in matrix[:10]:
    name, text = bbs
    print("-" * 25)
    print(name)
    print("-" * 25)
    print(text.strip(), end="\n\n\n")
