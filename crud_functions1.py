import sqlite3

def initiate_db():
     connection = sqlite3.connect("base_module_14.4.db")
     cursor = connection.cursor()

     cursor.execute('''
     CREATE TABLE IF NOT EXISTS Products(
     id INTEGER PRIMARY KEY,
     title TEXT NOT NULL,
     description TEXT,
     price INTEGER NOT NULL
     )
     ''')

     cursor.execute("CREATE INDEX IF NOT EXISTS idx_id ON Products(id)")

     # Наполнение базы продуктами
     # for i in range(1, 5):
     #     cursor.execute("INSERT INTO Products(title, description, price) VALUES (?, ?, ?)",
     #                    (f"Волшебный продукт {i}", f"Витамины {i} для Вас", f"{i*1000}"))
     #connection.commit()

     connection = sqlite3.connect("base_module_14.5.db")
     cursor = connection.cursor()

     cursor.execute('''
     CREATE TABLE IF NOT EXISTS Users(
     id INTEGER PRIMARY KEY,
     username TEXT NOT NULL,
     email TEXT NOT NULL,
     age INTEGER NOT NULL,
     balance INTEGER NOT NULL
     )
     ''')

     cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")

     connection.commit()
     connection.close()


#get_all_products возвращает все записи из таблицы Products
def get_all_products():
     connection = sqlite3.connect("base_module_14.4.db")
     cursor = connection.cursor()
     products = cursor.execute('SELECT * FROM Products').fetchall()
     connection.commit()
     connection.close()
     return products

def is_included(username):
     connection = sqlite3.connect("base_module_14.5.db")
     cursor = connection.cursor()
     cursor.execute('SELECT * FROM Users WHERE username = ?;',(username, ))
     user = cursor.fetchone()
     connection.commit()
     connection.close()
     return bool(user)


# add_user принимает имя пользователя, почту и возраст и добавляет в таблицу Users данные
def add_user(username, email, age):
     connection = sqlite3.connect("base_module_14.5.db")
     cursor = connection.cursor()
     if not is_included(username):
          cursor.execute("INSERT INTO Users (username, email, age, balance) "
                   "VALUES (?, ?, ?, ?)", (username, email, age, "1000"))
     connection.commit()
     connection.close()

