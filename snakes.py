import pygame
import random

pygame.mixer.init()




pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

img2 = pygame.image.load("bg2.jpg")
img2 = pygame.transform.scale(img2, (screen_width,screen_height)).convert_alpha()

img = pygame.image.load("bg.jpg")
img = pygame.transform.scale(img, (screen_width,screen_height)).convert_alpha()


# Game Title
pygame.display.set_caption("Snakes By Maneesh")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 55, bold=True)
Font = pygame.font.SysFont("comicsansms", 30)
FONT =  pygame.font.SysFont("comicsansms", 50)
fps = 30

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(img, (0,0))
        text_screen("Welcome to Snakes",black,180,250)
        text_screen2("Created By Maneesh...",(128, 0, 128),320,330)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("background.mp3")
                    pygame.mixer.music.play()
                    gameloop()
            
        pygame.display.update()
        clock.tick(fps)
        

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
    
def text_screen2(text, color, x, y):
    screen_text = Font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
    
def text_screen3(text, color, x, y):
    screen_text = FONT.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width / 1.2)
    food_y = random.randint(40, screen_height / 1.2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    while not exit_game:
        if game_over:
            gameWindow.fill(black)
            text_screen3("Game Over! Press Enter To Continue...", red, 0, 250)
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<20:
                score +=1
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5

            gameWindow.fill(white)
            gameWindow.blit(img2, (0,0))
            
            text_screen("Score: " + str(score * 10), black, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("explosion.mp3")
                pygame.mixer.music.play()


            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("explosion.mp3")
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
    
welcome()
gameloop()

