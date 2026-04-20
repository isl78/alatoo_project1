from datetime import datetime

cart = []

products = {
    "apple": {"price": 120},
    "sugar": {"price": 95},
    "rice": {"price": 110},
    "cheese": {"price": 650},
    "flour": {"price": 80}
}


def show_products():
    print("\n📦 --- МАГАЗИН ---")
    for name, data in products.items():
        print(f"{name} - {data['price']} сом/кг")


def add_item():
    show_products()

    name = input("\nВведите товар: ").lower().strip()

    if name not in products:
        print("❌ Нет такого товара")
        return

    try:
        qty = float(input("Количество (кг): "))
        if qty <= 0:
            print("❌ Ошибка")
            return
    except ValueError:
        print("❌ Введите число")
        return

    cart.append({
        "name": name,
        "qty": qty,
        "price": products[name]["price"]
    })

    print("✔ Добавлено")


def show_cart():
    if not cart:
        print("🛒 Корзина пуста")
        return

    print("\n🛒 --- ЧЕК ---")
    print("Время:", datetime.now().strftime("%Y-%m-%d %H:%M"))

    total = 0

    for i, item in enumerate(cart, 1):
        sum_item = item["qty"] * item["price"]
        total += sum_item
        print(f"{i}. {item['name']} | {item['qty']} кг | {sum_item:.2f} сом")

    print("-" * 30)
    print(f"💰 ИТОГО: {total:.2f} сом")


def main():
    while True:
        print("\n--- МАГАЗИН ---")
        print("1 - Добавить")
        print("2 - Корзина")
        print("0 - Выход")

        choice = input("> ")

        if choice == "1":
            add_item()

        elif choice == "2":
            show_cart()

        elif choice == "0":
            print("\n🧾 ФИНАЛЬНЫЙ ЧЕК:")
            show_cart()
            print("👋 Спасибо!")
            break

        else:
            print("❌ Ошибка")


if __name__ == "__main__":
    main()