luvut=[]
while True:
    syote=input("anna lukuja, (tyhjä lopettaa):")
    if syote =="":
        break
    luvut.append(float(syote))
luvut.sort(reverse=True)
print("viisi suurinta lukua")
for luku in luvut[:5]:
    print(luku)