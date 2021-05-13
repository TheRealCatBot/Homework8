import json
import sqlite3
import requests

API_URL = "https://jsonplaceholder.typicode.com"

response_1 = requests.get(f"{API_URL}/todos")

connection_1 = sqlite3.connect("todo.db")
cursor_1 = connection_1.cursor()

cursor_1.execute('CREATE TABLE IF NOT EXISTS todo(id INTEGER, title TEXT, userID INTEGER, completion INTEGER)')
for i in range(0, len(response_1.json())):
    cursor_1.execute('INSERT INTO todo VALUES(?,?,?,?)', (response_1.json()[i]['id'], response_1.json()[i]['title'], response_1.json()[i]['userId'], response_1.json()[i]['completed']))
cursor_1.execute('SELECT * FROM todo')
for i in cursor_1:
    print(i)

response_2 = requests.get(f"{API_URL}/users")

connection_2 = sqlite3.connect("USER.db")
cursor_2 = connection_2.cursor()
cursor_2.execute('CREATE TABLE IF NOT EXISTS USERS(address TEXT NOT NULL, company TEXT NOT NULL, email TEXT NOT NULL, id INTEGER NOT NULL, first_name TEXT NOT NULL, phone TEXT NOT NULL, username TEXT NOT NULL, website TEXT NOT NULL)')
for i in range(0, len(response_2.json())):
    address = json.dumps(response_2.json()[i]['address'])
    company = json.dumps(response_2.json()[i]['company'])
    email = json.dumps(response_2.json()[i]['email'])
    id = json.dumps(response_2.json()[i]['id'])
    firstname = json.dumps(response_2.json()[i]['name'])
    phone = json.dumps(response_2.json()[i]['phone'])
    username = json.dumps(response_2.json()[i]['username'])
    website = json.dumps(response_2.json()[i]['website'])
    cursor_2.execute('INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?)', (address,company,email,id, firstname, phone, username, website))
cursor_2.execute('SELECT * FROM USERS')
for i in cursor_2:
    print(i)

json.dumps(response_2.json()[0]['address'])
