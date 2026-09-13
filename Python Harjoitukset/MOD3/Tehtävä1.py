pituus = float(input("anna kuhan mitta senttimetreinä"))
if pituus < 37:
    print("Kuha on liian pieni, laske takaisin järveen")
    puuttuu = 37 - pituus
    print(f"Pyyntimitasta puuttuu {puuttuu:.1f} cm")
else:
    print("Kuha on riittävän suuri, voit ottaa sen mukaasi")