import pgzrun
import random

TITLE = "Flappy ball"
WIDTH = 600
HEIGHT = 600
GRAVITY = 2000

class Ball:
    #properties
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        self.radius = radius
        self.color = (R,G,B)
        self.vx = 100
        self.vy = 0
    #function
    def draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,self.color)
#
#objects
balle = Ball(100,20,15)
def draw ():
    screen.clear()
    balle.draw()

def update(dt):
    # Apply constant acceleration formulae
    uy = balle.vy # uy = current vertical velocity of balle
    balle.vy += GRAVITY * dt #(v=u+at) ball's vertical velocity increases due to the acc. of gravity
    balle.y += (uy + balle.vy) * 0.5 * dt #(s = ut + 1/2 at^2)  - calculate avg. velocity over the time interval dt

    # detect and handle bounce
    if balle.y > HEIGHT - balle.radius:  # we've bounced!
        balle.y = HEIGHT - balle.radius  # fix the position
        balle.vy = -balle.vy * 0.9  # inelastic collision
    # X component doesn't have acceleration
    balle.x += balle.vx * dt
    if balle.x > WIDTH - balle.radius or balle.x < balle.radius:
        balle.vx = -balle.vx

def on_key_down(key):
    """Pressing a key will kick the ball upwards."""
    if key == keys.SPACE:
        balle.vy = -500

pgzrun.go()





