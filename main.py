import pygame
import random
pygame.init()

# Game window
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load(r"images/icon.ico"))
width, height = 850, 650
screen = pygame.display.set_mode((width, height))
background_png = pygame.image.load(r"images/background.png")
font = pygame.font.Font(r"font.ttf", 20)
gameover_font = pygame.font.Font(r"font.ttf", 64)

# Creating the player
player_png = pygame.image.load(r"images/player.png")
player_positionX = (width/2)-32
player_positionY = 562
def player(x : int, y : int):
    '''Takes the integer coordinates of the player and draws the player png in those coordinates'''
    screen.blit(player_png, (x, y))

# Creating the laser shot
laser_png = pygame.image.load(r"images/laser.png")
laser_positionY = player_positionY-32+2  # Using +2 so that laser shoots right out of the canon
fired = False
def laser(x : int, y : int):
    '''Takes the integer coordinates of the laser and draws the laser png in those coordinates'''
    screen.blit(laser_png, (x, y))

# Creating the enemies
enemy_png = pygame.image.load(r"images/enemy.png")
enemy_positionX = []
enemy_positionY = []
enemyX_change = []
num_enemies = 6
for i in range(num_enemies):
    enemy_positionX.append(random.randint(0, width-64))
    enemy_positionY.append(random.choice([50, 114, 178]))
    enemyX_change.append(1)
def enemy(x : int, y : int):
    '''Takes the integer coordinates of the enemy and draws the enemy png in those coordinates'''
    screen.blit(enemy_png, (x, y))

# Progress
score = 0
lap = 0
difficulty = 0

try:
    saved_high_score = open(r"high_score.txt", "r")
    high_score = int(saved_high_score.read())
    saved_high_score.close()
except:
    high_score = 0

def progress():
    '''Displays the progress of the game'''
    text_color = (0, 255, 255)
    screen.blit(font.render("Score: " + str(score), True, text_color), (9, 9))
    screen.blit(font.render("Laps: " + str(lap), True, text_color), (378, 9))
    global high_score
    if score > high_score:
        high_score = score
    screen.blit(font.render("High Score: " + str(high_score), True, text_color), (644, 9))

# Audio
pygame.mixer.music.load(r"audio/music.mp3")
pygame.mixer.music.play(-1)
laser_mp3 = pygame.mixer.Sound(r"audio/laser.mp3")
hit_mp3 = pygame.mixer.Sound(r"audio/hit.mp3")
death_mp3 = pygame.mixer.Sound(r"audio/death.mp3")

# Game loop
running = True
paused = False
while running:
    for event in pygame.event.get():
        # Quits the game
        if event.type == pygame.QUIT:
            saved_high_score = open(r"high_score.txt", "w")
            saved_high_score.write(str(high_score))
            saved_high_score.close()
            running = False
    
    # Pauses the game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if not paused:
                paused = True
            else:
                paused = False
                pygame.mixer.music.unpause()
    if paused:
        screen.blit(font.render("Paused", True, (255, 255, 255)), (378, 312))
        pygame.display.update()
        pygame.mixer.music.pause()
        continue

    # Background
    screen.fill((0, 0, 0))
    screen.blit(background_png, (0, 0))

    # Positions the player
    keys = pygame.key.get_pressed()
    player(player_positionX, player_positionY)
    if keys[pygame.K_RIGHT] and player_positionX < width-64:
        player_positionX += 2+difficulty
    if keys[pygame.K_LEFT] and player_positionX > 0:
        player_positionX -= 2+difficulty

    for i in range(num_enemies):
        # Game over
        enemy_rectangle = pygame.Rect(enemy_positionX[i], enemy_positionY[i], 64, 64)
        player_rectangle = pygame.Rect(player_positionX, player_positionY, 64, 64)
        if enemy_rectangle.colliderect(player_rectangle):
            death_mp3.play()
            saved_high_score = open(r"high_score.txt", "w")
            saved_high_score.write(str(high_score))
            saved_high_score.close()
            screen.blit(background_png, (0, 0))
            screen.blit(gameover_font.render("Game Over!", True, (255, 0, 0)), (210, 266))
            screen.blit(font.render("Press ENTER to play again.", True, (255, 255, 255)), (255, 339))
            progress()
            pygame.display.update()
            pygame.mixer.music.stop()
            game_over = True

            while game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        game_over = False

                    # Playing again
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        player_positionX = (width/2)-32
                        laser_positionY = player_positionY-32+2
                        fired = False
                        enemy_positionX = []
                        enemy_positionY = []
                        enemyX_change = []
                        for i in range(num_enemies):
                            enemy_positionX.append(random.randint(0, width-64))
                            enemy_positionY.append(random.choice([50, 114, 178]))
                            enemyX_change.append(1)
                        score = 0
                        lap = 0
                        difficulty = 0
                        pygame.mixer.music.play(-1)
                        game_over = False

            if not running:
                continue

        # Positions the enemy
        enemy(enemy_positionX[i], enemy_positionY[i])
        if enemy_positionX[i] >= width-64:
            enemyX_change[i] = -(1+difficulty)
            enemy_positionY[i] += 64
        elif enemy_positionX[i] <= 0:
            enemyX_change[i] = 1+difficulty
            enemy_positionY[i] += 64
        enemy_positionX[i] += enemyX_change[i]

    # Fires the laser
    if keys[pygame.K_SPACE]:
        if not fired:
            laser_mp3.play()
            laser_positionX = player_positionX+29
            fired = True
    if fired and laser_positionY > -32:
        laser(laser_positionX, laser_positionY)
        
        # Hit detection
        for i in range(num_enemies):
            enemy_rectangle = pygame.Rect(enemy_positionX[i], enemy_positionY[i], 64, 64)
            laser_rectangle = pygame.Rect(laser_positionX, laser_positionY, 6, 32)
            if enemy_rectangle.colliderect(laser_rectangle):
                hit_mp3.play()
                fired = False
                laser_positionY = player_positionY-32+2
                score += 1
                if score != 0 and score % num_enemies == 0:
                    lap += 1
                    difficulty += 0.5
                enemy_positionX[i] = random.randint(0, width-64)
                enemy_positionY[i] = random.choice([50, 114, 178])
                enemyX_change[i] = 1+difficulty
        
        laser_positionY -= 2+difficulty
    else:
        fired = False
        laser_positionY = player_positionY-32+2

    # Displays the score and lap
    progress()

    pygame.display.update()