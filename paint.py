class Paint:
    def __init__(self, bucket, color):
        self.bucket = bucket
        self.color = color

    def total_price(self):
        if self.color=='white':
            return self.bucket*1.99
        else:
            return self.bucket*2.19


class House:
    def __init__(self, wall_area):
        self.wall_area = wall_area

    def paint_needed(self):
        return self.wall_area * 2.5


class DiscountedPrice(Paint):
    def discounted_price(self, discount_percentage):
        price = self.total_price()
        discount = price * discount_percentage /100
        return price - discount

