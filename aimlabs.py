import pygame, sys
import random

# globals
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 600,600
BLOCK_SIZE = 100
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Aimlabs')
clock = pygame.time.Clock()

spawn_x = [125,225,325,425]
spawn_y = [125,225,325,425]
# class
class Target:
    def __init__(self):
        self.clicked = False
        self.x = random.choice(spawn_x)
        self.y = random.choice(spawn_y)
        self.x1 = random.choice(spawn_x)
        self.y1 = random.choice(spawn_y)
        self.x2 = random.choice(spawn_x)
        self.y2 = random.choice(spawn_y)
        self.surf = pygame.Surface((50,50))
        self.surf.fill((255, 196, 0))
        self.rect = self.surf.get_rect(center = (self.x, self.y))
        self.rect1 = self.surf.get_rect(center = (self.x1, self.y1))
        self.rect2 = self.surf.get_rect(center = (self.x2, self.y2))
        self.target_list = [self.rect, self.rect1, self.rect2]

    def new_pos(self):
        self.x = random.choice(spawn_x)
        self.y = random.choice(spawn_y)
        self.rect = self.surf.get_rect(center = (self.x, self.y))
        return(self.x,self.y)

    def new_pos1(self):
        self.x1 = random.choice(spawn_x)
        self.y1 = random.choice(spawn_y)
        self.rect1 = self.surf.get_rect(center = (self.x1, self.y1))
        return(self.x1,self.y1)

    def new_pos2(self):
        self.x2 = random.choice(spawn_x)
        self.y2 = random.choice(spawn_y)
        self.rect2 = self.surf.get_rect(center = (self.x2, self.y2))
        return(self.x2,self.y2)

    def check_overlap(self):
        pass

    def draw(self):
        screen.blit(self.surf, self.rect)
        screen.blit(self.surf, self.rect1)
        screen.blit(self.surf, self.rect2)
        self.check_overlap()

# class 
target = Target()

# pregame collision check
new_pos = target.rect.center
if target.rect1.collidepoint(new_pos) or target.rect2.collidepoint(new_pos):
    target.new_pos()

new_pos = target.rect1.center
if target.rect.collidepoint(new_pos) or target.rect2.collidepoint(new_pos):
    target.new_pos1()

new_pos = target.rect2.center
if target.rect.collidepoint(new_pos) or target.rect1.collidepoint(new_pos):
    target.new_pos2()

# score
FONT = pygame.font.Font('freesansbold.ttf', 30)
score = 0
mouse_clicks = 1
hits = 0
score_surf = FONT.render('1', True, 'white')
score_rect = score_surf.get_rect(topleft = (50, SCREEN_HEIGHT/50))
accuracy_surf = FONT.render('1', True, 'white')
accuracy_rect = accuracy_surf.get_rect(topleft = (350, SCREEN_HEIGHT/50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # target 1
            if target.rect.collidepoint(mouse_pos):
                new_pos = target.new_pos()
                score += 500
                mouse_clicks += 1
                hits += 1
                if target.rect1.collidepoint(new_pos) or target.rect2.collidepoint(new_pos):
                    target.new_pos()
            # target 2
            if target.rect1.collidepoint(mouse_pos):
                new_pos = target.new_pos1()
                score += 500
                mouse_clicks += 1
                hits += 1
                if target.rect.collidepoint(new_pos) or target.rect2.collidepoint(new_pos):
                    target.new_pos1()
            # target 3
            if target.rect2.collidepoint(mouse_pos):
                new_pos = target.new_pos2()
                score += 500
                mouse_clicks += 1
                hits += 1
                if target.rect.collidepoint(new_pos) or target.rect1.collidepoint(new_pos):
                    target.new_pos2()
            
            elif  not target.rect.collidepoint(mouse_pos) or not target.rect1.collidepoint(mouse_pos) or not target.rect2.collidepoint(mouse_pos):
                score -= 200
                mouse_clicks += 1
                    

    screen.fill((0, 0, 25))

    # score 
    score_surf = FONT.render(f'Score:{score}', True, 'white')
    accuracy_surf = FONT.render(f'Accuracy:{round(hits/mouse_clicks*100)}%', True, 'white')
    screen.blit(score_surf, score_rect)
    screen.blit(accuracy_surf,accuracy_rect)
    # draw target
    target.draw()
    
    pygame.display.update()
    clock.tick(60)
    