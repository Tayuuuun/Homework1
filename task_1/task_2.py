

products = {
    '001': {'name': 'Батончик', 'price': 70},
    '002': {'name': 'Вода', 'price': 45},
    '003': {'name': 'Газировка', 'price': 64},
    '004': {'name': 'Булочка', 'price': 33}
}
#принимаемый номинал купюры
valid_bills = [10, 50, 100, 500]



def print_products():
    print("| ID  | ProductName | Цена |")
    print("|-----|-------------|------|")
    for product_id, product_info in products.items():
        print(f"| {product_id} | {product_info['name']:<11} | {product_info['price']:<4} |")


def vending_machine():

    print_products()

    product_id = input("Введите ID товара (или 'ОТМЕНА' для выхода): ").strip()

    if product_id.upper() == "ОТМЕНА":
        print("Операция отменена.")
        return

    if product_id not in products:
        print("Товара с таким ID не существует.")
        return

    selected_product = products[product_id]
    price = selected_product['price']

    print(f"Внесите {price} тугриков.")

    total_inserted = 0

    while total_inserted < price:
        user_input = input("Введите номинал купюры (или 'ОТМЕНА' для выхода): ").strip()

        if user_input.upper() == "ОТМЕНА":
            print("Операция отменена.")
            return

        try:
            bill = int(user_input)
        except ValueError:
            print("Внесена фальшивая купюра")
            continue

        if bill not in valid_bills:
            print("Внесена фальшивая купюра")
            continue

        total_inserted += bill

        if total_inserted >= price:
            change = total_inserted - price
            print(f"Ваша сдача: {change} тугриков.")
            break
        else:
            remaining = price - total_inserted
            print(f"Осталось внести {remaining} тугриков.")

vending_machine()


