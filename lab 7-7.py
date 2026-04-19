# lab 7-7 / 1
import turtle as t
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)

t.done

# labl 7-7 / 2
import turtle as t

for i in range(3):
    t.forward(100)
    t.left(120)

for i in range(3):
    t.forward(200)
    t.left(120)
    
t.done

# labl 7-7 / 3
import turtle as t

for i in range(1, 4, 1):
    for j in range(3):
        t.forward(100 * i)
        t.left(120)
    
t.done

# labl 7-7 / 4
import turtle as t

for i in range(4):
    t.forward(100)
    t.left(90)

t.done
