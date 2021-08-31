"""
    --掲示板の最新投稿１０件を表示する--
    >元のものから少し情報を追加
    >スクショURLも合わせたかったな…
"""
import requests
import re
from bs4 import BeautifulSoup

# サイト取り込み
url = "https://gamewith.jp/kuronekowiz/bbs/threads/show/118#bbs-form"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")


# ユーザー名のみ表示
users = [user.get_text() for user in soup.select("#bbs-posts span.bbs-post-user-name")]


# 投稿内容のみ表示
texts = [text.get_text() for text in soup.select("#bbs-posts p.bbs-post-body")]


# 投稿時間
times = [time.get_text() for time in soup.select("#bbs-posts span.bbs-posted-time")]


# 投稿No.
nums = [num.get_text() for num in soup.select("#bbs-posts span.bbs-post-number")]


# おまけ：スクショURL 報告が画像の人もいるため
soup = BeautifulSoup(res.text, "lxml")
img_url = [
    img["src"]
    for img in soup.find_all(
        "img", src=re.compile("^https://img.gamewith.jp/bbs/post/thumbnails/")
    )
]


# 投稿者名と投稿内容等を関連させる
matrix = list(zip(users, texts, times, nums))


# 内容を出力
print("---魔道杯ボーダー/ポイント/順位報告掲示板---", end="\n\n")

for bbs in matrix[:10]:
    (name, text, time, num) = bbs
    print(time)
    print("-" * 30)
    print(num, " ", name)
    print("-" * 30)
    print(text.strip(), end="\n\n\n\n")


# スクショURLまとめ
# for img in img_url:
#     print("URL", img)
