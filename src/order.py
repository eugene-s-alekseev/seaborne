class Order():
    def __init__(self, owner, order_type, price, amount, exchange_):
        self.owner = owner
        self.order_type = order_type
        self.price = price
        self.amount = amount
        self.exchange_ = exchange_


    def __gt__(self, other):
        return self.price > other.price


    def __ge__(self, other):
        return self.price >= other.price


    def __ne__(self, other):
        return self.price != other.price


    def __eq__(self, other):
        return self.price == other.price


    def __le__(self, other):
        return self.price <= other.price


    def __lt__(self, other):
        return self.price < other.price


    def __str__(self):
        rep = "owner: {owner}  order_type: {order_type}  price: {price}  amount: {amount}  exchange: {exchange}"
        rep = rep.format(
            owner=str(self.owner),
            order_type=str(self.order_type),
            price=str(self.price),
            amount=str(self.amount),
            exchange=str(self.exchange_)
        )
        return rep


    def __repr__(self):
        rep = "owner: {owner}  order_type: {order_type}  price: {price}  amount: {amount}  exchange: {exchange}"
        rep = rep.format(
            owner=str(self.owner),
            order_type=str(self.order_type),
            price=str(self.price),
            amount=str(self.amount),
            exchange=str(self.exchange_)
        )
        return rep


