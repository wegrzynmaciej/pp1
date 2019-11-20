def drawSquare(x, y, n, existing=None):
    if existing == None:
        import turtle
        pen = turtle.Turtle()
    else:
        pen = existing
    pen.penup()
    pen.setposition(x, y)
    pen.pendown()
    i = 0
    for i in range(4, 0, -1):
        pen.setheading(i*90)
        pen.forward(n)
    if existing == None:
        turtle.done()


def drawGrid(numrows, numcols, cellsize):
    import turtle

    pen = turtle.Turtle()

    for y in range(numrows, 0, -1):
        for x in range(numcols):
            drawSquare(x*100, y*100, cellsize, pen)
    turtle.done()
