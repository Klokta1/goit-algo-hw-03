import turtle

def draw_koch_segment(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)
        t.right(120)
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)

def draw_koch_snowflake(t, length, level):
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)

def main():
    level = int(input("Введіть рівень рекурсії (наприклад, 3): "))

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    draw_koch_snowflake(t, 400, level)

    turtle.done()

if __name__ == "__main__":
    main()
