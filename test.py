from graphics import *



def loop(win):
    for i in range(100):
        c = Circle(Point(i*5,100), 2)
        c.draw(win)
        update(2)

def main():
    win = GraphWin("Window", 500, 500, autoflush=False)
    win.setBackground(color_rgb(255,255,255))
    loop(win)
    win.close()
    win.getMouse()

main()