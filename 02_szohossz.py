"""
2️⃣ Szóhossz meghatározása – tweet vagy SMS ellenőrzés
Feladat: Kérj be egy üzenetet a felhasználótól, majd írd ki, hány karakterből áll. Hasznos lehet például Twitter/SMS hosszkorlátozás ellenőrzéséhez.
"""
uzenet = input("Add meg azu üzeneted: ")
uzenet_hossza = len(uzenet)
print(f"Az üzeneted hossza{uzenet_hossza} karakter")