import psycopg2 



# def run_db(query):
#     HOSTNAME = '127.0.0.1'
#     USERNAME = 'postgres'
#     PASSWORD = 'data123'
#     DATABASE = 'Restaurant Menu Manager'

#     connection = p.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

#     cursor = connection.cursor()
#     cursor.execute(query)
#     connection.commit()
#     results = cursor.fetchall()
#     connection.close()
#     return results



class MenuItem():
    def __init__(self, item, price):
        self.item = item
        self.price = price

   

        
    def save(self):
        query = f"INSERT INTO menu (item, price) values ('{self.item}', '{self.price}')"
        return run_db(query)

    def update(self):
        new_price = int(input('enter new price'))
        query = f"UPDATE menu SET price = {new_price} where name = '{item}';"
        return run_db(query)

    
    def delete(self):
        query = f"DELETE from menu where name = '{self.item};"
        return run_db(query)

    @classmethod
    def all(cls):
        query = "select * from menu;"
        cursor.execute(query)
        results = cls.cursor.fetchall()
        for line in results:
            print(f"item: {line[1]} price: {line[2]}")

    @staticmethod
    def run_db(query):
        HOSTNAME = '127.0.0.1'
        USERNAME = 'postgres'
        PASSWORD = ''
        DATABASE = 'Restaurant Menu Manager'

        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        results = cursor.fetchall()
        connection.close()
        return results



choice = MenuItem('Burger', 37)
choice.run_db()
choice.save()
choice.delete()
choice.update('Veggie Burger', 37)
item2 = MenuItem.get_by_name('Beef Stew')
items = MenuItem.all()








   




