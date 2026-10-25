palkka=float(input("anna tuntipalkka"))
tunnit=float(input("anna tuntimäärä"))
päivä=input("anna viikonpäivä")
if päivä.lower() == "sunnuntai":
    paivapalkka= palkka*tunnit*2
else:
    paivapalkka= palkka*tunnit
print(f"päiväpalkka:{paivapalkka}")