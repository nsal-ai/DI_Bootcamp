from rest_menu_manager import MenuItem

#def load_manager():
   # return self.MenuItem()


def show_user_menu():
    while user_choice != 'x':
        print('=== MENU ===')
        print('(a) Add an item')
        print('(d) Delete an item')
        print('(v) View the menu')
        print('(x) Exit')
        user_choice = input('Select your choice')

@classmethod
def add_item_to_menu():
    if user_choice == 'a':
        param = input('item and price').split()
        choice = MenuItem(param[0], param[1])
        choice.save()
        print('item added successfully')

@classmethod
def remove_item_from_menu():
    menu_item = input('which dish do you want to remove?')
    query = "select item from menu;"
    list_item = cursor.execute(query)
    if menu_item in list_item:
        return choice.delete()
    else:
        print('there was an error')
    




