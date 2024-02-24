from tkinter import *
import tkinter.messagebox as tmsg
import random

root = Tk()

root.title("Snake Game")
root.geometry("600x639")
root.resizable(False, False)
root.config(bg="Deep pink")

# Score Showing

Score = 0
f1 = Frame(root).grid()
s = Label(f1, text=f"Score = {Score}", font="Algerian 20", bg="deep Pink").grid(row=0, column=0)

Game_screen = Canvas(root, height=600, width=600, bg="Chartreuse")
Game_screen.grid(row=1, column=0)

Snake_x_cord = 0
Snake_y_cord = 0
snake_length = 3
Snake_pos = [[0, 0]]
body_parts = []


def Snake(Snake_x_cord, Snake_y_cord):
    snake = Game_screen.create_rectangle(Snake_x_cord, Snake_y_cord, Snake_x_cord + 20, Snake_y_cord + 20,
                                         fill="yellow")
    body_parts.append(snake)


Food_x_cord = 0
Food_y_cord = 0
food = Game_screen


def Food():
    global Food_x_cord
    global Food_y_cord
    Food_x_cord = (random.randint(1, 29)) * 20
    Food_y_cord = (random.randint(1, 29)) * 20

    food = Game_screen.create_oval(Food_x_cord, Food_y_cord, Food_x_cord + 20, Food_y_cord + 20, fill="red",
                                   tag="Khana")


def Collision():
    collision_test = Snake_pos.copy()
    collision_test.remove([Snake_x_cord, Snake_y_cord])

    if Snake_x_cord > 580 or Snake_y_cord > 580 or Snake_x_cord < 0 or Snake_y_cord < 0:
        return True
    elif [Snake_x_cord, Snake_y_cord] in collision_test:
        return True
    else:
        return False


Direc = "Right"


def Turning(event, new_direc):
    global Direc

    if new_direc == "Left":
        if Direc != "Right":
            Direc = new_direc
    elif new_direc == "Right":
        if Direc != "Left":
            Direc = new_direc
    elif new_direc == "Up":
        if Direc != "Down":
            Direc = new_direc
    elif new_direc == "Down":
        if Direc != "Up":
            Direc = new_direc


def Movement():
    global Snake_x_cord, Snake_y_cord, Score, snake_length

    if Direc == "Right":
        Snake_x_cord += 20
        Snake(Snake_x_cord, Snake_y_cord)
    elif Direc == "Up":
        Snake_y_cord -= 20
        Snake(Snake_x_cord, Snake_y_cord)
    elif Direc == "Down":
        Snake_y_cord += 20
        Snake(Snake_x_cord, Snake_y_cord)
    elif Direc == "Left":
        Snake_x_cord -= 20
        Snake(Snake_x_cord, Snake_y_cord)

    Snake_pos.append([Snake_x_cord, Snake_y_cord])
    # print(Snake_pos)

    if len(Snake_pos) >= snake_length:

        # Game_screen.delete(*Snake_pos[3], list(map(lambda x: x+20, Snake_pos[3])))
        for i in range(len(body_parts) - snake_length):
            Game_screen.delete(body_parts[i])
            del body_parts[i]
            Snake_pos.remove(Snake_pos[i])

    if Eating():
        Game_screen.delete("Khana")
        Score += 1
        snake_length += 1
        s = Label(f1, text=f"Score = {Score}", font="Algerian 20", bg="deep pink").grid(row=0, column=0)
        Food()

    if not Collision():
        Game_screen.after(100, Movement)
    else:
        Game_Over()


def Eating():
    if Snake_x_cord == Food_x_cord and Snake_y_cord == Food_y_cord:
        return True


root.bind("<Left>", lambda event: Turning(event, "Left"))
root.bind("<Right>", lambda event: Turning(event, "Right"))
root.bind("<Up>", lambda event: Turning(event, "Up"))
root.bind("<Down>", lambda event: Turning(event, "Down"))

Food()
Snake(Snake_x_cord, Snake_y_cord)
Movement()


def Game_Over():
    wigdet_list = root.winfo_children()
    for item in wigdet_list:
        item.destroy()
    root.geometry("400x200")
    Label(text="GAME OVER", font="Algerian 32 bold", fg="gold", bg="DodgerBlue2").pack()
    Label(text=f"Your Score is {Score}", font="Algerian 32 bold", fg="gold", bg="DodgerBlue2").pack()
    msg = tmsg.askyesno("LOL", "Don't worry my friend losing is not new for you."
                               "After this shameful score do you want to play again !!!")
    if msg:
        ok = tmsg.showinfo("LOL", "You dont deserve another chance")
        if ok == "ok":
            exit()


root.mainloop()
