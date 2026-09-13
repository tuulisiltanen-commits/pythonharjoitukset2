sukupuoli = input("kerro sukupuoli (nainen/mies): ").lower()
hemoglobiini=input("anna hemoglobiiniarvo (g/l): ")
hemoglobiini=float(hemoglobiini)

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

