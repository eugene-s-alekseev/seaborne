import numpy as np

from src import order


class Agent():
    def __init__(self, agent_id, X, y, asset_amount=0, balance=0):
        self.agent_id = agent_id
        self.asset_amount = asset_amount
        self.balance = balance
        self.X = X
        self.y = y


    def make_order(
            self,
            exchange_,
            amount_function=lambda old_price, new_price: (old_price-new_price)**2
    ):
        old_price, new_price = self.estimate_price(exchange_)
        order_params = {
            "owner": self,
            "order_type": "buy" if new_price > old_price else "sell",
            "price": new_price,
            "amount": amount_function(old_price, new_price),
            "exchange_": exchange_
        }
        new_order = order.Order(**order_params)

        if self.permit_order(new_order, exchange_):
            exchange_.take_order(new_order)
        else:
            print("cannot make an order")


    def permit_order(self, new_order, exchange_):
        return True


    def estimate_price(self, exchange_):
        old_price = exchange_.get_current_price()
        w1 = old_price
        w0 = exchange_.get_money_price()
        for i in range(1, 60):
            eta = 0.01 / i
            dw1 = np.sum((w1*self.X + w0 - self.y)*self.X)*2 / self.X.shape
            dw0 = np.sum(w1*self.X + w0 - self.y)*2 / self.X.shape
            w1 = w1 - eta*dw1
            w0 = w0 - eta*dw0

        exchange_.set_money_price(w0)
        return old_price, w1


    def __str__(self):
        return str(self.agent_id)


    def __repr__(self):
        return "agent"
