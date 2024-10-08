class Produkt:
    def __init__(self,name:str,weight:float,category:str):
        self.name = name # название товара
        self.weight = weight # общий вес товара
        self.category = category # категория товара

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
     __file_name = 'products.txt' # файл с нозванием продуктов

     def get_products(self):
         file = open(self.__file_name,'r')
         tx = file.read()
         file.close()
         return tx

     def add(self,*products):
        current_produkts = self.get_products()

        for product in products:
              if str(product) not in current_produkts:
                  file = open(self.__file_name,'a')
                  file.write(str(product) +'\n')# запись в файл
                  current_produkts += (str(product)+ '\n')
                  file.close()
              else:
                  print(f'Продукт {product} уже есть в магазине')


s1 = Shop()
p1 = Produkt('Potato',50.0,'Vegetables')
p2 = Produkt('Spaghetti',3.4,'Groceries')
p3 = Produkt('Potato',5.5,'Vegetables')

print(p2) # __str__
s1.add(p1,p2,p3)

print(s1.get_products())
