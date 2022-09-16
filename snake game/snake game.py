# importing
import pygame, sys
import random

# initializing
pygame.init()
# globals
SCREEN_WIDTH, SCREEN_HEIGHT = 680,680
BLOCK_SIZE = 40
# basic setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
# classes
class Snake:
    def __init__(self):
        # attributes
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x,self.y,BLOCK_SIZE,BLOCK_SIZE)
        self.body = [pygame.Rect(self.x-BLOCK_SIZE,self.y,BLOCK_SIZE,BLOCK_SIZE)]
        self.dead = False

    def update(self):
        global apple
        # collision
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0,SCREEN_WIDTH) or self.head.y not in range(0, SCREEN_HEIGHT):
                self.dead = True
            
        if self.dead:
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.xdir = 1
            self.ydir = 0
            self.head = pygame.Rect(self.x,self.y,BLOCK_SIZE,BLOCK_SIZE)
            self.body = [pygame.Rect(self.x-BLOCK_SIZE,self.y,BLOCK_SIZE,BLOCK_SIZE)]
            self.dead = False
            apple = Apple()
        # creating the snake
        self.body.append(self.head) # <-- the for loop runs until the second last square 
                                    #so we append the head so that it also works on the square before the head
        for i in range(0,len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body [i+1].x, self.body[i+1].y
            
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head) # remove the head after the for loops is completed
class Apple:
    def __init__(self):
        # attributes
        self.x = int(random.randint(0, SCREEN_WIDTH)/BLOCK_SIZE) *BLOCK_SIZE 
        self.y = int(random.randint(0, SCREEN_HEIGHT)/BLOCK_SIZE) *BLOCK_SIZE 
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):
        pygame.draw.rect(screen, (125, 7, 2), self.rect)

# creating grid 
def drawGrid():
    # nested loops
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x,y,BLOCK_SIZE,BLOCK_SIZE)
            pygame.draw.rect(screen, (38, 38, 38), rect, 1)
# score
FONT = pygame.font.Font('font.ttf',75)
score = FONT.render('1', True, 'white')
score_rect = score.get_rect(midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT/60))
# classes
snake = Snake()
apple = Apple()

# game loop
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            snake.ydir = 1
            snake.xdir = 0
        elif event.key == pygame.K_UP:
            snake.ydir = -1
            snake.xdir = 0
        elif event.key == pygame.K_RIGHT:
            snake.ydir = 0
            snake.xdir = 1
        if event.key == pygame.K_LEFT:
            snake.ydir = 0
            snake.xdir = -1
    
    # draw
    screen.fill((0,0,0))
    drawGrid()

    # update
    snake.update()
    apple.update()
    
    # score
    score = FONT.render(f'{len(snake.body) - 1}', True, 'white')

    # draw snake
    pygame.draw.rect(screen, (0, 120, 7), snake.head)
    for square in snake.body:
        pygame.draw.rect(screen, (0, 120, 7), square)

    # draw score
    screen.blit(score,score_rect)

    # eating logic
    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x,square.y,BLOCK_SIZE,BLOCK_SIZE))
        apple = Apple()

    pygame.display.update()
    clock.tick(10)