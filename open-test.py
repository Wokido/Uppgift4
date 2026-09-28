import csv
import locale
import subprocess

FILENAME = "db_products.csv"


def format_currency(value):
    return locale.currency(value, grouping=True)


def load_data(filename):
    products = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(
                    {
                        "id": int(row["id"]),
                        "name": row["name"],
                        "desc": row["desc"],
                        "price": float(row["price"]),
                        "quantity": int(row["quantity"]),
                    }
                )
    except FileNotFoundError:
        print(f"Hittade inte {filename}, skapar en ny tom lista.")
    return products


def save_data(filename, products):
    """Sparar ändringar permanent i CSV-filen."""
    fieldnames = ["id", "name", "desc", "price", "quantity"]
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)


def list_products(products):
    print(f"{'Nr':<4} {'Namn':<20} {'Pris':<15} {'Antal':<5}")
    print("-" * 50)
    for idx, product in enumerate(products, start=1):
        name = product["name"]
        price = format_currency(product["price"])
        quantity = product["quantity"]
        print(f"{idx:<4} {name:<20} {price:<15} {quantity:<5}")


def view_product(idx, products):
    subprocess.run("cls", shell=True)
    if 1 <= idx <= len(products):
        product = products[idx - 1]
        print("=" * 40)
        print(f"ID:          {product['id']}")
        print(f"Namn:        {product['name']}")
        print(f"Beskrivning: {product['desc']}")
        print(f"Pris:        {format_currency(product['price'])}")
        print(f"Antal:       {product['quantity']}")
        print("=" * 40)


# UPPGIFT 1 & 2: Lägg till produkt med automatiskt ID
def add_product(products):
    subprocess.run("cls", shell=True)
    print("LÄGG TILL NY PRODUKT")

    name = input("Namn: ").strip()
    desc = input("Beskrivning: ").strip()
    try:
        price = float(input("Pris: "))
        quantity = int(input("Antal: "))
    except ValueError:
        print("\n[Fel] Pris och antal måste vara siffror.")
        return

    # SVÅR (Uppgift 2): Automatiskt ID baserat på högsta befintliga ID
    max_id = (
        max(products, key=lambda p: p["id"])["id"] if products else 0
    )

    new_product = {
        "id": max_id + 1,
        "name": name,
        "desc": desc,
        "price": price,
        "quantity": quantity,
    }
    products.append(new_product)
    save_data(FILENAME, products)
    print(
        f"\nProdukten '{name}' har lagts till med automatiskt ID {new_product['id']}!"
    )


# UPPGIFT 1: Ta bort produkt
def remove_product(products):
    subprocess.run("cls", shell=True)
    try:
        target_id = int(input("Ange ID på produkten som ska tas bort: "))
    except ValueError:
        print("\n[Fel] Ogiltigt ID.")
        return

    for product in products:
        if product["id"] == target_id:
            products.remove(product)
            save_data(FILENAME, products)
            print(
                f"\nProdukten '{product['name']}' (ID {target_id}) har tagits bort."
            )
            return

    print(f"\nIngen produkt med ID {target_id} hittades.")


# UPPGIFT 3 (SVÅR): Ändra data för en produkt
def edit_product(products):
    subprocess.run("cls", shell=True)
    print("ÄNDRA PRODUKT")
    try:
        target_id = int(input("Ange ID på produkten du vill ändra: "))
    except ValueError:
        print("\n[Fel] Ogiltigt ID.")
        return

    product = next((p for p in products if p["id"] == target_id), None)
    if not product:
        print(f"\nIngen produkt med ID {target_id} hittades.")
        return

    print("\nTryck på Enter utan att skriva något för att behålla nuvarande värde.\n")

    new_name = input(f"Namn [{product['name']}]: ").strip()
    if new_name:
        product["name"] = new_name

    new_desc = input(f"Beskrivning [{product['desc']}]: ").strip()
    if new_desc:
        product["desc"] = new_desc

    new_price = input(f"Pris [{product['price']}]: ").strip()
    if new_price:
        try:
            product["price"] = float(new_price)
        except ValueError:
            print("[Fel] Ogiltigt pris. Bevarar gamla priset.")

    new_qty = input(f"Antal [{product['quantity']}]: ").strip()
    if new_qty:
        try:
            product["quantity"] = int(new_qty)
        except ValueError:
            print("[Fel] Ogiltigt antal. Bevarar gamla antalet.")

    save_data(FILENAME, products)
    print(f"\nProdukten '{product['name']}' har uppdaterats!")


# UPPGIFT 4 (ÖVERKURS): Statistik om alla produkter
def show_statistics(products):
    subprocess.run("cls", shell=True)
    print("PRODUKTSTATISTIK")
    print("=" * 60)

    if not products:
        print("Inga produkter finns i databasen.")
        return

    total_unique = len(products)
    total_quantity = sum(p["quantity"] for p in products)
    total_value = sum(p["price"] * p["quantity"] for p in products)
    avg_price = sum(p["price"] for p in products) / total_unique

    most_expensive = max(products, key=lambda p: p["price"])
    cheapest = min(products, key=lambda p: p["price"])

    print(f"Totalt antal unika produkter:  {total_unique}")
    print(f"Totalt antal artiklar i lager:  {total_quantity} st")
    print(f"Genomsnittspris per produkt:    {format_currency(avg_price)}")
    print(
        f"Dyraste produkt:                {most_expensive['name']} ({format_currency(most_expensive['price'])})"
    )
    print(
        f"Billigaste produkt:             {cheapest['name']} ({format_currency(cheapest['price'])})"
    )
    print(f"Totalt lagervärde:              {format_currency(total_value)}")
    print("-" * 60)
    print("Andel av totalt lagervärde per produkt:")

    for p in products:
        p_val = p["price"] * p["quantity"]
        pct = (p_val / total_value * 100) if total_value > 0 else 0
        print(f" - {p['name']:<22}: {format_currency(p_val):<14} ({pct:.1f}%)")

    print("=" * 60)


# Huvudprogram
try:
    locale.setlocale(locale.LC_ALL, "sv_SE.UTF-8")
except locale.Error:
    locale.setlocale(locale.LC_ALL, "")

products = load_data(FILENAME)

while True:
    subprocess.run("cls", shell=True)
    list_products(products)

    print("-" * 60)
    option = (
        input(
            "Vad vill du göra? [# = visa | L = lägg till | T = ta bort | Ä = ändra | S = statistik | Q = avsluta]: "
        )
        .strip()
        .lower()
    )

    if option.isdigit():
        idx = int(option)
        if 1 <= idx <= len(products):
            view_product(idx, products)
            input("\nTryck Enter för att gå tillbaka...")
    elif option == "l":
        add_product(products)
        input("\nTryck Enter för att gå tillbaka...")
    elif option == "t":
        remove_product(products)
        input("\nTryck Enter för att gå tillbaka...")
    elif option == "ä":
        edit_product(products)
        input("\nTryck Enter för att gå tillbaka...")
    elif option == "s":
        show_statistics(products)
        input("\nTryck Enter för att gå tillbaka...")
    elif option == "q":
        break