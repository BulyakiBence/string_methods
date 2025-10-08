"""
3️⃣ Szó keresése a szövegben – tartalom ellenőrzés
Feladat: Kérj be egy bejegyzést a közösségi oldalra, majd ellenőrizd, hogy szerepel-e benne a „Python” szó.
"""

bejegyzes = input('Add meg a bejegyzésedet: ')
szo = input("Keresett szo: ")
x = bejegyzes.count(szo)
print(f"Ennyiszer volt benne {x}")