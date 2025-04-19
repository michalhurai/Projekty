# ODKAZY:
# https://www.w3schools.com/python/python_ref_keywords.asp
# https://www.w3schools.com/python/python_ref_list.asp
# https://www.w3schools.com/python/python_strings_methods.asp

# LIST: v hranatých zátvorkách [] - obsah dá sa meniť
# TUPLE: v okrúhlych zátvorách (), alebo aj bez nich - obsah sa nedá meniť
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

# Domáca úloha 1.lekcia
mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""

print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(cara)
print(nabidka)
print(cara)

destinace = input("CISLO DESTINACE: ")
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")
email = input("EMAIL: ")
print(cara)

spravna_destinace = mesta[int(destinace) - 1]
cena = ceny[int(destinace) - 1]

print(f"""DEKUJI, {jmeno} ZA OBJEDNAVKU,
CIL. DESTINACE: {spravna_destinace}, CENA JIZDNEHO: {cena},
NA TVUJ MAIL {email} JSME TI POSLALI LISTEK.""")

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
# .appen: pridá záznam na koniec listu
# .clear: vyčistí list
# .copy: kopírovať list
# .count:
# .extend:
# .index:
# .insert: dodá záznam na konkrétnu pozíciu v liste
# .pop:
# .remove: odstráni záznam v liste
# .reverse: obráti zoznam v liste
# .sort: zoradí list abecedne

# ZOZNAMY modifikácia/úprava
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
zaznam.insert(0, "2021-01-01 11:10:11:1111 - BANG,")
zaznam.append("2021-01-01 11:14:11:1111 - BANG BANG!")
print(zaznam)

# PODMIENKY if/elif/else - domáca úloha 2.lekcia
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

# SLOVNÍKY: zadávajú sa do {}
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

počet_slov = len(slovnik) # zobrazí počet záznamov v slovníku "dĺžku"
print("Počet slov:", počet_slov)  # zobrazí počet záznamov v slovníku "dĺžku"

# 2.
print("Česká slova:", list(slovnik.keys())) # vráti hodnotu "na ľavej strane" = KĽÚČ - KEYS
print(dict.keys(slovnik)) # alternatíva bez "záhlavia"

# 3.
print("Anglická slova:", list(slovnik.values())) # vráti hodnotu "na pravej strane" = HODNOTA - VALUES
print(dict.values(slovnik)) # alternatíva bez "záhlavia"

# 4.
ceske_slovo = input("Zadej české slovo: ") # pridanie kľúča
anglicky_preklad = input("Zadej anglicky překlad: ") # pridanie hodnoty
slovnik[ceske_slovo] = anglicky_preklad # párovanie hodnôt, dodanie hodnoty aj kľúča do slovníka

# 5
vyhledej = input("Jaké slovo hledáš? ")
print(slovnik.get(vyhledej, f"Slovo {vyhledej} není ve slovníku.")) # vyhľadá kľúč v slovníku

ceske_slovo = input("Zadej české slovo pro ověření: ")
preklad = slovnik.get(ceske_slovo)
if preklad:
    print(f"Anglický překlad pro '{ceske_slovo}' je: {preklad}")
else:
    print(f"Slovo '{ceske_slovo}' není ve slovníku.") # náhrada za funkciu .get

# 6
odstraň = input("Jaké slovo chceš odstranit? ")
slovnik.pop(odstraň)
print(slovnik) # odstráni zadané slovo
del slovnik["kočka"] # odstráni konkrétny kľúč a hodnotu

# F-STRING preddefinovanie kľudne aj celého reťazca
pozdrav = f"Ahoj {meno}" 
print(pozdrav)

# .copy používa sa copy.deepcopy = vtedy sa pri modifikácii upraví iba daný zoznam a nie prvotný
# .pop sa dá nahradiť univerzálnou metodou "del": del slovnik["kočka"] 
# .popitem() maže posledne dodanú hodnotu a kľúč
# .get namiesto chyby ktorá spôsobí pád systému vráti hodnotu "NONE"

