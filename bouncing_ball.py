'''
def f1():
    x=1
    print(x)
    x=12
f1()
'''
import pygame
import random
 
BLACK = (10, 0, 0)
#MIX = (a,b,c)
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25
 
 
class Ball:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        
 
def make_ball():
    ball = Ball()
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
 
    ball.change_x = random.randrange(-7,7)
    ball.change_y = random.randrange(-7,7)
 
    return ball
 
 
def main():
    pygame.init()
 
    a=0
    b=200
    c=0
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Bouncing Balls")
 
    done = False
 
    clock = pygame.time.Clock()
    ball_colors=[(50,0,255)]
    ball_list = []
    
    ball = make_ball()
    ball_list.append(ball)
  
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Space bar! Spawn a new ball.
                if event.key == pygame.K_SPACE:
                   
                    a=random.randrange(0,255,)
                    b=random.randrange(0,255,)
                    c=random.randrange(0,255,)
                    ball = make_ball()
                    ball_list.append(ball)
                    ball_colors.append((a,b,c))
                    
        # --- Logic
        for ball in ball_list:
                     
             # Bounce the ball if needed
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1
            # Move the ball's center
            ball.x += ball.change_x
            ball.y += ball.change_y
                      
 
        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)
 
        # Draw the balls
        for ball in ball_list:
           
           ind=ball_list.index(ball)
           jack=ball_colors[ind]               
           
           pygame.draw.circle(screen,jack,[ball.x, ball.y], BALL_SIZE)
           
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()


