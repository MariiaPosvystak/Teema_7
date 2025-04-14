from random import * 

# 1. отображение столицы, если вводиться название государства и наоборот.
# 2. если искомое слово отсутствует в словаре, дайте пользователю возможность добавить его в словарь.
# 3. если пользователь находит ошибку в словаре, то у него должна быть возможность ее исправить.
# При желании пользователя проверить знание слов из словаря, реализуйте эту возможность 
# случайным образом появляются названия столиц/стран,
# после ввода соответствующего значения, сообщение о правильности или нет 
# после окончания проверки знаний результат в %)

#1
def riigid_pealinnad():
    riik=input("Palun sisestage riik:")
    print("Riigi pealinn on:", "riigid_pealinnad.txt"[riik])



# def failist_to_dict(f:str):
#     riik_pealinn={}
#     pealinn_riik={}
#     riigid=[]
#     file=open(f, "r", encoding="utf-8-sig")
#     for line in file:
#         k,v=line.strip().split("-")
#         riik_pealinn[k]=v
#         pealinn_riik[v]=k
#         riigid.append(k)
#     file.close()
#     return riik_pealinn, pealinn_riik, riigid
# riik_pealinn, pealinn_riik, riigid=failist_to_dict("riigid_pealinnad.txt")