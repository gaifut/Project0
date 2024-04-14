[return to main Readme file](https://github.com/gaifut/Project0)

# Graphical User Interface (GUI) for order processing.

## Table of contents:
- [Definitions.](#Definitions)
- [Technology stack.](#Technology-stack)
- [Project description.](#Project-description)
  - [Project goals.](#Project-goals)
  - [How it works.](#How-it-works)
- [How to download and set up.](#How-to-download-and-set-up)
- [System requirements.](#System-requirements)

## Definitions.
- GUI - graphical user interfance
- DB - database

## Technology stack:
- Python
- Windows 10 (the system in which the project was developed)
- Tkinter
- Pandas
- SQL, MySQL Server (was installed locally for the files to be sent to the DB).
- Sqlite3
- Jira (was used for planning and execution control)

## Project description.
### Project goals.
This is my pet project, made and executed by myself(my friend with experience in tech helped me with ideas for goals).
The main goal was to learn to work with new (at the time of writihng the code) libraries and areas: making graphical user interfaces, working with APIs and databases as well as to practice and broaden my knowledge of Python programming language.
Furthermore, the project was intended to be a part that could be used in future projects when improving the processes of the company I worked at (Gofromachines Premium - a supplier of heavy equipment where I was the operations manager at that time) to increase automation, reduce the number of errors and create a unified system with a single interface and logic that takes into account company's specifics.

The project pursued the following goals:
- The program should use API to check for errors in customer addresses and to have a single style and logic for all the addresses displayed in the GUI after the check.
- Information should be displayed in the GUI.
- The GUI should have an option to add/modify product and quantity information for each order.
- The system should calculate the total cost for every entry.
- Product infomration is stored in a separate DB and can be added/removed from there via a separate GUI.
- The modified file (with added order infomration) is loaded to SQL DB.
### How it works.
The project consists of 2 programs with a graphical interface: the main one and a separate window for managing products. 
When starting the main program, a graphical interface with buttons is displayed on the screen. The user can:
- upload files in csv format.
- upload files to the database (DB needs to be configured separately).
- make changes to positions (quantity, product)
- save the edited csv file.

At the same time, when uploading a csv file to the graphical interface, the program communicates with the Dadata website API and checks all client addresses, corrects errors (if any), addresses are displayed in the interface according to a single structure logic (street, city, zip code, etc.).
The system automatically calculates the total cost for each product.
A separate window (program) for managing products is designed to add/remove positions. After making changes to it, the main program must be restarted for the changes to be reflected.
I made a demo video early on (the code is now slightly improved): https://youtu.be/B2OR45Mf0x0?si=3Ctbg-WKLwAhj8Gy

## How to download and set up.
1. Clone the repository. ```git clone git@github.com:gaifut/Project0.git```
2. I recommend to install virtual inviroment, it can be done via this command for instance: ```python -m venv venv```
   then you need to activate it with: ```. venv/Scripts/activate``` (for Linux it is ```. venv/bin/activate```, but this project was created on Windows OS)
   to deactivate virtual environment use this command: ```deactivate```.
   It is possible that Windows will give you Scripts error, to fix it:
    - Run PowerShell as administrator (type powershell in the start menu to find it).
    - Enter this command: ```set-executionpolicy remotesigned```
    - Confirm it with Y or Yes once asked to.
    - After this venv activation should start working.
3. Install dependencies from requirements.txt
   ```pip install -r requirements. txt```
4. Create .env file in the same folder where the project is located add the following variables to the file (use real data instead of sample data that is provided below after = sign):
   ```
   TOKEN=09dfsdfsfds8dsfw23SADFDFDS # (Dadata)
   SECRET=fdgfd234234asdaFG331DGGsds3 # (Dadata)
   HOST=host_name_SQL
   USER=user_name_SQL
   PASSWORD=password_SQL
   DATABASE=DB_name_SQL
   ```
   I used DaData service API to adjust and work with addresses, but you can use any other one.
5. If you want to rename the interface, replace “Обрабатыватель данных ГМП” with your name in line 59 of the testgui-1.4.py file.
6. Run the project from testgui-1.4.py file (in VSCode, the run hotkey is F5) or with a termnial command ```python testgui-1.4.py```
   A window with a graphical user interface should open. For testing, you can use the csv file Updated 3.3 qty and ppu.csv.
7. If you want to add/remove positions, then run the products DB.py file. A window with a graphical user interface should open.
## System requirements.
[Project system requirements](https://github.com/gaifut/Project0/blob/main/requirements.txt)
