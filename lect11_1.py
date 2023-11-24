from faker import Faker as fk
import os
import pandas as pd

temp = fk("ko-KR")

folder = "data/"

with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
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
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n")

target = folder + "fktemp.csv"

df = pd.read_csv(target)

#rank 매기기
df["aver"] = df.postcode.rank(method="average")
print(df[["postcode","aver"]])

df["dense"] = df.postcode.rank(method="dense")
print(df[["postcode","dense"]])

df["first"] = df.postcode.rank(method="first")
print(df[["postcode","first"]])

df["min"] = df.postcode.rank(method="min")
print(df[["postcode","min"]])

df["max"] = df.postcode.rank(method="max", ascending=False)
df["max"] = df.postcode.rank(method="max")
print(df[["postcode","max"]])

print(df[["postcode","max","min","first","dense","aver"]])
