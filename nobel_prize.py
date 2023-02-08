import requests

HELP_STRING = """
1- Ange ett år och fält
Exempelvis: 1965 fysik
2- välj 2 om du är osäker
Q- stäng av
H- hjälp
"""

cat = {"fysik": "phy",
       "kemi": "che",
       "litteratur": "lit",
       "ekonomi": "eco",
       "fred": "pea",
       "medicin": "med"}


# TODO 10p programmet skall ge en hjälpsam utskrift istället för en krasch om användaren skriver in fel input
# TODO 15p om användaren inte anger ett område som exempelvis fysik eller kemi så skall den parametern inte skickas med till apiet och vi får då alla priser det året

def calcMoneyForEachPrize(money: float, prize_cnt: float):
    average_money = money / prize_cnt
    res = round(average_money, 3)
    return res


def checkfield(field: str):
    if field not in cat:
        return False
    else:
        return True


# def summa, årtal och fält
def getInforamationFromServer(year: int, field: str):
    params = {"nobelPrizeYear": year, "nobelPrizeCategory": cat[field]}
    res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=params).json()
    return res


# print alla årtal
def printAllInformationsForYear(year: int):
    for item in cat:
        print("*" * 30)
        print(f"Field is {item}")
        res = getInforamationFromServer(int(year), item)

        for p in res["nobelPrizes"]:
            print("----------------------------")
            peng = p["prizeAmount"]
            idagpeng = p["prizeAmountAdjusted"]
            print(f"{p['categoryFullName']['se']} prissumma {peng} SEK")
            print(f"{p['categoryFullName']['se']} prissumma {idagpeng} SEK")
            prize_cnt = 0

            for m in p["laureates"]:
                print("----------------------------")
                if "knownName" in m:
                    print(m['knownName']['en'])
                print(m['motivation']['en'])
                andel = m['portion']
                prize_cnt += 1

                printResult(peng, idagpeng, prize_cnt)


def printOneFieldForYear(year: int, field: str):
    res = getInforamationFromServer(int(year), field)
    for p in res["nobelPrizes"]:
        print("----------------------------")
        peng = p["prizeAmount"]
        idagpeng = p["prizeAmountAdjusted"]
        print(f"{p['categoryFullName']['se']} prissumma {peng} SEK")
        prize_cnt = 0

        for m in p["laureates"]:
            print("----------------------------")
            if "knownName" in m:
                print(m['knownName']['en'])
            print(m['motivation']['en'])
            andel = m['portion']
            prize_cnt += 1

        print("*" * 30)
        money_for_thattime = calcMoneyForEachPrize(peng, prize_cnt)
        result1 = f'{money_for_thattime:.3f}'
        print(f"The money of the time for each prizer is {result1}")
        money_for_now = calcMoneyForEachPrize(idagpeng, prize_cnt)
        result2 = f'{money_for_now:.3f}'
        print(f"The Today's value for each prizer is {result2}")

    for item in cat:
        print("*" * 30)
        print(f"Field is {item}")
        res = getInforamationFromServer(int(year), item)

    for p in res["nobelPrizes"]:
        print("----------------------------")
        peng = p["prizeAmount"]
        idagpeng = p["prizeAmountAdjusted"]
        print(f"{p['categoryFullName']['se']} prissumma {peng} SEK")
        print(f"{p['categoryFullName']['se']} prissumma {idagpeng} SEK")
        prize_cnt = 0

        for m in p["laureates"]:
            print("----------------------------")
            if "knownName" in m:
                print(m['knownName']['en'])
            print(m['motivation']['en'])
            andel = m['portion']
            prize_cnt += 1

        print("*" * 30)
        money_for_thattime = calcMoneyForEachPrize(peng, prize_cnt)
        result1 = f'{money_for_thattime:.3f}'
        print(f"The money of the time for each prizer is {result1}")
        money_for_now = calcMoneyForEachPrize(idagpeng, prize_cnt)
        result2 = f'{money_for_now:.3f}'
        print(f"The Today's value for each prizer is {result2}")


# print resultat

def printResult(peng: float, idagpeng: float, prize_cnt: int):
    print("*" * 30)
    money_for_thattime = calcMoneyForEachPrize(peng, prize_cnt)
    result1 = f'{money_for_thattime:.3f}'
    print(f"The money of the time for each prizer is {result1}")

    money_for_now = calcMoneyForEachPrize(idagpeng, prize_cnt)
    result2 = f'{money_for_now:.3f}'
    print(f"The Today's value for each prizer is {result2}")


def printOneFieldForYear(year: int, field: str):
    res = getInforamationFromServer(int(year), field)

    for p in res["nobelPrizes"]:
        print("----------------------------")
        peng = p["prizeAmount"]
        idagpeng = p["prizeAmountAdjusted"]
        print(f"{p['categoryFullName']['se']} prissumma {peng} SEK")
        prize_cnt = 0

        for m in p["laureates"]:
            print("----------------------------")
            if "knownName" in m:
                print(m['knownName']['en'])
            print(m['motivation']['en'])
            andel = m['portion']
            prize_cnt += 1
        printResult(peng, idagpeng, prize_cnt)


def main():
    print(HELP_STRING)
    while True:

        # TODO 5p Skriv bara ut hjälptexten en gång när programmet startar inte efter varje gång användaren matat in en fråga
        #      Förbättra hjälputskriften så att användaren vet vilka fält, exempelvis kemi som finns att välja på
        meny_val = input(
            "Välj ett av fälten \nSkriv enligt hjälprutan (år,fält), hjälp(H) eller avsluta(Q) ").upper().strip()

        if meny_val == "2":
            print("Fälten")
            for item in cat:
                print(item)
                pass

        if meny_val == '1':
            field = ""
            year = ""
            aaa = input(">")
            str_list = aaa.split()
            flag = "All"
            if (len(str_list) == 1):
                flag = "All"
                year = str_list[0]
            else:
                flag = "OneField"
                year, field = aaa.split()

            if flag == "OneField" and not checkfield(field):
                print("You should print correct field.\n You can find the fields select 2")
            else:
                if (flag == "OneField"):
                    printOneFieldForYear(int(year), field)
                else:
                    printAllInformationsForYear(int(year))
            if meny_val.upper() == "H":
                print(HELP_STRING)

            if meny_val.upper() == "Q":
                print("Tack och hejdå!")
                return


if __name__ == '__main__':
    main()