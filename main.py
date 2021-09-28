import Menu

import Manager

import Customer

while True:
    user_action = Menu.Menu.main_menu()

    if user_action == "1":

        while True:
            user_role = Menu.Menu.role_menu()

            if user_role == "1":
                Manager.Manager.register()

            else:
                Customer.Customer.register()

            while True:
                register_again = input("DO YOU WANT TO REGISTER AGAIN?(y: yes, n: no): ").lower()

                if register_again.isalpha() and register_again in ["y", "n"]:
                    break
                else:
                    print("\nINVALID INPUT! please enter between 'y' and 'n'.")
                    continue

            if register_again == "y":
                continue
            else:
                break

    if user_action == "2":
        while True:
            user_role = Menu.Menu.role_menu()

            if user_role == "1":
                user_name = Manager.Manager.sign_in()

                Manager.Manager.warning(user_name)  # test1

                if user_name:
                    while True:
                        manager_option = Menu.Menu.manager_menu()

                        if manager_option == "1":

                            while True:
                                Manager.Manager.record_goods(user_name)

                                while True:
                                    record_again = input("\nDO YOU WANT TO RECORD AGAIN?(y: yes, n: no): ").lower()

                                    if record_again.isalpha() and record_again in ["y", "n"]:
                                        break

                                    else:
                                        print("\nINVALID INPUT! please enter between 'y' and 'n'.")
                                        continue

                                if record_again == "y":
                                    continue
                                else:
                                    while True:
                                        if Manager.Manager.inventory_update_customer(user_name):  # test2
                                            break
                                        else:
                                            continue
                                    break

                        elif manager_option == "2":
                            print(Manager.Manager.view(user_name))

                        elif manager_option == "3":
                            Manager.Manager.view_all_invoices()

                        elif manager_option == "4":
                            Manager.Manager.filter_invoices()  # test3

                        elif manager_option == "5":
                            Customer.Customer.view()

                        elif manager_option == "6":
                            Manager.Manager.customer_blocker(user_name)

                        elif manager_option == "7":
                            break

                else:
                    continue

            else:
                user_name = Customer.Customer.sign_in()

                if user_name:

                    while True:
                        customer_option = Menu.Menu.customer_menu()

                        if customer_option == "1":
                            pass

                        elif customer_option == "2":
                            pass

                        elif customer_option == "3":
                            pass

                        elif customer_option == "4":
                            pass

                        elif customer_option == "5":
                            pass

                        elif customer_option == "6":
                            pass

                        elif customer_option == "7":
                            pass

                        elif customer_option == "8":
                            pass

                        elif customer_option == "9":
                            pass

                        elif customer_option == "10":
                            pass

                        elif customer_option == "11":
                            break
            break

    elif user_action == "3":
        break
