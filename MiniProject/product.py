def product():
    items = []

    print("PRODUCTS")
    with open("products.txt", "r") as f:
        for line in f:
            data = line.strip().split()
            pid = int(data[0])
            name = data[1]
            price = int(data[2])
            items.append([pid, name, price, 0])
            print(pid, name, price)


    while True:
        ch = int(input("Enter product id: "))
        found = False

        for item in items:
            if item[0] == ch:
                qty = int(input("Enter quantity: "))
                item[3] += qty
                found = True
                break

        if not found:
            print("Invalid product id")

        flag = input("Do you want to shop (y/n): ").lower()
        if flag != "y":
            break

    print("\nBILL")
    print("ID   Name       Price   Qty   Total")

    total_amount = 0

    with open("bill.txt", "w") as f:
        f.write("ID   Name      Price   Qty   Total\n")

        for item in items:
            if item[3] > 0:
                pid = item[0]
                name = item[1]
                price = item[2]
                qty = item[3]
                total = price * qty
                total_amount += total

                print(f"{pid}  {name}  {price}    {qty}    {total}")
                f.write(f"{pid}  {name}  {price}  {qty}  {total}\n")

        print("Grand Total:", total_amount)
        f.write("Grand Total: " + str(total_amount))

    return total_amount