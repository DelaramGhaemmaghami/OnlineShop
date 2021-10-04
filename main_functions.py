def ask_register_again():
    while True:
        register_again = input("DO YOU WANT TO REGISTER AGAIN?(y: yes, n: no): ").lower()

        if register_again.isalpha() and register_again in ["y", "n"]:
            return register_again
        else:
            print("\nINVALID INPUT! please enter between 'y' and 'n'.")
            continue


def ask_record_again():
    while True:
        record_again = input("\nDO YOU WANT TO RECORD AGAIN?(y: yes, n: no): ").lower()

        if record_again.isalpha() and record_again in ["y", "n"]:
            return record_again

        else:
            print("\nINVALID INPUT! please enter between 'y' and 'n'.")
            continue


def ask_buy_again():
    while True:
        buy_again = input("DO YOU WANT TO BUY AGAIN?(y: yes, n: no): ")

        if buy_again.isalpha() and buy_again in ["y", "n"]:
            return buy_again

        else:
            print("INVALID INPUT! Please choose between 'y' and 'n'.")
            continue
