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

počet_slov = len(slovnik) 
print("Počet slov:", počet_slov)  # zobrazí počet záznamov v slovníku "dĺžku"

# 2.
print("Česká slova:", list(slovnik.keys())) # vráti hodnotu "na pravej strane" = KĽÚČ
print(dict.keys(slovnik)) # alternatíva bez "záhlavia"

# 3.
print("Anglická slova:", list(slovnik.values())) # varianta pri definovaní "kľúča"
print(dict.values(slovnik)) # alternatíva bez "záhlavia"

# 4.
ceske_slovo = input("Zadej české slovo: ") # pridanie kľúča
anglicky_preklad = input("Zadej anglicky překlad: ") # pridanie hodnoty
slovnik[ceske_slovo] = anglicky_preklad # párovanie hodnôt, dodanie hodnoty aj kľúča do slovníka

# 5
vyhledej = input("Jaké slovo hledáš? ")
print(slovnik.get(vyhledej, f"Slovo {vyhledej} není ve slovníku.")) # vyhľadá kľúč v slovníku

# 6
odstraň = input("Jaké slovo chceš odstranit? ")
slovnik.pop(odstraň)
print(slovnik) # odstráni zadané slovo
pozdrav = f"Ahoj {meno}" # f-string preddefinovanie kľudne aj celého reťazca
print(pozdrav)

# .copy používa sa copy.deepcopy = vtedy sa pri modifikácii upraví iba daný zoznam a nie prvotný
# .pop sa dá nahradiť univerzálnou metodou "del"
# .popitem() maže posledne dodanú hodnotu a kľúč
# .get namiesto chyby ktorá spôsobí pád systému vráti hodnotu "NONE"
auta = uzivatel.setdefault("auta", ["Skoda Octavia"]) # .setdefault - vezme z listu, ak nemá tak pridadí definovanú hodnotu
print(auta) # = Skoda Octavia (užívateľ nemá auto tak mu dáme Octaviu)
# .update spája viacero slovníkov

# SET: zoznamy/množiny FROZENSET: nemeniteľné zoznamy/množiny
# .union nahrádza znak "|"
# .intersection nahrádza znak "&"
# .difference nahrádza znak "-"
# .simmetric_difference nahrádza znak "^"

# VOLITEĽNÉ ARGUMENTY
# print("Ja", "Ty", "On", sep=",", end="a ") # oddeľuje text napríklad čiarkou (sep) + môže pokračovať v riadku (end)
# print("Ona", "Oni", "My", sep=",")

