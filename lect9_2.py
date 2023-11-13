"""from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://table.cafe.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')
item = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong")
print(item)
print(item.get_text())

wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")
print(wt)
print(wt.get_text())

goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
print(goods)
print(goods.get_text())

iss = res_html.select("a.wrap_thumb")
print(iss)

print("\n---------------------------------\n")
ct = res_html.select("a.wrap_thumb")
for j in ct :
    c = j.attrs["data-tiara-id"]
    print(c+"\n")
"""
"""
# 이미지 저장

from bs4 import BeautifulSoup as bs
import requests as rq
import os
from urllib.request import urlretrieve as rl

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

imgs = res_html.select("img")
print(imgs)

linkimgs = []

for i in imgs:
    irs = i.attrs["src"]
    linkimgs.append(irs)
    
folder = "imgs/"
if not os.path.isdir(folder):
    os.mkdir(folder)
    
i = 0
for ln in linkimgs:
    if  str(ln).find("//t") == False :
        print(ln)
        continue
    else:
        pass
    
    i += 1
    rl(ln, folder + f"{i}.jpg")
"""

# Pandas 전처리
# 시리즈 생성

"""from pandas import Series as sr

data = [10, 20,30, 40]
sdata = sr(data)

print(sdata)

import numpy as np"""

"""data = np.arange(1, 5)
sdata = sr(data)

sdata = sr(data)

print(sdata.index)

print(sdata.index.to_list())
print("\n===========================\n")
sdata.index = ["a", "b", "c", "d"]
print(sdata)"""

"""
dt = [10, 20,30, 40]
idx = ["a", "b", "c", "d"]

sdata = sr(data=dt, index=idx)
print(sdata)

sd = sdata.reindex({"a","j","c"})
print(sd)

sd = sdata.reindex({"b"})
print(sd)
print("\n------------------------\n")
print(sdata["b"])
print("\n------------------------\n")

print(sdata.iloc[0])
print(sdata.iloc[2])
# print(sdata[0]) 오류 발생
"""

from pandas import Series as sr

"""dt = ["alpha","beta","charlie","delta"]
idx = ["ab","bc","cd","de"]

sdata =sr(data=dt,index=idx)

print(sdata.iloc[1:2])
print("\n------------------------------\n")
print(sdata.iloc[2:])
print("\n------------------------------\n")
print(sdata.iloc[:2])
print("\n------------------------------\n")

"""
"""dt = ["alpha","beta","charlie","delta"]
idx = ["ab","bc","cd","de"]

sdata = sr(data=dt, index=idx)

sdata.loc["cd"] = "echo"
print(sdata)

print("\n------------------------------\n")
sdata.iloc[1] = "fox"
print(sdata)

# 수정/추가/삭제

# 추가
sdata.loc["ef"] = "golf"

# 삭제
print("\n------------------------------\n")
print(sdata.drop("bc"))
print("\n------------------------------\n")"""

"""s1 = sr([100, 200, 300], index=["a", "b", "c"])
s2 = sr([100, 200, 300], index=["b", "c", "a"])

sum_res = s1 + s2
print(sum_res)
print(sum_res.max())
print(sum_res.mean())
print(sum_res.min())
print("\n------------------------------\n")


sub_res = s1 - s2
print(sub_res)
print(sub_res.max())
print(sub_res.mean())
print(sub_res.min())
print("\n------------------------------\n")

mul_res = s1 * s2
print(mul_res)
print(mul_res.max())
print(mul_res.mean())
print(mul_res.min())
print("\n------------------------------\n")

div_res = s1 / s2
print(div_res)
print(div_res.max())
print(div_res.mean())
print(div_res.min())
print("\n------------------------------\n")

# 연산

data = {
    "삼성전자": "전기,전자",
    "LG전자": "전기,전자",
    "현대차": "운수장비",
    "NAVER": "서비스업",
    "카카오": "서비스업"
}

sdata = sr(data)
uniq = sdata.unique()
print(uniq)

# sc = sdata.count()

# sv = sdata.value_counts()
"""

# 필터링

idx = ["a", "b", "c", "d", "e"]
s1 = sr([1100, 270, 30, 450, 50], index=idx)
s2 = sr([150, 740, 810, 40, 25], index=idx)

# 시리즈내 데이터 비
fil = s1 > 300
print(fil)

# 시리즈간 비교
# fil1 = s2 > s1

# 인덱싱 출력
# s2[s2 > s1].index

sv = s1.sort_values()
print(sv)

print("\n------------------------------\n")

sv1 = s1.sort_values(ascending=False)
print(sv1)


