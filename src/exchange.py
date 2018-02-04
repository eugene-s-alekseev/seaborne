from src.book import BuyBook, SellBook


class Exchange():
    def  __init__(self):
        self.buy = BuyBook()
        self.sell = SellBook()
        self.current_price = self.buy.get_current_price()
        self.money_price = 0

    def take_order(self, new_order):
        if new_order.order_type == "buy":
            self.buy.take_order(new_order)
            self.execute()
        elif new_order.order_type == "sell":
            self.sell.take_order(new_order)
            self.execute()
        else:
            raise ValueError("order_type must be either buy or sell not {order_type}".format(order_type=new_order.order_type))

    def get_current_price(self):
        return self.current_price

    def set_current_price(self, current_price):
        self.current_price = current_price

    def get_money_price(self):
        return self.money_price

    def set_money_price(self, money_price):
        self.money_price = money_price

    def execute(self):
        if len(self.buy.book) > 0 and len(self.sell.book) > 0:
            if self.buy.book[-1] >= self.sell.book[0]:
                sell_order = self.sell.get_top_order()
                self.set_current_price(sell_order.price)
                self.buy.book[-1].amount -= sell_order.amount
                buy_order_owner = self.buy.book[-1].owner
                buy_order_owner.balance = sell_order.amount * sell_order.price
                sell_order_owner = sell_order.owner
                sell_order_owner.balance = sell_order.amount * sell_order.price
                self.execute()
            else:
                buy_order = self.buy.get_top_order()
                self.set_current_price(buy_order.price)
                self.sell.book[0].amount -= buy_order.amount
                sell_order_owner = self.sell.book[0].owner
                sell_order_owner.balance = buy_order.amount * buy_order.price
                buy_order_owner = buy_order.owner
                buy_order_owner.balance = buy_order.amount * buy_order.price
                self.execute()

    def __str__(self):
        return "exchange"

    def __repr__(self):
        return "Buy: " + "\n\n" + str(self.buy) + "\n\n" + "Sell: " + "\n\n" + str(self.sell)