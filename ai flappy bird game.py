import pygame

# initialize Pygame
pygame.init()

# set the screen size
screen_width = 288
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))

# set the background color
background_color = (255, 255, 255)
screen.fill(background_color)

# load the bird sprite
bird_img = pygame.image.load("bird.png")

# load the pipe sprite
pipe_img = pygame.image.load("pipe.png")

# load the ground sprite
ground_img = pygame.image.load("ground.png")

# create the game loop
game_running = True
while game_running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # make the bird jump
                bird_y -= 50

# move the bird
bird_y += 5

# detect collisions with pipes
for pipe in pipes:
    if bird_rect.colliderect(pipe.rect):
        game_running = False

# detect collisions with the ground
if bird_rect.bottom >= ground_rect.top:
    game_running = False

# update the display
screen.blit(bird_img, (bird_x, bird_y))
for pipe in pipes:
    screen.blit(pipe_img, (pipe.x, pipe.top))
    screen.blit(pipe_img, (pipe.x, pipe.bottom))
screen.blit(ground_img, (ground_x, ground_y))
pygame.display.update()

# update the score
score += 1



