import mysql.connector

class ProductManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vimal@sql123",
            database="shop_db"
        )
        self.cur = self.connection.cursor()
        print("Connect Successfully..!")

    def post(self,**kwargs):
        query = """
        insert into product(name,category,price,quantity,manufacture)
        values(%s%s%s%s%s)
        """
        values=(kwargs.values())
        self.cur.execute(query,values())
        self.connection.commit()
        print("column added successfully...!")

        print("product added successfully..!")
    def get(self):
        self.cur.execute("select * from product")
        for items in self.cur.fetchall():
            print(items)

    def retreive(self):
        self.cur.execute("select * from product where id=%s",id)
        print(self.cur.fetchone())
        print("retreived successfully..!")

    def get_object(self):
        self.cur.execute("Select * from product where id =%s",id)
        print(self.cur.fetchone())

    def delete(self):
        self.cur.execute("delete from product where id = %s",id)
        self.connection.commit()
        print("deleted successfully..!")


product_instance = ProductManager()
product_instance.post(name="Headphone",category="electronics",price="3000",
                      quantity=5,manufacture="realme")
product_instance.get()
product_instance.get_object()



