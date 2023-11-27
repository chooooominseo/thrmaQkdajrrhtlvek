# 변환
import pandas as pd

target = "data/apt.csv"

# df = pd.read_csv(target, encoding="CP949")
# print(df.head())

# df.to_csv("data/apt.csv", encoding="utf8")

df = pd.read_csv("data/apt.csv", index_col=0)

# 컬럼명 바꾸기

df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
# print(df)
# print(df.dtypes)

df["분양가"] = df["분양가"].convert_dtypes()
print(df.dtypes)
print("\n--------------------------\n")

# 정렬
# res = df.sort_values(by="지역명")[:5]
# print(res)

# res = df.sort_values(by="지역명")
# res = df.sort_values(by="지역명")
# res = df.sort_values(by="지역명", ascending=False)
# res = df.sort_values(by="지역명", ascending=True) #디폴트
# print(res.head()) # n개 출력

# res = df.sort_values(by="연도")
# res = df.sort_values(by="분양가")
# res = df.sort_values(by="연도")[:5]
# print(res)
# print(res.head())

# 컬럼이름 출력
# res = df[["지역명"]][:5]
# res = df[["지역명"]]
# res = df[:, ["지역명", "연도","분양가"]] -> error
# res = df[:, ["지역명", "연도","분양가"]][:7]
# res = df[["지역명", "연도"]][:5]
# print(res)

# print("\n--------------------------\n")
# res = df.loc[:, ["지역명", "연도","분양가"]][:7]
# print(res)

# res = df.loc[:][:5]
# res = df.loc[:][:] -> 처음부터 끝까지 출력
# print(res)
# res = df.loc[:6, ["지역명", "연도"]] 6까지 출력
# res = df.loc[6:, ["지역명", "연도"]] 6부터 출력

# res = df.iloc[1] - > 행번호 1번 출력
# # print(res)

# res = df.loc[:3, ["지역명", "연도"]][:8]
# print(res)

# 필터 출력
# res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]]
# 전체 data 출력됨
# res = df.loc[df["지역명"]=="강원"]
# res = df.loc[df["연도"] > 2020]
# res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][:16]
# res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][-10:] -> 끝에서부터 출력
# print(res)

# 인덱스 지정 선택
df0 = df.copy()
# print(df0) # 동일한 내용 copy

# print("\n--------------------------\n")
# res = df.iloc[2]
# res = df.iloc[2][2]
# print(res)

# 인덱스 필터
res = df[df.index > 3560] # 3561번부터 출력
print(res)

# 비트 연산 필터'
# res = df[df.연도 == 2023]
# res = df[df.월 == 3]
res = df[(df.연도 == 2023) & (df.지역명 == "서울") & (df.월 == 6)]
print(res)

# 컬럼 추가

columns = list(df.columns)
print(columns)

df1 = df.reindex(index=df.index[:7], columns=list(df.columns) + ["extra"])
# df1 = df.reindex(columns=list(df.columns) + ["extra"])
# print(df)
# print("\n--------------------------\n")
# print(df1)

print("\n--------------------------\n")
# df1.loc[:6, "extra"] = "0"
df1.loc[:4, "extra"] = False
print(df1)

# 복사
df2 = df1.copy()

# Nan 제거
# res = df2.dropna(how="any")
res = df2.fillna(value="text")
print(res)
res = df2.fillna(value="1234")
print(res)

# res = df2.dropna(how="any", inplace=True)
# print(df2)
print("\n--------------------------\n")



