print(("ja "+"ty " + "! ") *5) # spájanie stringu a násobenie
print(len("abeceda zjedla deda")) # meranie dĺžky stringu 
print("abeceda"[0]) # indexovanie - vypísanie znaku v poradí: "0" je prvý znak, "-1" je posledný znak
print("abeceda"[1:5]) # indexovanie "časť textu": určiť prvý a posledný znak
print("abedeca"[::4]) # indexovanie "preskakovanie": určiť prvý znak a potom každý "xtý" (druhý, piaty...)
meno = "Michal" # určenie premennej/identifikátora = TUPLE - nedá sa meniť
vek = 42
print(meno, vek) 
zoznam = ["Ja", "Ty", "On", "Ona", "My"] # LIST: hranaté zátvorky, je možné neskôr meniť
print(zoznam[1:3])
print(100>1) # BOOL: vyhodnotí pravdu TRUE/FALSE
print(100>1 and 1>100) # ak je jediná hodnota FALSE vyhodnotí celý príkaz ako FALSE
print(100==100 or 200==200)
print(not True) # NOT obráti hodnotu
print("M" in meno) # vyhodnocuje či sa hodnota nachádza na opačnej strane
print(2 in (1, 2, 3, 4))
zoznam = (1, 2, 3)
zoznam_1 = (1, 2, 3)
print(zoznam == zoznam_1) # == !=: porovnávajú hodnotu (celý text); is is not: porovnávajú objekt
cislo_1 = input("Zadaj prvé číslo: ")
cislo_2 = input("Zadaj druhé číslo: ")
if cislo_1 == cislo_2:          # if, elif, else: posledná podmienka "else" sa zadáva bez podmienky, už iba výsledok (print)
    print("Čísla sú rovnaké")
elif cislo_1 > cislo_2:
    print("Prvé číslo je väčie")
else:
    print("Druhé číslo je väčšie")
nove_cislo = int(input("ZADAJ ČÍSLO: ")) # pre definíciu čísla vo funkcii "input" sa musí dodať pred zátvorku "int" / "float"
if nove_cislo % 3 == 0 and nove_cislo % 5 == 0:
    print("FizzBuzz")
elif nove_cislo % 5 == 0:
    print("Buzz")
elif nove_cislo % 3 == 0:
    print("Fizz")
else:
    print(nove_cislo)

#METODY - PODMIENKY - PRIKAZY
books = ["1984", "Brave New World", "Fahrenheit 451", "The Hobbit"]
books.append("Dune") # doplniť na koniec zoznamu
print(books) 
books.insert(1, "Animal Farm") # doplniť na konkrétnu pozíciu
print(books)
books.remove("Fahrenheit 451") # odstrániť hodnotu
print(books)
books.sort() # zoradiť abecedne
print(books)
books_naopak = books.copy() # kópia zoznamu
books_naopak.reverse() # otočiť poradie
print(books_naopak)
print(len(books)) # spočíta záznamy - počet záznamov v zozname
search_title = input("ZADAJ NÁZOV KNIHY: ")
if search_title in books:
    position = books.index(search_title) # hľadanie pozície v zozname
    print(f"Kniha {search_title} je v zozname na {position} pozícii.")
else:
    print(f"Kniha nebola nájdená")
zaznam = ["""2021-01-01 11:11:11:1111 - něco se děje,
2021-01-01 11:12:11:1111 - nic to nebylo,
2021-01-01 11:13:11:1111 - a přece něco!,"""]
zaznam.insert(0, "BANG")
print(zaznam)
zaznam.append("BANG BANG!")
print(zaznam)
heslo = input("ZADAJ HESLO: ")
if not heslo:
    print("Nezadal si heslo")
elif heslo[0].isdigit() and not heslo.isnumeric():
    print("Heslo nemôže začínať číslom")
elif len (heslo) < 8:
    print("Heslo musí mať minimálne 8 znakov")
elif heslo.find("@") != -1:
    print("""Heslo nesmie obsahovať "@" """)
elif heslo.isnumeric() or heslo.isalpha():
    print("Heslo musí obsahovať čísla aj písmená")
else:
    print("Heslo je v poriadku")

#SLOVNÍKY: zadávajú sa do {}
uzivatel = {
    "jmeno": "Matouš",
    "vek": 100,
    "rid_opravneni": True,
    "volny_cas": ["klavír", "čtení", "Python!"],
    "kontakt":{
        "telefon": "123 456 789",
        "email": "email@email.com"
    }
}
print(uzivatel["jmeno"])
print(uzivatel["kontakt"]["telefon"])

slovnik = {
    "kočka": "cat",
    "pes": "dog",
    "strom": "tree",
    "auto": "car",
    "dům": "house"
}
print(len(slovnik)) # zobrazí počet záznamov v slovníku "dĺžku"
ceska_slova = slovnik.keys()
anglicka_slova = slovnik.values()
print(dict.keys(slovnik)) # vráti hodnotu "na pravej strane" = KĽÚČ
print(ceska_slova) # varianta pri definovaní "kľúča"
print(dict.values(slovnik)) # vrátif hodnotu "na ľavej strane" = HODNOTA
print(anglicka_slova) # varianta pri definovaní "hodnoty"
nove_cz_slovo = input("Zadaj nove CZ slovo: ") # pridanie kľúča
nove_en_slovo = input(f"Zadaj EN preklad {nove_cz_slovo}: ") # pridanie hodnoty
slovnik[nove_cz_slovo] = nove_en_slovo # párovanie hodnôt
print(slovnik)
ceska_slova = input("Zadaj CZ slovo: ") # ako vyhľadať kľúč (CZ) v slovníku a vrátiť jeho hodnotu (EN)
preklad = slovnik.get(ceska_slova)
if preklad:
    print(f"EN preklad pre {ceska_slova} je: {preklad}")
else:
    print(f"Slovo {ceska_slova} nie je v slovníku")
