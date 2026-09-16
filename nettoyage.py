import pandas as pd
import os,sys
df=pd.read_csv("data/ventes.csv",sep=";")
print("lignes au depart",len(df))
df=df.drop_duplicates()
l=[]
for i in range(len(df)):
    x=df.iloc[i]["ville"]
    if type(x)==str:
        x=x.strip()
        x=x.lower()
        x=x.capitalize()
        if x=="":
            x="Inconnue"
    else:
        x="Inconnue"
    l.append(x)
df["ville"]=l
l2=[]
for i in range(len(df)):
    x=df.iloc[i]["date"]
    x=str(x).replace("/","-")
    l2.append(x)
df["date"]=l2
df["date"]=pd.to_datetime(df["date"])
l3=[]
for i in range(len(df)):
    x=df.iloc[i]["prix_unitaire"]
    x=str(x).replace(",",".")
    l3.append(float(x))
df["prix_unitaire"]=l3
df=df[df["quantite"].notna()]
df["quantite"]=df["quantite"].astype(float)
df=df[df["quantite"]>0]
df["total"]=df["quantite"]*df["prix_unitaire"]
# df["total"]=df["total"]*1.2
tmp=df.groupby("ville")["total"].sum()
tmp=tmp.sort_values(ascending=False)
print(tmp)
df.to_csv("data/ventes_propres.csv",index=False,sep=";")
tmp2=df.groupby("produit")["total"].sum()
tmp2=tmp2.sort_values(ascending=False)
print(tmp2)
tmp2.to_csv("data/total_par_produit.csv",sep=";")
tmp.to_csv("data/total_par_ville.csv",sep=";")
print("fini",len(df))
