from faker import Faker as fk
import os
import pandas as pd

temp = fk("ko-KR")
print(temp.name())


folder = "data/"

if not os.path.isdir(folder):
    os.mkdir(folder)
    
with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "w", newline='', encoding='utf8') as f :
    for i in range(30) :
        f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," )
            # temp.color_name() + "\n"


folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)

# print(df.name == "김병철")
# print(df.company == "박박정")

"""
# 비교 연산

res = df[df.postcode > 70000]["name","postcode"]
print(res)
print(res.count)

temp = df.postcode.mean()
temp = df.postcode.sum()
print(temp)
"""

# temp = df[df.color == "ivory"].postcode.mean()
# print(temp)

# temp = df[df.postcode > df.postcode.mean()]["name","postcode"]
# temp = df[df.postcode > df.postcode.mean()]
# print(temp)

# temp = df.company.isnull()
# for el in temp:
    # if el == True:
        # print(el)
        
# temp = df[df.company.isnull()]
# temp = df.company.empty
# print(temp)

"""
# 비트 연산
# Nor

temp = df[(df.color == "Ivory")]
res = df[~(df.color == "Ivory")] # 아이보리 아닌 애들 출력

print(temp.count)
# print(temp.color.count)
print(res)
"""

# and 연산
# temp = df[(df.color == "Ivory") & (df.postcode > 70000)]
# temp = df[(df.color == "Ivory") | (df.postcode > 70000)]
# temp = df[(df.color == "Ivory") | (df.postcode > 70000)]["name","postcode"]
# print(temp)

# 정렬

# temp = df.sort_values("postcode")
# temp = df.sort_values("postcode", ascending=False)
# temp = df.sort_values("name", ascending=False)
# temp = df.sort_values("name", ascending=True) # 오름차순
# print(temp)

# 데이터 재배열
# 특정 데이터 기준으로 긴 데이터 행렬을 피봇으로 재배열

col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]
df = pd.DataFrame(data=data, columns=col)
print(df)

print("\n----------------------------\n")
print(df.pivot(index="Machine", columns="Country", values="Price"))
print(df.pivot(index="Brand", columns="Machine", values="Price"))
print(df.pivot(index="Country", columns="Machine", values="Price"))
print(df.pivot(index="Price", columns="Brand", values="Machine"))