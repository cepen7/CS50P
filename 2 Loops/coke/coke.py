
coke = 50
paid = 0

while True:  # loop for counting the amount paid
    if paid < coke:
        print(f"Amount Due: {coke - paid}")
        amount = int(input(f"Insert coin: "))
        # condition to accept only 3 types of coin
        if amount == 5 or amount == 10 or amount == 25:
            paid = paid + amount
    else:
        print(f"Change Owed: {paid - coke}")
        break

