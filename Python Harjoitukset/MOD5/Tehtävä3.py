luku=int(input("anna luku:"))
if luku<2:
    print("luku on alkuluku")
else:
    print("luku ei ole alkuluku")
    for i in range(2,luku):
        if luku%i==0:
            on_alkuluku=False
            print("luku ei ole alkuluku)")
            break
    else:
        on_alkuluku=True
if on_alkuluku:
    print("luku on alkuluku")
else:
    print("luku ei ole alkuluku")

