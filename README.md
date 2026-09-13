# Coffee Bean Log

This project is a Command Line Interface (CLI) application designed to log and rate coffee beans. It uses an SQLite database to store entries and follows a structured Model-View-Controller (MVC) architecture.

## Features

*   **Insert Beans:** Add a new coffee bean to your log by providing its name, the brewing method used (in a single line), and a rating from 1 to 10.
*   **View Logs:** Display your recorded coffee beans along with their details and creation dates.
*   **Custom Sorting:** List the beans using four different sorting methods: oldest to newest, newest to oldest, best rating to worst rating, and worst rating to best rating.
*   **Data Persistence:** Automatically stores all logs in a local SQLite database file named `database.db` with a timestamp for when the log was created.

## Project Structure

*   `main.py`: The entry point of the application that ensures the SQLite table is created before executing the main controller loop.
*   `control/bean_controller.py`: The controller that handles the logic flow, utilizing `match` statements to route user menu choices to the appropriate views and models.
*   `model/bean.py`: The data model responsible for all database queries, including executing the `CREATE TABLE` statement, inserting logs, and fetching sorted lists.
*   `model/database.py`: Contains the `Database` class that manages the connection to `database.db` and configures rows to be accessed like dictionaries.
*   `view/bean_view.py`: The view layer responsible for printing menus, handling user inputs, catching `TypeError` or out-of-range rating inputs, and formatting the console output.

## Usage

1.  Run the `main.py` file to launch the application.
2.  From the main menu, press `1` to input a new coffee bean. You will be prompted to enter a name, brewing method, and rating.
3.  Press `2` to enter the list menu, where you can press `1`, `2`, `3`, or `4` to view your log based on your preferred sorting criteria. 
4.  Press `0` at any menu to exit the application. 

**Note on Requirements:** Because `bean_controller.py` utilizes `match` and `case` statements for structural pattern matching, you must run this project using Python 3.10 or higher.