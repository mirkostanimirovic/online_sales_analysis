# Online Sales Analysis

## Opis projekta

Ovaj projekat predstavlja jednostavan Python sistem za upravljanje proizvodima u online prodavnici.  
Cilj projekta je vežbanje rada sa Python programiranjem, objektno orijentisanim programiranjem (OOP) i Git/GitHub sistemom za verzionisanje.

---

## Struktura projekta

Projekat sadrži sledeće Python datoteke:

- product.py
- product_manager.py
- cart.py
- main.py

---

## Klasa Product

Klasa Product predstavlja jedan proizvod.

Atributi:
- name – naziv proizvoda
- price – cena proizvoda
- quantity – količina proizvoda

Metode:
- display_info() – prikazuje informacije o proizvodu
- update_quantity() – ažurira količinu proizvoda

---

## Klasa ProductManager

Klasa ProductManager upravlja listom proizvoda.

Metode:
- add_product() – dodaje proizvod
- display_products() – prikazuje sve proizvode
- total_inventory_value() – računa ukupnu vrednost inventara
- remove_product() – uklanja proizvod po imenu

---

## Klasa Cart

Klasa Cart predstavlja korpu kupca.

Metode:
- add_to_cart() – dodaje proizvod u korpu
- display_cart() – prikazuje proizvode u korpi
- total_price() – računa ukupnu cenu korpe

---

## main.py

Datoteka main.py služi za pokretanje programa i demonstraciju rada sistema.

---

## Git funkcionalnosti

Tokom izrade projekta korišćene su sledeće Git funkcije:

- git clone
- git add
- git commit
- git branch
- git merge
- rešavanje konflikata

---

## .gitignore

U projektu je dodat .gitignore kako bi se ignorisali:

- config.json
- snimci ekrana