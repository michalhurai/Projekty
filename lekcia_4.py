samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'
vysledky = {'souhlasky': 0, 'samohlasky': 0}
veta = 'Zvuk řeči je produkován otevřenou konfigurací vokálního traktu'


for znak in veta:
    if not znak.isalpha():
        continue
    znak = znak.lower()
    if znak in samohlasky:
        vysledky['samohlasky'] += 1
    elif znak in souhlasky:
        vysledky ['souhlasky'] +=1

print("Počet samohlásek:", vysledky['samohlasky'],"|" "Počet souhlasek:", vysledky['souhlasky'])

zamestnanci_raw = """
Helena Vybíralová
Wendy Štrumlová
Marie Vybíralová
Stanislav Bechyňka
Zdeňka Urbánková
Lukáš Riečan
Veronika Koudelová
Františka Vorlová
Ilie Seleš
Martin Železný
Petra Niklesová
Bohumil Skok
Jakub Šmíd
Jarmila Procházková
Dagmar Hlavatá
Jiří Nguyen Thanh
Marie Franková
Dana Ulrichová
Jana Hranická
Hana Budošová
Ivan Široký
Květoslava Jiráčková
Pavel Przywara
Josef Umlauf
Tomáš Granzer
Miroslav Kuba
Miloslava Adámková
Marie Karlíková
Jaroslav Hronský
Vlasta Karlíková
Andrea Žatková
Zuzana Lokočová
Ondřej Ptáček
Zdeněk Najman
Tereza Šebešová
Antonie Skokánková
Jan Lion
Václav Vecko
František Vajgl
Adéla Kavková
Amália Vacková
Anna Pažická
Ivo Pustějovský
Antonín Pavela
Jitka Adamová
Libuše Hamroziová
Drahomíra Balzerová
Marek Suchánek
Petr Vavrinec
Jonáš Stuchlý
Jaromír Pecen
Markéta Kyliánková
Marina Pečenková
Ivana Perdochová
Michaela Drápalová
Michael Mentlík
Rudolf Špičák
Žaneta Holá
Blanka Lišková
Eva Svatoňová
Rostislav Hoang
Martina Kalivodová
Milan Hruška
Zdenka Marková
Lenka Schambergerová
Růžena Martinů
Věra Řezanková
Marie Pečenková
Miloš Váchal
Jaroslava Hrubá
Petr Pecen
Pavla Konvicová
Lucie Marešová
Květuše Zdráhalová
Vlastimila Svatošová
Zora Michalčíková
Daniel Švejnoha
Klára Brunclíková
Vladimír Bauer
Michal Slaný
Jiřina Novosadová
Karel Sršeň
Stanislava Lakosilová
Filip Černý
Alena Kubiková
Sára Kotrlová
Alois Rejlek
Božena Novotná
Maryana Nováková
Kateřina Máslová
Ladislav Dvořák
Radek Varga
Petr Dvořák
Ludmila Jaklová
Renáta Foubíková
Nikola Lehká
Dominika Riegerová
Patrik Polák
Soňa Štrbová
David Matoušek
Liubov Hollíková
Monika Poláková
Marie Jaklová
Aleš Svoboda
Roman Kolínský
Karolína Košiková
"""

zamestnanci = {}

for cele_jmeno in zamestnanci_raw.splitlines(): # ak nie sú hodnoty oddelené čiarkou, používame "splitlines"
    if cele_jmeno:
        zamestnanci[cele_jmeno] = {
            "krestni_jmeno": (kr_jmeno := cele_jmeno.split()[0]),
            "prijmeni": (prijmeni := cele_jmeno.split()[1]),
            "email": kr_jmeno.lower()[0] + "." + prijmeni.lower() + "@firma.cz",
#             "email": f"{kr_jmeno.lower()[0]}.{prijmeni.lower()}@firma.cz"
        }
print(zamestnanci)

zamestnanci_vystup = {}
for zamestnanec in zamestnanci_raw.split("\n"):
    if len(zamestnanec):
        jmeno = zamestnanec.split()[0]
        prijmeni = zamestnanec.split()[-1]
        zamestnanci_vystup[zamestnanec] = {
            "email": f"{jmeno[0]}.{prijmeni}@firma.cz",
            "krestni_jmeno": jmeno,
            "prijmeni": prijmeni
        }

print(zamestnanec)



