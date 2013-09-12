# This is where Exercise 5.6 goes
# Name:Ethan Puzarne

bob = Turtle()
bob.delay = 0.01
bob.pu()
bob.bk(150)
bob.pd()

def koch(t, length):
    """Draws a koch curve with the given width.

    Args:
        t: Turtle
        length: trunk length
    """
    if length < 3.0:
        fd(t, length)
        return
    #angle = 50
    else:
        short_length = length / 3.0
        angle = 60
        koch(t, short_length)
        lt(t, angle)
        koch(t, short_length)
        rt(t, 2*angle)
        koch(t, short_length)
        lt(t, angle)
        koch(t, short_length)

#koch(bob, 300)

def snowflake(t, length):
    for i in range(2):
        koch(t, length)
        t.rt(120)
    koch(t,length)

snowflake(bob, 100)