auta = uzivatel.setdefault("auta", ["Skoda Octavia"]) # .setdefault - vezme hodnotu z listu, ak nemá tak pridadí definovanú hodnotu
print(auta) # = Skoda Octavia (užívateľ nemá auto tak mu dáme Octaviu)
# .update spája viacero slovníkov

# SET: zoznamy/množiny FROZENSET: nemeniteľné zoznamy/množiny - nedá sa dodávať ani odoberať hodnota
# .union nahrádza znak "|" - spája sety (všetky hodnoty)
# .intersection nahrádza znak "&" - spája iba spoločné hodnoty v setoch
# .difference nahrádza znak "-" - vráti rozdiely v setoch (A - B, B - A)
# .simmetric_difference nahrádza znak "^" - vráti všetky rozdiely v setoch
# .remove - nahrádza sa .discard pokiaľ nechceme aby program padol

# Předem dané množiny
mnozina_1 = {"kočka", "pes", "králík", "had"}
mnozina_2 = {"pes", "papoušek", "had", "ryba"}

# 1. Zjištění, kolik různých zvířat obsahuje každá množina
pocet_mnozina_1 = len(mnozina_1)
pocet_mnozina_2 = len(mnozina_2)
print(f"Množina 1 obsahuje {pocet_mnozina_1} zvířat.")
print(f"Množina 2 obsahuje {pocet_mnozina_2} zvířat.")

# 2. Výpis zvířat, která jsou v první množině, ale nejsou ve druhé (rozdíl množin)
rozdil_1_2 = mnozina_1 - mnozina_2
print("Zvířata v první množině, ale ne ve druhé:", rozdil_1_2)

# 3. Výpis zvířat, která jsou ve druhé množině, ale nejsou v první
rozdil_2_1 = mnozina_2 - mnozina_1
print("Zvířata ve druhé množině, ale ne v první:", rozdil_2_1)

# 4. Průnik množin (zvířata, která jsou v obou množinách)
prunik = mnozina_1 & mnozina_2
print("Zvířata, která jsou v obou množinách:", prunik)

# 5. Sjednocení množin (všechna zvířata z obou množin)
sjednoceni = mnozina_1 | mnozina_2
print("Všechna zvířata z obou množin:", sjednoceni)

# 6. Přidání nového zvířete zadaného uživatelem do první množiny
nove_zvire = input("Zadej nové zvíře, které chceš přidat do první množiny: ")
mnozina_1.add(nove_zvire)
print("Aktualizovaná množina 1:", mnozina_1)

# 7. Odstranění zvířete zadaného uživatelem z druhé množiny
zvire_k_odstraneni = input("Zadej zvíře, které chceš odstranit z druhé množiny: ")
if zvire_k_odstraneni in mnozina_2:
    mnozina_2.remove(zvire_k_odstraneni)
    print(f"Zvíře '{zvire_k_odstraneni}' bylo odstraněno z druhé množiny.")
else:
    print(f"Zvíře '{zvire_k_odstraneni}' není ve druhé množině.")
    
print("Aktualizovaná množina 2:", mnozina_2)

# VOLITEĽNÉ ARGUMENTY
# print("Ja", "Ty", "On", sep=", ", end="a ") # oddeľuje text napríklad čiarkou (sep) + môže pokračovať v riadku (end)
# print("Ona", "Oni", "My", sep=", ")

skupina_1 = [
    'h.vybíralová@firma.cz', 'w.štrumlová@firma.cz', 'm.vybíralová@firma.cz',
    's.bechyňka@firma.cz', 'z.urbánková@firma.cz', 'l.riečan@firma.cz',
    'v.koudelová@firma.cz', 'f.vorlová@firma.cz', 'i.seleš@firma.cz'
]

skupina_2 = [
    'j.šmíd@firma.cz', 'j.procházková@firma.cz', 'l.riečan@firma.cz', 'd.hlavatá@firma.cz', 
    'm.železný@firma.cz', 'p.niklesová@firma.cz', 'b.skok@firma.cz',
]

