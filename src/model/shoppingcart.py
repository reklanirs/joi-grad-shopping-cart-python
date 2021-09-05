from src.model.product import Product
from src.model.customer import Customer
from src.model.order import Order


class ShoppingCart:
    def __init__(self, customer=Customer, products=[]):
        self.products = products
        self.customer = customer

    def add_product(self, product):
        self.products.append(product)

    def checkout(self):
        
        loyalty_points_earned = 0.00
        products_buy_2_1 = [i for i in self.products if i.product_code.startswith("BULK_BUY_2_GET_1")]
        # products_dis = [i for i in self.products if i.product_code.startswith("DIS_")]


        count = dict()
        price_dict = dict()
        for product in products_buy_2_1:
            if product.name in count:
                count[product.name] += 1
            else:
                count[product.name] = 1
                price_dict[product.name] = product.price
        pass
        price_buy_2_1 = 0.0
        for product, c in count.items():
            price_buy_2_1 += (c%3)*price_dict[product] + (c//3)*2*price_dict[product]

        total_price = 0.00
        for product in self.products:
            discount = 0.00
            if product.product_code.startswith("DIS_10"):
                loyalty_points_earned += (product.price / 10)
                discount = product.price * 0.1
            elif product.product_code.startswith("DIS_15"):
                loyalty_points_earned += (product.price / 15)
                discount = product.price * 0.15
            elif product.product_code.startswith("DIS_20"):
                loyalty_points_earned += (product.price / 20)
                discount = product.price * 0.2
            else:
                loyalty_points_earned += (product.price / 5)
                discount = 0.00
            if not product.product_code.startswith("BULK_BUY_2_GET_1"):
                total_price += product.price - discount

        total_price += price_buy_2_1

        if total_price >= 500:
            total_price = total_price * 0.95
        return Order(int(loyalty_points_earned), total_price)


    def __str__(self):
        # product_list = "".join('%s'%product for product in self.products)
        count = dict()
        product_list = []
        for product in self.products:
            if product.name not in count:
                count[product.name] = 1
            else:
                count[product.name] += 1
            product_list.append( product.mystr(count[product.name]) )
        product_list = "".join(product_list)
        return "Customer: %s \nBought: \n%s" % (self.customer, product_list)
