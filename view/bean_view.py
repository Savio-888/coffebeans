class Bean_view:
    @staticmethod
    def main_menu():
        while True:
            print('''---COFFE BEAN LOG---
            [1] - INSERT BEAN
            [2] - LIST BEANS
            [0] - EXIT''')
            choice = input('>> ')
            if choice in '120':
                return choice
            else:
                print('INPUT ERROR: Invalid Option')
                continue
    @staticmethod
    def insert_bean():
        while True:
            try:
                name = input('Input the name of the coffe bean:\n>> ')
                brewing = input('Input the brewing method (you need to write in a single line):\n>> ')
                rating = int(input('Input your rating (1 to 10):\n>> '))
                if rating not in range(1, 11):
                    print('ERROR: Rating not between 1 and 10, reseting...')
                    continue
                return name, brewing, rating
            except TypeError:
                print('ERROR: Invalid Input')
                continue
    @staticmethod
    def list_beans_menu():
        while True:
            print('''---LIST MENU---
            [1] - OLDEST TO NEWEST LOG
            [2] - NEWEST TO OLDEST LOG
            [3] - BETTER RATING TO WORST RATING
            [4] - WORST RATING TO BETTER RATING
            [0] - EXIT''')
            choice = input('>> ')
            if choice in '12340':
                return choice
            else:
                print('ERROR: Invalid Option')
                continue
    @staticmethod
    def list_beans(bean_list):
        if bean_list:
            for line in bean_list:
                print(f'\nNAME: {line['name']}\nBREWING METHOD: {line['brewing']}\nRATING: {line['rating']}/10\nDATE OF LOG: {line['date_create']}')
        else:
            print('There is no coffe beans log registered yet...')
