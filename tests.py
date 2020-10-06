import pygame
import random as rd
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 600
score = 0 
# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    
    def update(self,pressed_keys):
        if pressed_keys[K_UP] and self.rect.y > 0:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN] and self.rect.y <SCREEN_HEIGHT-self.rect.height:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]and self.rect.x > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]and self.rect.x <SCREEN_WIDTH-self.rect.width:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Enemy,self).__init__()
        self.surf = pygame.Surface((20,10))
        self.surf.fill((255,0,0))
        self.side =rd.choice([-1,1])
        if self.side == -1:
            self.center_x = rd.randint(SCREEN_WIDTH+20,SCREEN_WIDTH+100)
        else:
            self.center_x = rd.randint(-100,-20)

        
        self.speed = self.side * rd.randint(5,15)
        self.rect = self.surf.get_rect(center = (self.center_x,rd.randint(0,SCREEN_HEIGHT)))

    def update(self):
        self.rect.move_ip(self.speed,0)
        if (self.rect.right < 0 and self.side == -1) or (self.rect.left > SCREEN_WIDTH and self.side == 1):
            global score
            score+=abs(self.speed)
            self.kill()

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable to keep the main loop running
running = True

# Main loop
while running:
    pygame.time.delay(5)
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
                # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
        
        
    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    # Update enemy position
    enemies.update()
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False

    # Update the display
    pygame.display.flip()
print(score)