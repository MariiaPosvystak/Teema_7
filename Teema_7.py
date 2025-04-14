def Loe_failist(fail:str)->list:
    f=open(fail,'r',encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()


list_=Loe_failist("fail.txt")
for x in list_:
    print(x)

list_=["Ann", "Kati","Mari"]
Kirjuta_failisse("fail.txt",list_)
list_2=Loe_failist("fail.txt")
print(list_2)
with open ("fail.txt", "r", encoding="utf-8-sig") as f:
    print(f.read())
with open ("fail.txt", "r", encoding="utf-8-sig") as f:
    print(f.read())
