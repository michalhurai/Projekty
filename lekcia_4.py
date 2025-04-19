obsah = [
    ['jmeno;prijmeni;email;projekt'],
    ['Matous;Holinka;m.holinka@firma.cz;hr'],
    ['Petr;Svetr;p.svetr@firma.cz;devops']
]
for lines in obsah:
    print(lines)
    for cells in lines[0].split(";"):
        print(cells)