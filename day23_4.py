import turtle as T
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(T.Turtle):
    def __init__(self) -> None:
        self.All_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = T.Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-230, 230)
            new_car.goto(300, random_y)
            self.All_car.append(new_car)

    def moveing(self):
        for car in self.All_car:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        