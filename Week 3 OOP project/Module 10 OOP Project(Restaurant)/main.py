
from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from Users import Chef, Sever, Manager, Customer
from Order import Order
def main():
    # print('main as cpp')
    menu = Menu()
    # add pizza item
    pizza_1 = Pizza('suti pizza', 600, 'large', 'sutki and onion')
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('dal pizza', 500, 'medium', 'dal and onion')
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('meat pizza', 800, 'large', 'meat and onion')
    menu.add_menu_item('pizza', pizza_3)

    # add burger items
    Burger_1 = Burger('cicken burger', 850, 'chicken meat', 'meat and latus')
    menu.add_menu_item('burger', Burger_1)
    Burger_2 = Burger('cheze burger', 950, 'cheze', 'cheze and latus')
    menu.add_menu_item('burger', Burger_2)
    Burger_3 = Burger('meat burger', 1000, 'beef meat', 'meat and latus')
    menu.add_menu_item('burger', Burger_3)

    # add drinks items
    drinks = Drinks('Coke', 50, True)
    menu.add_menu_item('drinks', drinks)
    coffee = Drinks('Mocha coffee', 40, True)
    menu.add_menu_item('drinks', coffee)
    tea = Drinks('Red Tea', 55, True)
    menu.add_menu_item('drinks', tea)


# show menu
    menu.show_menu()

    print('==================== employees=================')
# naming a restaurant
    restaurant = Restaurant('time pass', 1500, menu)

    manager = Manager('arif', 12345, 'manager@gmail.com', 'kalihati', 500, 'july 2023', 'core')
    restaurant.add_employee('manager', manager)

    chef = Chef('kader mia', 1234, 'kader@mail.com', 'sirajgonj', 700, 'jun 2023', 'cooking', 'pizza and burger')
    restaurant.add_employee('chef', chef)

    server = Sever('jamal', 4587, 'jamal@gmail.com','Borishal', 450, 'jun 2023', 'server')
    restaurant.add_employee('server', server)

    restaurant.show_employees()

    print('==============CUSTOMER==================')

    #Customer placing order
    customer_1 = Customer('Skib khan', 78954, 'sakib@gmail.com', 'Khakan bari', 100000)
    order_1 = Order(customer_1,[pizza_2, coffee, Burger_1])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)
    restaurant.receive_payment(order_1, 5000, customer_1)

    print(f'Revenue: {restaurant.revenue}, balance: {restaurant.balance}')
   
    # customer pay for his order
   # after first customer
    customer_2 = Customer('khan', 785654, 'khan@gmail.com', 'akan bari', 4000)
    order_2 = Order(customer_2,[pizza_3, tea, Burger_2])
    customer_1.pay_for_order(order_2)
    restaurant.add_order(order_2)
    restaurant.receive_payment(order_2, 2000, customer_2)
    print(f'Revenue: {restaurant.revenue}, balance: {restaurant.balance}')

   
   # pay rent
    restaurant.pay_expanse(300, 'for rent of place')
    print('after rent:', restaurant.revenue, restaurant.balance, restaurant.expense)
    restaurant.pay_salay(chef)
    print('after pay salary:', restaurant.revenue, restaurant.balance, restaurant.expense)
    
    

    

    






# main()
# call main method
if __name__ == '__main__':
    main()