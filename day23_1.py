import time
from turtle import Screen
from day23_2 import Player
from day23_4 import CarManager
from day23_3 import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.upward, "Up")
screen.onkey(player.downward, "Down")


score = Scoreboard()
car = CarManager()

car_count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_count += 1
    car.spawn_car()
    car.moveing()

    # # Detect collision with car
    for cars in car.All_car:
        if cars.distance(player) < 20:
            score.display_game_over()
            game_is_on = False

    # Detect Successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        score.level_up()


screen.exitonclick()
