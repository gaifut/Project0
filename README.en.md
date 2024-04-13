[return to main Readme file](https://github.com/gaifut/Project0)

# Graphical User Interface (GUI) for order processing.

## Table of contents:
- [Definitions.](#Definitions)
- [Technology stack.](#Technology-stack)
- [Project description.](#Project-description)
- [Как скачать и запустить.](#Как-скачать-и-запустить)
- [Системные требования.](#Системные-требования)

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
- Информация должна отображаться в графическом интерфейсе.
- В интерфейсе должна быть возможность длбавить информацию по каждому заказу - продукт, кол-во.
- После этого система должна расчитать общую стоимость, основываясь на цене за 1 единицу и кол-ве.
- Информация по позициям хранится в отдельной БД и может быть добавлена/удалена оттуда.
- Измененный файл (с добавленной информацией по заказам) подгружается в базу данных SQL.
### Функционал и работа.
Проект представляет из себя 2 программы с графическим интерфейсом: основная и отдельное окно для управления продуктами. 
При запуске основной программы на экран выводится графический интефейс с кнопками. Пользователь может:
- подгружать файлы в формате csv.
- выгружать файлы в базу данных (необходимо отдельно настроить).
- вносить изменения в позиции (кол-во, продкут)
- сохранять отредактированный файл csv.

При этом при выгрузке csv файла в графический интерфейс программа связывается с API сайта Dadata и проверяет все адреса клиентов, исправляет ошибки (если они есть), в интерфейс адреса выводятся уже по единой структуре (улица, город, индекс итп).
Система автоматически расчитывает общую стоимость по каждому продукту.
Отдельное окно (программа) для управления продуктами предназначена для добавления/удаления позиций. После внесения в нее изменений основную программу необходимо перезапустить для того, чтобы изменения начали отражаться.
На раннем этапе я сделал демонстрационное видео (сейчас код несколько доработан): https://youtu.be/B2OR45Mf0x0?si=3Ctbg-WKLwAhj8Gy

## Как скачать и запустить.
1. Fork'ните этот репозиторий.
2. Клонируйте форкнутый репозиторий.
3. Советую установить виртуальное окружение, например так: ```python -m venv venv```
   и далее активируйте его: ```. venv/Scripts/activate``` (для линукса это ```. venv/bin/activate```, но данный проект реализован на Windows)
   для деактивации можно набрать ```deactivate```
   Вероятно, Windows выдаст вам ошибку про Scripts, для ее устранения:
    - Зайдите в PowerShell как администратор (наберите powershell в пуск).
    - Наберите ```set-executionpolicy remotesigned```
    - Вас попросят подтвердить это, укажите Y или Yes.
    - После этого активащия виртуального окружения должна заработать.
4. Установите зависимости из requirements.txt
   ```pip install -r requirements. txt```
5. Создайте .env файл в папке, где находится проект, в него добавьте следующие переменные (ниже указан пример с вымышленными данными):
   ```
   TOKEN=09dfsdfsfds8dsfw23SADFDFDS # (Dadata)
   SECRET=fdgfd234234asdaFG331DGGsds3 # (Dadata)
   HOST=host_name_SQL
   USER=user_name_SQL
   PASSWORD=password_SQL
   DATABASE=DB_name_SQL
   ```
   Я использовал API сервиса DaData для корректировки и работы с адресами, но можно использовать и любой другой.
6. Если вы хотите переименовать название интерфейса, в строчке 59 файла testgui-1.4.py замените "Обрабатыватель данных ГМП" на ваше название.
7. Запустите проект из файла testgui-1.4.py (в VSCode горячая клавиша запуска F5). Должно открыться окно с графическим интерфейсом. Для тестирования можно использовать csv файл Updated 3.3 qty and ppu.csv.
8. Если вы хотите добавить/удалить позиции, то запустите файл products DB.py. Должно открыться окно с графическим интерфейсом.
## Системные требования.
[Системные требования проекта](https://github.com/gaifut/Project0/blob/main/requirements.txt)
