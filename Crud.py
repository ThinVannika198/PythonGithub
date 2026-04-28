stuffs = []
prices = []

while True:
    print("\n" + "="*10 + " Menu " + "="*10)
    print("1. Input")
    print("2. Output")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Add Data")
    print("7. Check the bill")
    print("0. Exit")
    print("="*26)

    op = input("Choose your option: ")

    match op:
        case '1' | '6': # Combined Input and Add Data as they do the same thing
            header = "Input" if op == '1' else "Add Data"
            print(f"========== {header} ==========")
            while True:
                stuff = input("Enter your stuff (or 'q' to quit): ")
                if stuff.lower() == 'q':
                    break
                try:
                    price = float(input(f"Enter price for '{stuff}': "))
                    stuffs.append(stuff)
                    prices.append(price)
                except ValueError:
                    print("Invalid price! Please enter a number.")

        case '2':
            print("========== Output ==========")
            if not stuffs:
                print("No items yet.")
            else:
                for i, (s, p) in enumerate(zip(stuffs, prices), start=1):
                    print(f"{i}. {s} - ${p:.2f}")

        case '3':
            print("========== Search ==========")
            search_item = input("Enter item to search: ")
            if search_item in stuffs:
                idx = stuffs.index(search_item)
                print(f"'{search_item}' found at position {idx + 1}, price: ${prices[idx]:.2f}")
            else:
                print("Item not found.")

        case '4':
            print("========== Update ==========")
            old = input("Enter item name to update: ")
            if old in stuffs:
                idx = stuffs.index(old)
                new_name = input("Enter new item name: ")
                try:
                    new_price = float(input("Enter new price: "))
                    stuffs[idx] = new_name
                    prices[idx] = new_price
                    print("Updated successfully.")
                except ValueError:
                    print("Update failed: Invalid price.")
            else:
                print("Item not found.")

        case '5':
            print("========== Delete ==========")
            old = input("Enter item to delete: ")
            if old in stuffs:
                idx = stuffs.index(old)
                stuffs.pop(idx)
                prices.pop(idx)
                print("Deleted successfully.")
            else:
                print("Item not found.")

        case '7':
            print("********* Check the bill **********")
            if not stuffs:
                print("No items to bill.")
            else:
                total = sum(prices)
                for s, p in zip(stuffs, prices):
                    print(f"{s:15} : ${p:8.2f}")
                print("-" * 30)
                print(f"{'Total':15} : ${total:8.2f}")

        case '0':
            print("Exiting... Thank you!")
            break

        case _:
            print("Invalid option. Please choose from 0-7.")