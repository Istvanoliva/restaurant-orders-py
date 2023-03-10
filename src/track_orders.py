class TrackOrders:

    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        favorite_dish = dict()

        for order in self.orders:
            if (order[0] == customer):
                if (order[1] in favorite_dish):
                    favorite_dish[order[1]] += 1
                else:
                    favorite_dish[order[1]] = 1

        return max(favorite_dish, key=favorite_dish.get)

    def get_never_ordered_per_customer(self, customer):
        dishes = set()
        ordereds = set()

        for order in self.orders:
            dishes.add(order[1])
            if order[0] == customer:
                ordereds.add(order[1])
        return dishes.difference(ordereds)

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        served_days = set()

        for order in self.orders:
            days.add(order[2])
            if order[0] == customer:
                served_days.add(order[2])
        return days.difference(served_days)

    def get_busiest_day(self):
        days = dict()

        for order in self.orders:
            if order[2] not in days:
                days[order[2]] = 1
            else:
                days[order[2]] += 1

        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = dict()

        for order in self.orders:
            if order[2] not in days:
                days[order[2]] = 1
            else:
                days[order[2]] += 1

        return min(days, key=days.get)
