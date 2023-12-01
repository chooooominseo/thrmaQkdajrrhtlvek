"""import pandas as pd

tr = pd.read_csv("data/train.csv")

print(tr)
print("\n-------------------------------\n")
# print(tr.head())

# res = tr.isnull.sum()
# print(res)

# 승선지
print("\n-------------------------------\n")
res = pd.crosstab(tr["Embarked"], tr["Survived"])
print(res)

# 컬럼 매핑
print("\n-------------------------------\n")
res.columns = res.columns.map({0:"Dead", 1:"Alive"})
print(res)

# 연령
print("\n-------------------------------\n")
res = pd.crosstab(tr["Age"], tr["Survived"])
print(res)

res.columns = res.columns.map({0:"Dead", 1:"Alive"})

# 승차 등급별 생존자
print("\n-------------------------------\n")
res = pd.crosstab(tr["Pclass"], tr["Survived"])
print(res)

# 성별 생존자
print("\n-------------------------------\n")
res = pd.crosstab(tr["Sex"], tr["Survived"])
print(res)

# 호칭 구분
print("\n-------------------------------\n")
tr["Title"] = tr.Name.str.extract(" ([A-Za-z]+)\.")
res = tr["Title"].value_counts()
print(res)

# tr["Title"] = tr["Title"].replace(["Capt", "Col", "Countess", "Don","Dona", "Dr", "Jonkheer", "Lady","Major", "Rev", "Sir"], "Other")
# tr["Title"] = tr["Title"].replace("Mlle", "Miss")
# tr["Title"] = tr["Title"].replace("Mme", "Mrs")
# tr["Title"] = tr["Title"].replace("Ms", "Miss")
tr["Title"].value_counts()

print(tr)

# age 별 Null 확인
print(tr["Age"].isnull()) #T/F
print(tr["Age"].isnull().sum)

meanAge = tr[["Title", "Age"]].groupby(["Title"]).mean()
print(meanAge)
# print(tr["Age"].head(20))

print("\n-------------------------------\n")

for index, row in meanAge.iterrows():
    nullIndex = tr[(tr.Title == index) & (tr.Age.isnull())].index
    # print(nullIndex, index, row[0])
    tr.loc[nullIndex, "Age"] = row[0]
    
print(tr)

print(tr["Age"].head(20))
# print(tr["Age"].isnull().sum())

tr["AgeCate"] = pd.qcut(tr.Age, 8, labels=range(1, 9))
print(tr.head())
# print(tr.dtypes)
print("\n-------------------------------\n")

tr.AgeCate = tr.AgeCate.astype(int)
print(tr.head())
print(tr.dtypes)

tr["CabinCate"] = tr["Cabin"].str.slice(start=0, stop=1)
print(tr["CabinCate"].value_counts())

# tr.Cabin.fillna("N", inplace=True)

#방번호 매핑
print("\n-------------------------------\n")
tr["CabinCate"] = tr["CabinCate"].map({ "N": 0, "C": 1, "B": 2, "D": 3, "E": 4, "A": 5, "F": 6, "G": 7, "T": 8 })
tr.CabinCate = tr.CabinCate.astype
print(tr)
print(tr.dtypes)
print(tr["CabinCate"].value_counts())

# 방번호별 생존자
print("\n-------------------------------\n")
res = pd.crosstab(tr["CabinCate"], tr["Survived"])
print(res)

# 요금컬럼 별 구간 구분
print("\n-------------------------------\n")
tr["FareCate"] = pd.qcut(tr.Fare, 8, labels=range(1, 9)) # 8등위
tr["FareCate"] = pd.qcut(tr.Fare, 5, labels=range(1, 6))
tr.FareCate = tr.FareCate.astype(int)
print(tr["FareCate"].value_counts())

res = pd.crosstab(tr["CabinCate"], tr["Survived"])
print(res)
"""

"""# 아이리스 전처리

import pandas as pd

df = pd.read_csv("./data/Iris.csv", index_col="Id")
print(df.head())


# 컬럼 매칭
df.rename(columns={
    "SepalLengthCm": "꽃받침길이",
    "SepalWidthCm": "꽃받침너비",
    "PetalLengthCm": "꽃잎길이",
    "PetalWidthCm": "꽃잎너비", 
    "Species": "품종"},
    inplace=True
)

print(df.head())

ir = df.rename(columns={
    "SepalLengthCm": "꽃받침길이",
    "SepalWidthCm": "꽃받침너비",
    "PetalLengthCm": "꽃잎길이",
    "PetalWidthCm": "꽃잎너비", 
    "Species": "품종"}
)

print(ir.head())
print("\n-------------------------------\n")

res = df.iloc[:, [0, 1, 4]]
print(res)


# df["품종"]= df["품종"].str[5:]
# print(df)

# ir["품종"]= ir["품종"].str[5:]
# print(df)

# res = df.groupby("품종").mean()
# print(res)

# res = df["품종"].value_counts()
# print(res)
"""

# 데이터 시각화

import matplotlib.pyplot as plt

# 기본 사용 y

value = [1, 2, 3, 4]
# value = [2, 4, 5, 7, 10]
res = plt.plot(value)
plt.show()

# 두 축 설정하기

x_value = [2, 3, 6, 7, 10 ]
y_value = [1, 4, 5, 8, 9]

plt.plot(x_value, y_value)