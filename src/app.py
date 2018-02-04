from src import agent, exchange


def main():
    EPOCHS = 1000

    my_exchange = exchange.Exchange()
    my_agents = [agent.Agent() for _ in range(4)]

    for i in range(EPOCHS):
        for current_agent in my_agents:
            current_agent.make_order(my_exchange)



if __name__ == "__main__":
    main()