s1 = set(skupina_1)
s2 = set(skupina_2)

if s1 & s2: # vyhľadať prienik a vypísať výsledok
    print("Máme užívateľa v oboch skupinách")
else:
    print("Žiadny užívateľ v oboch skupínách")

print(s1 & s2) # vyhľadať prienik a vypísať hodnotu
s2.discard('l.riečan@firma.cz') # zmazať prienik
s2.add("matous.holinka@firma.cz") # dodať do skupiny_2
print(s2)
s = frozenset(s1.union(s2)) # zjednotiť skupiny a definovať ako "frozenset"
print (s)

# Zjednotenie slovníkov (domáca úlohy 3.lekcia)
pozdrav = "VÍTEJ V NAŠEM FILMOVÉM SLOVNÍKU!"
sluzby = ("dostupné filmy", "detaily filmu", "seznam režisérů")
hlavička = " | " .join(sluzby).center(62) # .join zjednotí položky zoznamu, ako prvý sa zadáva separátor
oddelovac = "=" * 62
film_1 = {
    "jmeno": "Shawshank Redemption",
    "rating": "93/100",
    "rok": 1994,
    "reziser": "Frank Darabont",
    "stopaz": 144
}
film_2 = {
    "jmeno": "The Godfather",
    "rating": "92/100",
    "rok": 1972,
    "reziser": "Francis Ford Coppola",
    "stopaz": 175
}
film_3 = {
    "jmeno": "The Dark Knight",
    "rating": "90/100",
    "rok": 2008,
    "reziser": "Christopher Nolan",
    "stopaz": 152
}
# sjednoť předchozí 3 slovníky do jednoho slovníku 'filmy'
# .. klíčem bude jméno filmu a samotný slovník následuje
# .. jako hodnota.
filmy = {
    film_1["jmeno"]: film_1,
    film_2["jmeno"]: film_2,
    film_3["jmeno"]: film_3,
}

print(pozdrav.center(62))
print(oddelovac)
print(hlavička)
print(oddelovac)
print("Dostupné filmy:".center(62))
print(oddelovac)
print(", " .join(filmy.keys())) # .join zjednotí kľúce slovníka, ako prvý sa zadáva separátor
print(oddelovac)
print("Detail filmu:")
print(oddelovac)
print(filmy["The Dark Knight"]) # vyhľadá na základe kľúča v tomto prípade "jmeno" názov filmu
print(oddelovac)
print("Všetci režíséri:")
print(oddelovac)

reziseri = []
for film in filmy.values():
    for k, v in film.items():
        if k == "reziser":
            reziseri.append(v)
print(reziseri)

# úloha po 3.lekcii
jmeno = "Marek"
heslo = "1234"
uzivatel = {"Marek": "1234"}
zprava = f"Ahoj {jmeno}, vítej v aplikaci! Pokračuj..."
oznam = "Uživatelské jméno nebo heslo nejsou v pořádku!"
if heslo == uzivatel.get(jmeno) and jmeno in uzivatel:
    print(f"Výstup: {zprava}")
else:
    print(f"Výstup: {oznam}")

# FOR / IN - iterácia, vypisovanie hodnôt (v riadkoch): ČÍSLA SA ITEROVAŤ NEDAJÚ!
for pismeno in ['a', 'b', 'c']:
    print(pismeno)
# SETY
for jmeno in {"Matouš", "Marek", "Lukáš"}:
    print(jmeno)
# TUPLE
for jmeno in ("Matouš", "Marek", "Lukáš"):
    print(jmeno)
# LIST
for jmeno in ["Matouš", "Marek", "Lukáš"]:
    print(jmeno)
# SLOVNIK
for kyes, values in {
    "jmeno": "Matous",
    "prijmeni": "Holinka",
    "email": "matous@holinka.com"
}.items():
    print(kyes, values, sep=": ") # vypíše slovník, možno dodať separátor. Ak zadám iba kyes, vráti iba kľúče (values detto)

