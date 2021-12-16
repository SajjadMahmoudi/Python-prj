import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(30)

col = ['yellow', 'green', 'blue', 'orange', 'white']
c = 0

for i in range(200):
    t.forward(i*5)
    t.right(150)
    t.color(col[c])
    if c == 4:
        c = 0
    else:
        c+=1
        