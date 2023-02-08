

import nobel_prizes

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar199
# vi använder oss enbart av /nobelPrizes

# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1

HELP_STRING = """
Ange det år och ämne som du 
Exempelvis 1965 fysik
"""

category = {"fysik": "phy",
            "kemi": "che",
            "litteratur": "lit",
            "ekonomi": "eco",
            "fred": "pea",
            "medicin": "med"}


# TODO 10p programmet skall ge en hjälpsam utskrift istället för en krasch om användaren skriver in fel input
# TODO 15p om användaren inte anger ett område som exempelvis fysik eller kemi så skall den parametern inte skickas med till apiet och vi får då alla priser det året


def main():
    print(HELP_STRING)
    while True:

        # TODO 5p Skriv bara ut hjälptexten en gång när programmet startar inte efter varje gång användaren matat in en fråga
        #      Förbättra hjälputskriften så att användaren vet vilka fält, exempelvis kemi som finns att välja på

        # TODO 5p Gör så att det finns ett sätt att avsluta programmet, om användaren skriver Q så skall programmet stängas av
        #      Beskriv i hjälptexten hur man avslutar programmet
        # TODO 5p Gör så att hjälptexten skrivs ut om användaren skriver h eller H
        prompt = input(">")
        year, field = prompt.split()
        cat = category[field]

        cat = {"nobelPrizeYear": int(year), "nobelPrizeCategory": cat}

        prizes = nobel_prizes.get_nobel_prizes(cat)

        # TODO 5p  Lägg till någon typ av avskiljare mellan pristagare, exempelvis --------------------------
        # TODO 20p Skapa en funktion som ger en summering av ett år. Om användaren exempelvis skriver "summering 1965"
        #   skall programmet skriva ut den totala prissumman det året samt hur många pristagare det var.
        #   Du skall alltså summera alla priser det året och räkna antalet pristagare.
        #   Exempel på hur det kan se ut:
        #   > summering 1965
        #   År 1965 fick 9 pristagare dela på totalt 1410000 kronor
        #   Tips: Tänk på alla priser inte delats ut alla år. Ekonomipriset infördes exempelvis 1968

        for prize in prizes["nobelPrizes"]:
            price_sum = prize["prizeAmount"]
            print(f"{prize['categoryFullName']['se']} prissumma {price_sum} SEK")

            for winner in prize["laureates"]:
                print(winner['knownName']['en'])
                print(winner['motivation']['en'])


if __name__ == '__main__':
    main()