import turtle
from random import randint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, guirectangle):
        if guirectangle.point1.x <= self.x <= guirectangle.point2.x and guirectangle.point1.y <= self.y \
                <= guirectangle.point2.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):
    def pointer(self, canvas, size=5, color = 'red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


guirectangle = GuiRectangle(Point(randint(0, 200), randint(0, 200)), Point(randint(0, 200), randint(0, 200)))


print("Rectangle Coordinates :",
      guirectangle.point1.x, ",",
      guirectangle.point1.y, "and",
      guirectangle.point2.x, ',',
      guirectangle.point2.y)


guipointer = GuiPoint(float(input('Enter the X coordinates :')),
                      float(input('Enter the Y coordinates :')))

area_guess=int(input('Guess the area :'))

print("The point lies inside the rectangle :", guipointer.falls_in_rectangle(guirectangle))
print('The actual area is', abs(guirectangle.area()), 'compared to', area_guess)


myturtle = turtle.Turtle()
guirectangle.draw(canvas=myturtle)
guipointer.pointer(canvas=myturtle)
turtle.done()