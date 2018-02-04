from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

import src.agent as agent
import src.exchange as exchange
import src.order as order


def main():
    data = load_boston()
    X = data.data[:, :1]
    y = data.target

    exchange_ = exchange.Exchange()
    agent_ = agent.Agent(0, X.squeeze(), y)
    order_ = order.Order(owner=agent_, order_type="sell", price=3, amount=1, exchange_=exchange_)
    for _ in range(100):
        agent_.make_order(exchange_)

    print(repr(exchange_))
    print("money: ", str(exchange_.money_price))
    print("current_price: ", str(exchange_.current_price))

    lr = LinearRegression()
    lr.fit(X, y)
    print(lr.intercept_, lr.coef_)

if __name__ == "__main__":
    main()