pismena = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
for pismeno in pismena:
    if pismeno == "g":  # "a" --> False
        print("*Mam hodnotu ->*", pismeno)
    else:
        print("Nemam 'g', ale", pismeno)

suda_cisla = list()

for cislo in (1, 2, 3, 4, 5):
    if cislo % 2 == 0:      # pokud je hodnota v proměnné "cislo" sudá
        suda_cisla.append(cislo)  # ... přidej ji do seznamu "suda_cisla"

# po skončení smyčky vypíšeme obsah proměnné 'suda_cisla'
print(suda_cisla) # dodanie hodnoty to zoznamu (listu)

for cislo in (1, 2, 3, 4, 5):
    if cislo % 2 == 0:
        print("Sude cislo")
    elif cislo % 2 != 0:
        print("Liche cislo") # if/elif definícia/triedenie hodnôt

for pismeno in ("a", "b", "c", "d"):
    if pismeno == "c":
        print("Nasel jsem 'c', preskakuji cyklus..")
        break
    print(pismeno) # BREAK - ak nájde hodnotu, ukončí interáciu

for pismeno in ("a", "b", "c", "d"):
    if pismeno in {"a", "b"}:
        continue                             # CONTINUE - po vyhľadaní hodnôt, pokračuje v iterácii
    print("Hodnota", pismeno, "je dulezita") # V tomto prípade porovnáva SET {a, b} a STR (a, b, c, d). C a D nie sú v sete, tak ich vypíše (print)

for pismeno in ("a", "b", "c", "d"):
    print(pismeno.upper())
else:
    print("Vsechna pismena vypsana") #FOR/ELSE - vypíše všetky hodnoty a ak neobsahuje BREAK vypíše druhý print

for pismeno in ("a", "b", "c", "d"): # takto vypíše iba hľadanú hodnotu z LISTu
    if pismeno == "c":
        print("Nasel jsem 'c', preskakuji cyklus..")
        break
else:
    # kvůli 'break' se tento text nevypíše po ukončení smyčky
    print("Vsechna pismena vypsana")
print("Pokracuji po smycce") # BREAK - vypíše hľadanú hodnotu, a kvôli BREAK nevypíše "ELSE", ale až posledný print

for pismeno in "Matous":
    print(pismeno)
    break
print("-" * 29, "Konec smycky!", "-" * 29, sep="\n") # pri vynechaní "ELSE" vypíše hodnotu a vypíše posledný print

pismena = ["a", "b", "c", "d", "e", "f", "g", "h"]
for pismeno in pismena: # týmto zápisom bude vypisovať hodnoty z TUPLE kým nenájde správnu
    if pismeno == "e":
        print("Mam hodnotu ->", pismeno)
        break
    else:
        print("Nemam 'e', ale", pismeno)
print("Pokracuji s interpretaci naseho zapisu ^.^") # po nájdený hľadanej hodnoty ukončí interáciu posledným printom

for pismeno in "Matous":
    print(pismeno) # tu sa interácia končí ale pridaním CONTINUE bude pokračova a cez ELSE vypíše posledný print
    continue
else:
    print("-" * 29, "Konec smycky!", "-" * 29, sep="\n")

pismena = ["a", "b", "c", "d", "e", "f", "g", "h"]
for pismeno in pismena:
    if pismeno in {"a", "b", "c", "d"}: # porovnáva SET s TUPLE a vypíše iba rozdielne hodnoty
        continue
    print("Hodnota je dulezita:", pismeno) # pomocou CONTINUE vypíše print pre hodnoty mimo SETu

obsah = [
    ['jmeno;prijmeni;email;projekt'],
    ['Matous;Holinka;m.holinka@firma.cz;hr'],
    ['Petr;Svetr;p.svetr@firma.cz;devops']
]
for lines in obsah:
    print(lines)
    for cells in lines[0].split(";"): # musí byť zadaná hodnota [0]
        print(cells)

