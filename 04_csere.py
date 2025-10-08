"""
4️⃣ Szó cseréje másikra – ételrendelés módosítása
Feladat: A rendelésben az „alma” helyett cseréld „körtére”, ha a boltban nincs alma.
"""

rendeles = input("Add meg a rendelesed: ")
alma =input("Van e alma a boltban (i/n):")
if alma == "n":
    x = rendeles.replace("alma", "körte")
    print(f"A rendelesed {x}")
else: 
    print(f"Nincs alma, ezért rendelésed: {rendeles}")