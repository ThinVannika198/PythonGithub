stuffs = []
prices = []

while True:
    print("\n========== Menu ==========")
    print("1. Input")
    print("2. Output")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Add Data")
    print("7. Check the bill")
    print("0. Exit")
    print("==========================")

    op = input("Choose your option: ")
    match op:
        case '1':
            while True:
                print("========== Input ==========")
                stuff = input("Enter your stuff (or 'q' to quit): ")
                if stuff.lower() == 'q':
                    break
                price = float(input(f"Enter price for '{stuff}': "))
                stuffs.append(stuff)
                prices.append(price)

        case '2':
            print("========== Output ==========")
            if not stuffs:
                print("No items yet.")
            else:
                for i, (s, p) in enumerate(zip(stuffs, prices), start=1):
                    print(f"{i}. {s} - ${p:.2f}")

        case '3':
            print("========== Search ==========")
            stuff = input("Enter item to search: ")
            if stuff in stuffs:
                idx = stuffs.index(stuff)
                print(f"'{stuff}' found at position {idx + 1}, price: ${prices[idx]:.2f}")
            else:
                print("Item not found.")

        case '4':
            print("========== Update ==========")
            old = input("Enter item to update: ")
            if old in stuffs:
                index = stuffs.index(old)
                new = input("Enter new item name: ")
                new_price = float(input("Enter new price: "))
                stuffs[index] = new
                prices[index] = new_price
                print("Updated successfully.")
            else:
                print("Item not found.")

        case '5':
            print("========== Delete ==========")
            old = input("Enter item to delete: ")
            if old in stuffs:
                index = stuffs.index(old)
                stuffs.pop(index)
                prices.pop(index)
                print("Deleted successfully.")
            else:
                print("Item not found.")

        case '6':
            print("========== Add Data ==========")
            while True:
                add_item = input("Enter item to add (or 'q' to quit): ")
                if add_item.lower() == 'q':
                    break
                price = float(input(f"Enter price for '{add_item}': "))
                stuffs.append(add_item)
                prices.append(price)

        case '7':
            print("********* Check the bill **********")
            if not stuffs:
                print("No items to bill.")
            else:
                total = 0
                for stuff, price in zip(stuffs, prices):
                    print(f"{stuff}: ${price:.2f}")
                    total += price
                print(f"Total = ${total:.2f}")

        case '0':
            print("Exiting... Thank you!")
            break

        case _:
            print("Invalid option. Please choose from 0-7.")
