import pygame
from pygame import image, transform

BACKGROUND_COLOR = (0, 0, 0)

WIDTH = 1200
HEIGHT = 600

FPS = 60

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

playr_color = (0, 128, 255)
playr_x = 0
playr_width = 50
playr_height = 50
playr_y = HEIGHT - playr_height
playr_speed = 5

jump = False

gravity = 1
jump_streng = -15

start_jump = 0
grond_y = HEIGHT - playr_height

running = True

background = transform.scale(image.load("Fon.png"), (WIDTH, HEIGHT))
player_skin = transform.scale(image.load("Character.png"), (playr_width, playr_height))

def reset_player():
    global playr_x, playr_y, jump, start_jump
    playr_x = 0  
    playr_y = HEIGHT - playr_height  
    jump = False
    start_jump = 0

def draw_menu():
    font = pygame.font.Font(None, 74)
    text_start = font.render("Start", True, (255, 255, 255))
    text_exit = font.render("Exit", True, (255, 255, 255))

    start_rect = text_start.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    exit_rect = text_exit.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.fill((0, 0, 0))  
    screen.blit(text_start, start_rect)
    screen.blit(text_exit, exit_rect)

    pygame.display.flip()

    return start_rect, exit_rect

def draw_level_options():
    font = pygame.font.Font(None, 74)
    text_level2 = font.render("Level 2", True, (255, 255, 255))
    text_level1 = font.render("Level 1", True, (255, 255, 255))

    level2_rect = text_level2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    level1_rect = text_level1.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))

    screen.fill((0, 0, 0))  
    screen.blit(text_level2, level2_rect)
    screen.blit(text_level1, level1_rect)

    pygame.display.flip()

    return level2_rect, level1_rect


class Barriel:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def collide(self, player_rect):
        return pygame.Rect(self.x, self.y, self.width, self.height).colliderect(player_rect)


def menu():
    global running
    menu_active = True
    
    start_rect, exit_rect = draw_menu()

    while menu_active:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                menu_active = False
                running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(mouse_pos):
                    menu_active = False
                    level_active = True
                    while level_active:
                        for e in pygame.event.get():
                            if e.type == pygame.QUIT:
                                level_active = False
                                running = False
                        level2_rect, level1_rect = draw_level_options()
                        
                        if e.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()
                            if level2_rect.collidepoint(mouse_pos):
                                level_active = False
                                level2_game()  # Запуск рівня 2
                            if level1_rect.collidepoint(mouse_pos):
                                level_active = False
                                level1_game()  # Запуск рівня 1
                elif exit_rect.collidepoint(mouse_pos):
                    menu_active = False
                    running = False


