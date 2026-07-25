from model.bean import Bean
from view.bean_view import Bean_view
import sys

class Bean_controller:
    @staticmethod
    def main():
        while True:
            choice = Bean_view.main_menu()
            match choice:
                case '1':
                    name, brewing, rating = Bean_view.insert_bean()
                    Bean.insert_bean(name, brewing, rating)
                case '2':
                    choice = Bean_view.list_beans_menu()
                    match choice:
                        case '1':
                            list = Bean.list_beans()
                            Bean_view.list_beans(list)
                        case '2':
                            list = Bean.list_bydate()
                            Bean_view.list_beans(list)
                        case '3':
                            list = Bean.list_byrating_best()
                            Bean_view.list_beans(list)
                        case '4':
                            list = Bean.list_byrating_worst()
                            Bean_view.list_beans(list)
                        case '0':
                            sys.exit()
                case '0':
                    sys.exit()

