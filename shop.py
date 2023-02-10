from in_stock import products
import view

class Product:

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def show_product(self):
        return f'{self.name.title()} - {self.price} ₽ за 1 кг - {self.amount} кг'

    
def product_list(info):
    for key, val in info.items():
        current_product = Product(val["name"], val["price"], val["amount"])
        view.showinfo(f"{key}. {current_product.show_product()}")
    

def buying():
    while True:
        product_id = view.getNumb('\nЧто вы хотите купить? ')
        if not product_id in products.keys():
            view.showinfo('Такого варианта нет')
            continue
        else:
            current_product = Product(products[product_id]["name"],products[product_id]["price"],products[product_id]["amount"])
            view.showinfo(current_product.show_product())
            break
    
    product_amount = int(view.getNumb(f'Сколько килограммов {current_product.name} вы хотите купить? '))
    if product_amount > current_product.amount:
        view.showinfo(f'У нас не так много {current_product.name}. Осталось {current_product.amount} кг.')
        return None
    else:
        products[product_id]["amount"] = current_product.amount - product_amount
        return product_amount * current_product.price

def run():
    total_payment = 0

    while True:
        product_list(products)
        remains_product = buying()
        if remains_product == None:
            while True:
                davom_etish = view.getNumb('\nПродолжить?(да/нет): ')
                if davom_etish == 'нет':
                    view.showinfo(f'Ваш общий платеж составляет {total_payment} ₽.\nБлагодарим за использование нашего приложения!\n')
                    exit()
                if davom_etish == 'да':
                    break
                else:
                    view.showinfo('да или нет?')
                    continue
                
            
        else:
            total_payment += remains_product
            view.showinfo(f'Ваш текущий платеж составляет {total_payment} ₽')
            while True:
                davom_etish = view.getNumb('\nПродолжить?(да/нет): ')
                if davom_etish == 'нет':
                    view.showinfo(f'Ваш общий платеж составляет {total_payment} ₽.\nБлагодарим за использование нашего приложения!\n')
                    exit()
                if davom_etish == 'да':
                        break
                else:
                    view.showinfo('да или нет?')
                    continue
                

run()