def level1_game():
    global playr_x, playr_y, jump, start_jump
    playr_x = 0
    playr_y = HEIGHT - playr_height
    jump = False

    wall1 = Barriel((255, 255, 255), 500, 550, 150, 50)
    wall2 = Barriel((0, 0, 0), 500, 550, 5, 50)
    wall3 = Barriel((0, 0, 0), 645, 550, 5, 50)
    wall4 = Barriel((0, 0, 0), 500, 550, 150, 5)
    enemy = Barriel((0, 0, 0), 800, 550, 20, 50)
    enemy1 = Barriel((0, 0, 0), 900, 550, 20, 50)
    enemy2 = Barriel((0, 0, 0), 620, 500, 20, 50)
    wall5 = Barriel((255, 255, 255), 1000, 550, 100, 50)
    wall6 = Barriel((0, 0, 0), 1000, 550, 5, 50)
    wall7 = Barriel((0, 0, 0), 1100, 550, 5, 50)
    wall8 = Barriel((0, 0, 0), 1000, 550, 100, 5)
    finish = Barriel((0, 255, 0), 1180, 500, 200, 100)

    level1_active = True
    while level1_active:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                level1_active = False
                break

        keys = pygame.key.get_pressed()

        player_rect = pygame.Rect(playr_x, playr_y, playr_width, playr_height)
        wall1_rect = pygame.Rect(wall1.x, wall1.y, wall1.width, wall1.height)
        enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
        enemy1_rect = pygame.Rect(enemy1.x, enemy1.y, enemy1.width, enemy1.height)
        enemy2_rect = pygame.Rect(enemy2.x, enemy2.y, enemy2.width, enemy2.height)
        wall5_rect = pygame.Rect(wall5.x, wall5.y, wall5.width, wall5.height)
        finish_rect = pygame.Rect(finish.x, finish.y, finish.width, finish.height)

        if keys[pygame.K_a] and playr_x > 0:
            new_rect = player_rect.move(-playr_speed, 0)
            if not wall1_rect.colliderect(new_rect) and not wall5_rect.colliderect(new_rect):
                playr_x -= playr_speed

        if keys[pygame.K_d] and playr_x < WIDTH - playr_width:
            new_rect = player_rect.move(playr_speed, 0)
            if not wall1_rect.colliderect(new_rect) and not wall5_rect.colliderect(new_rect):
                playr_x += playr_speed

        if keys[pygame.K_SPACE] and not jump:
            jump = True
            start_jump = jump_streng

        if jump:
            playr_y += start_jump
            start_jump += gravity
            if player_rect.colliderect(wall1_rect) and start_jump < 0: 
                playr_y = wall1.y - playr_height  
                jump = False
                start_jump = 0
            if player_rect.colliderect(wall5_rect) and start_jump < 0: 
                playr_y = wall5.y - playr_height  
                jump = False
                start_jump = 0               

            if playr_y >= grond_y:
                playr_y = grond_y
                jump = False
                start_jump = 0

        if not jump and playr_y < grond_y:
            playr_y = grond_y

        if player_rect.colliderect(wall1_rect):
            if playr_y + playr_height > wall1.y:  
                playr_y = wall1.y - playr_height  
                jump = False
                start_jump = 0
        if player_rect.colliderect(wall5_rect):
            if playr_y + playr_height > wall5.y:  
                playr_y = wall5.y - playr_height  
                jump = False
                start_jump = 0
        if player_rect.colliderect(enemy_rect):
            font = pygame.font.Font(None, 74)
            lose_text = font.render('You Lose', True, (255, 255, 255))
            screen.fill((0, 0, 0))
            screen.blit(lose_text, lose_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
            pygame.display.flip()
            pygame.time.delay(2000)
            menu()
            reset_player()

        if player_rect.colliderect(enemy1_rect):
            font = pygame.font.Font(None, 74)
            lose_text = font.render('You Lose', True, (255, 255, 255))
            screen.fill((0, 0, 0))
            screen.blit(lose_text, lose_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
            pygame.display.flip()
            pygame.time.delay(2000)
            menu()
            reset_player()

        if player_rect.colliderect(enemy2_rect):
            font = pygame.font.Font(None, 74)
            lose_text = font.render('You Lose', True, (255, 255, 255))
            screen.fill((0, 0, 0))
            screen.blit(lose_text, lose_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
            pygame.display.flip()
            pygame.time.delay(2000)
            menu()
            reset_player()

        if player_rect.colliderect(finish_rect):
            font = pygame.font.Font(None, 74)
            win_text = font.render('You Win!!', True, (255, 255, 255))
            screen.fill((0, 0, 0))
            screen.blit(win_text, win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
            pygame.display.flip()
            pygame.time.delay(2000)
            menu()
            reset_player()

        screen.blit(background, (0, 0))
        screen.blit(player_skin, (playr_x, playr_y))

        wall1.draw()
        wall2.draw()
        wall3.draw()
        wall4.draw()
        enemy.draw()
        enemy1.draw()
        enemy2.draw()
        wall5.draw()
        wall6.draw()
        wall7.draw()
        wall8.draw()
        finish.draw()

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)


def level2_game():
    global playr_x, playr_y, jump, start_jump, grounded
    playr_x = 0
    playr_y = HEIGHT - playr_height  
    jump = False
    grounded = False  


    wall1 = Barriel((255, 0, 0), 300, HEIGHT - 50, 150, 50) 
    wall2 = Barriel((0, 255, 0), 500, 550, 100, 30)  
    wall3 = Barriel((0, 0, 255), 700, 500, 120, 40) 
    wall4 = Barriel((255, 255, 0), 950, 400, 90, 30) 
    wall5 = Barriel((255, 255, 255), 1000, 650, 100, 50) 
    enemy = Barriel((0, 0, 0), 800, 600, 20, 50)  
    enemy1 = Barriel((0, 0, 0), 900, 500, 20, 50)  
    enemy2 = Barriel((0, 0, 0), 650, 400, 20, 50)  
    moving_platform = Barriel((255, 165, 0), 400, 300, 100, 30)  

    finish = Barriel((0, 255, 0), 1180, 300, 200, 100)  


    moving_platform_direction = 1  # 1 - вправо, -1 - вліво

    level2_active = True
    while level2_active:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                level2_active = False
                break

        keys = pygame.key.get_pressed()

        player_rect = pygame.Rect(playr_x, playr_y, playr_width, playr_height)
        wall1_rect = pygame.Rect(wall1.x, wall1.y, wall1.width, wall1.height)
        wall2_rect = pygame.Rect(wall2.x, wall2.y, wall2.width, wall2.height)
        wall3_rect = pygame.Rect(wall3.x, wall3.y, wall3.width, wall3.height)
        wall4_rect = pygame.Rect(wall4.x, wall4.y, wall4.width, wall4.height)
        wall5_rect = pygame.Rect(wall5.x, wall5.y, wall5.width, wall5.height)
        enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
        enemy1_rect = pygame.Rect(enemy1.x, enemy1.y, enemy1.width, enemy1.height)
        enemy2_rect = pygame.Rect(enemy2.x, enemy2.y, enemy2.width, enemy2.height)
        moving_platform_rect = pygame.Rect(moving_platform.x, moving_platform.y, moving_platform.width, moving_platform.height)
        finish_rect = pygame.Rect(finish.x, finish.y, finish.width, finish.height)

     
        if keys[pygame.K_a] and playr_x > 0:
            new_rect = player_rect.move(-playr_speed, 0)
            if not wall1_rect.colliderect(new_rect) and not wall2_rect.colliderect(new_rect) and not wall3_rect.colliderect(new_rect):
                playr_x -= playr_speed

        if keys[pygame.K_d] and playr_x < WIDTH - playr_width:
            new_rect = player_rect.move(playr_speed, 0)
            if not wall1_rect.colliderect(new_rect) and not wall2_rect.colliderect(new_rect) and not wall3_rect.colliderect(new_rect):
                playr_x += playr_speed

        if keys[pygame.K_SPACE] and not jump:
            jump = True
            start_jump = jump_streng

  
        if jump:
            playr_y += start_jump
            start_jump += gravity

            if playr_y >= grond_y:
                playr_y = grond_y
                jump = False
                start_jump = 0

           
            if start_jump > 0:  
                if player_rect.colliderect(wall1_rect) and player_rect.bottom <= wall1.y + start_jump:
                    playr_y = wall1.y - playr_height
                    jump = False
                    start_jump = 0
                    grounded = True

                elif player_rect.colliderect(wall2_rect) and player_rect.bottom <= wall2.y + start_jump:
                    playr_y = wall2.y - playr_height
                    jump = False
                    start_jump = 0
                    grounded = True

                elif player_rect.colliderect(wall3_rect) and player_rect.bottom <= wall3.y + start_jump:
                    playr_y = wall3.y - playr_height
                    jump = False
                    start_jump = 0
                    grounded = True

                elif player_rect.colliderect(wall4_rect) and player_rect.bottom <= wall4.y + start_jump:
                    playr_y = wall4.y - playr_height
                    jump = False
                    start_jump = 0
                    grounded = True

      
        if not jump and grounded:
            grounded = True
            start_jump = 0

        else:
            grounded = False
            
            
            
     
          

   
        if not grounded and not jump:
            playr_y = playr_y 




        if player_rect.colliderect(finish_rect):
            font = pygame.font.Font(None, 74)
            win_text = font.render('You Win!!', True, (255, 255, 255))
            screen.fill((0, 0, 0))
            screen.blit(win_text, win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
            pygame.display.flip()
            pygame.time.delay(2000)
            menu()
            reset_player()


        if player_rect.colliderect(enemy_rect) or player_rect.colliderect(enemy1_rect) :
            font = pygame.font.Font(None, 74)
            lose_text = font.render('You Lose', True, (255, 255, 255))
            screen.fill((0, 0, 0))
            screen.blit(lose_text, lose_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
            pygame.display.flip()
            pygame.time.delay(2000)
            menu()
            reset_player()

        moving_platform.x += moving_platform_direction * 2
        if moving_platform.x <= 0 or moving_platform.x >= WIDTH - moving_platform.width:
            moving_platform_direction *= -1  

       
        screen.blit(background, (0, 0))
        screen.blit(player_skin, (playr_x, playr_y))


        wall1.draw()
        wall2.draw()
        wall3.draw()
        wall4.draw()
        wall5.draw()
        enemy.draw()
        enemy1.draw()

        moving_platform.draw()
        finish.draw()

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)






menu()
pygame.quit()
