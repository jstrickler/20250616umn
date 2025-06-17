print("Welcome to ticket sales\n")

while True:  # Loop "forever"
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        print("please enter a quantity between 1 and 32")
        continue  # Skip rest of loop; start back at top
    if raw_quantity.lower() == 'q':
        print("goodbye!")
        break  # Exit loop

    # try...
    quantity = int(raw_quantity)  # could validate via try/except
    if 0 < quantity < 33:
        print(f"sending {quantity} ticket(s)")
    else:
        print("Invalid number of tickets")
