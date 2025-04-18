jmeno = "Marek"
heslo = "1234"
uzivatel = {"Marek": "1234"}

if heslo == uzivatel.get(jmeno) and jmeno in uzivatel:
    print(f"Ahoj {jmeno}, vítej v aplikaci! Pokračuj...")
else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku!")

if heslo == uzivatel["Marek"] and jmeno in uzivatel:
    print(f"Ahoj {jmeno}, vítej v aplikaci! Pokračuj...")
else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku!")



