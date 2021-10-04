import Menu

import Manager

import Customer

import main_functions

import Customer_functions

while True:
    user_action = Menu.Menu.main_menu()

    if user_action == "1":

        while True:
            user_role = Menu.Menu.role_menu()

            if user_role == "1":
                Manager.Manager.register()

            else:
                Customer.Customer.register()

            ask = main_functions.ask_register_again()

            if ask.lower() == "y":
                continue
            else:
                break

    if user_action == "2":
        while True:
            user_role = Menu.Menu.role_menu()

            if user_role == "1":
                user_name = Manager.Manager.sign_in()

                if user_name:

                    Manager.Manager.warning(user_name)

                    while True:
                        manager_option = Menu.Menu.manager_menu()

                        if manager_option == "1":

                            while True:
                                Manager.Manager.record_goods(user_name)

                                ask = main_functions.ask_record_again()

                                if ask.lower() == "y":
                                    continue
                                else:
                                    break

                        elif manager_option == "2":
                            print(Manager.Manager.view(user_name))

                        elif manager_option == "3":
                            Manager.Manager.view_all_invoices(user_name)

                        elif manager_option == "4":
                            Manager.Manager.filter_invoices(user_name)

                        elif manager_option == "5":
                            Customer.Customer.view_customers()

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
                            Customer.Customer.view_invoice(user_name)

                        elif customer_option == "2":
                            Customer.Customer.view_existed_stores()

                            desired_store_name = Customer_functions.wanna_buy()

                            if desired_store_name:

                                if Customer_functions.is_blocked(desired_store_name, user_name):
                                    continue

                                search_or_all = input("""Do you wanna search a specific good or you wanna see all """
                                                      """the goods?(s: search, a:all): """)

                                if search_or_all.lower() == "a":
                                    while True:
                                        print(Customer.Customer.view_goods(desired_store_name))
                                        Customer.Customer.inventory_update_customer(desired_store_name, user_name)

                                        ask = main_functions.ask_buy_again()

                                        if ask.lower() == "y":
                                            continue
                                        else:
                                            break

                                elif search_or_all.lower() == "s":
                                    while True:
                                        desired_brand_good_name = Customer.Customer.search_goods(desired_store_name)

                                        if desired_brand_good_name:
                                            brand_good, name_good = desired_brand_good_name

                                            Customer.Customer.inventory_update_customer(desired_store_name, user_name,
                                                                                        brand_good, name_good)

                                        ask = main_functions.ask_buy_again()

                                        if ask.lower() == "y":
                                            continue
                                        else:
                                            break

                            else:
                                continue

                        elif customer_option == "3":
                            desired_store_name = Customer.Customer.search_store()

                            if desired_store_name:

                                if Customer_functions.wanna_buy(desired_store_name):
                                    search_or_all = input(
                                        """Do you wanna search a specific good or you wanna see all """
                                        """the goods?(s: search, a:all): """)

                                    if search_or_all.lower() == "a":
                                        while True:
                                            print(Customer.Customer.view_goods(desired_store_name))
                                            Customer.Customer.inventory_update_customer(desired_store_name, user_name)

                                            ask = main_functions.ask_buy_again()

                                            if ask.lower() == "y":
                                                continue
                                            else:
                                                break

                                    elif search_or_all.lower() == "s":
                                        while True:
                                            desired_brand_good_name = Customer.Customer.search_goods(desired_store_name)

                                            if desired_brand_good_name:
                                                brand_good, name_good = desired_brand_good_name

                                                Customer.Customer.inventory_update_customer(desired_store_name,
                                                                                            user_name, brand_good,
                                                                                            name_good)

                                            ask = main_functions.ask_buy_again()

                                            if ask.lower() == "y":
                                                continue
                                            else:
                                                break

                        elif customer_option == "4":
                            break

            break

    elif user_action == "3":
        break
