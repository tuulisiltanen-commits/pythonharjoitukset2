import random
lkm=int(input("kerro noppien määrä"))
summa=0
for i in range(lkm):
    silmaluku=random.randint(1,6)
    summa+=silmaluku
print(f"silmälukujen summa on, {summa}")
\

