import tkinter as tk
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 5000
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    
    def __init__(self):
        self.bodySize = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])
            print(self.coordinates)

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)
            

class Food:
    
    def __init__(self):
        x = random.randint(0,(GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0,(GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE ,fill = FOOD_COLOR, tag="food")

def nextTurn(snake,food):
    
    x,y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0,(x,y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0,square)

    del snake.coordinates[-1]

    canvas.delete(snake.squares[-1])

    del snake.squares[-1]
    print(snake.coordinates)
    window.after(SPEED, nextTurn, snake, food)


def channgeDirection(newDirection):
    pass

def checkCollisions(snake):
    pass

def gameOver():
    pass

window= tk.Tk()
window.title("SnakeGame")
window.resizable(False,False)

score = 0
direction = 'down'

label = tk.Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

windowWidth = window.winfo_width()
windowHeight = window.winfo_height()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int(screenWidth/2 -windowWidth/2)
y = int(screenHeight/2 - windowHeight/2)

window.geometry("{}x{}+{}+{}".format(windowWidth,windowHeight,x,y))

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

nextTurn(snake, food)

window.mainloop()