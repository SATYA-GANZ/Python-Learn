# konsep advance encapsulation,method magic,dunder,gennerator,decorator dan lainya
import datetime
class product:
    #type hint expect to return None as default
    def __init__(self,product:dict):
        self._name = product.get('name')
        self._quantity = product.get('quantity')
        self._expired = product.get('expired')
        self._id = product.get('id')
    
    def __str__(self):
        return f"information about this product\nName : {self._name}\nQuantity : {self._quantity}\nexpired date {self._expired}\nproduct Id : {self._id}"
    
     # for getter
    @property
    def name(self):
         return self._name
         
    @property
    def quantity(self):
        return self._quantity
                
    @property
    def id(self):
       return self._id
       
   # @name.setter
   # def name(self,value):
       #  if not isinstance(value,str):
            # raise ValueError("name must be a string or nothing")
     #    self._name = value

class Gudang:
    def __init__(self):
        self._products = {}
        self._import = []
        self._export = []
        self._history = []
        
    #getter
    @property
    def history(self):
      return self._history
      
      # wrapper
    def log_add(func):
       from datetime import datetime
       def wrapper(self, produk):
            logger = func(self,produk)
            log_entry = {
                'timestamp': datetime.now(),
                'action': 'add',
                'product_info': {
                    'name': product.name,
                    'quantity': product.quantity,
                    'id': product.id
                }
            }
            self._history.append(log_entry)
            print(f"product add success")
            return logger
       return wrapper
    # wrapper implementation
    
    @log_add
    def add_product(self,produk):
        if isinstance(produk,product):
            barang = produk
        elif isinstance(produk,dict):
            barang = product(produk)
        self._products[barang._name] = barang
     
    def input_product(self):
        try:
            print("Add Product Program")
            name = input("masukkan nama prorduk")
            quantity = int(input("masukkan jumlah barang"))
            expired = int(input("masukkan tahun kadaluarsa"))
            id = int(input("masukkan id product"))
            
            product_data = {
                'name': name,
                'quantity': quantity,
                'expired': expired,
                'id': id
            }

            new_product = product(product_data)
            self.add_product(new_product)
        finally:
            pass
            
    def remove_product(self,name):
        if name in self._products:
            removed_product = self._products.pop(name)
            self._history.append(removed_product)
        
    def list_product(self):
        for prodak in self._products.values():
            print(f"{prodak}")
            
    def history_generator(self):
           for entry in self._history:
            timestamp = entry['timestamp']
            action = entry['action']
            product_info = entry['product_info']
            
            # Format yang lebih mudah dibaca
            yield (
                f"\nTransaction Time: {timestamp}\n"
                f"Action: {action}\n"
                f"Product Name: {product_info['name']}\n"
                f"Quantity: {product_info['quantity']}\n"
                f"ID: {product_info['id']}\n"
                f"{'-' * 40}"
            )
                 
    
            
def main():
    all_one = {
        'name':'pji',
        'quantity':10,
        "expired":2024,
        "id":10
        }
        
    sabun = product(all_one)
        
    gudang = Gudang()       
        
    print("1. memasukkan barang baru\n2. remove barang dari gudang\n3. check log barang masuk dan keluar\n4. list barang gudang")
    menu = int(input("1-4 : "))
    match menu:
           case 1:
               gudang.input_product()
               print("\n=== Transaction History ===")
               history_exists = False
               for log in gudang.history_generator():
                 history_exists = True
                 print(log)
                 back = input("back to mein manu? y/n")
                
               if back == "y":
                    main()
               else:
                    exit()
           case 2:
                barangs = input("masukkan nama barang yang ingin dihapus")
                gudang.remove_product(barangs)
                gudang.list_product(),
           case 3:
             print("\n=== Transaction History ===")
             history_exists = False
             for log in gudang.history_generator():
               history_exists = True
               print(log),
           case 4:
                gudang.list_product()
       
def login():
    username = "ahmad"
    password = "123"
    
    print("Aplikasi Pergudangan Admin")
    print("masukkan username dan passowrd")
    user = input("username : ")
    pw = str(input("password : "))
    
    if user == username and password == pw:
        main()
    else:
       print("salah nyet")


if __name__ == "__main__":
    login()
