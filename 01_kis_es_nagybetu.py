"""
1️⃣ Kis- és nagybetűssé alakítás – névformázás
Feladat: Kérj be egy felhasználónevet a regisztrációhoz, majd jelenítsd meg háromféleképpen:
- nagybetűs (pl. címkén vagy azonosítóban),
- kisbetűs (pl. email összehasonlításhoz),
- csak az első betű nagy (személyes üdvözlésnél).
"""

username = input("add meg  a felhasználó nevedet: ")

nagybetus_szo = username.upper()
print(f"Csupa nagybetű: {nagybetus_szo}")

kisbetus_szo = username.lower()
print(f"Csupa kisbetűs {kisbetus_szo}")

nagykezdobetus_szo = username.capitalize()
print(f"Nagy kezdőbetűűs szó: {nagykezdobetus_szo}")