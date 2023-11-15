def main():
    amount_due = 50
    while True:
        user_input = input("Insert coin: ").strip()
        if user_input == "25":
            amount_due = amount_due - int(user_input)
        elif user_input == "10":
            amount_due = amount_due - int(user_input)
        elif user_input == "5":
            amount_due = amount_due - int(user_input)
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
        else:
            print(f"Change Owed: {abs(amount_due)}")
            break


if __name__ == "__main__":
    main()
