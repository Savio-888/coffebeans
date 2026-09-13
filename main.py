from model.database import Database
from control.bean_controller import Bean_controller

if __name__ == '__main__':
    Database.create_database()
    Bean_controller.main()
