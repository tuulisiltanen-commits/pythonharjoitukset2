luku=int(input("anna kokonaisluku"))
if luku % 3 == 0 and luku % 5 == 0:
    print("jaollinen molemmilla luvuilla")
elif luku % 3 == 0:
    print("luku on kolmella jaollinen") 
elif luku % 5 == 0:
    print("luku on jaollinen viidellä")
