import pygame
WIDTH = 800
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
fps = 60
pygame.init()
class BALL:
    def __init__(self):
        self.PongXpos = 400
        self.PongYpos = 400
        self.PongVelocityX = 9
        self.PongVelocityY = 9
        self.score = 0
        self.AI_Score = 0
    def draw_ball(self):
        self.CircleRect = pygame.Rect(self.PongXpos - 30,self.PongYpos - 30,60,60)
        pygame.draw.circle(screen,(255,255,255),(self.PongXpos,self.PongYpos),30)
        pygame.draw.line(screen,(255,255,255),(400,0),(400,800),2)

    def move_ball(self):
        self.PongXpos += self.PongVelocityX
        self.PongYpos += self.PongVelocityY

    def add_collision(self):

        if self.PongXpos >=770 or self.PongXpos <= 30:
            self.PongVelocityX *= -1
            self.AI_Score = self.AI_Score + 1
        if self.PongYpos >= 670 or self.PongYpos <= 30:
            self.PongVelocityY *= -1
class PADDLES:
    def __init__(self):
        self.player_paddle = pygame.Rect(50,400,20,80)
        self.PaddleVelocity = 7
        self.AI_paddle = pygame.Rect(750,400,20,80)
    def draw_paddles(self):
        pygame.draw.rect(screen,(255,255,255),self.player_paddle)
        pygame.draw.rect(screen,(255,255,255),self.AI_paddle)
    def move_paddles(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_w]:
            self.player_paddle.y -= self.PaddleVelocity
        elif self.keys[pygame.K_s]:
            self.player_paddle.y += self.PaddleVelocity


class MAIN:
    def __init__(self):
        self.ball = BALL()
        self.paddle = PADDLES()
        self.cooldown = False
        self.Text = pygame.font.SysFont(None,50)
    def draw_elements(self):
        self.ball.draw_ball()
        self.paddle.draw_paddles()
        self.score = self.ball.score
        self.AIscore = self.ball.AI_Score
        self.System = self.Text.render(f"Score:{self.score}",True,(255,255,255))
        self.AISystem = self.Text.render(f"AI_Score:{self.AIscore}",True,(255,255,255))
        screen.blit(self.System,(0,0))
        screen.blit(self.AISystem,(600,0))
    def move_elements(self):
        self.ball.move_ball()
        self.ball.add_collision()
        self.paddle.move_paddles()

    def check_collsion(self):
        if self.ball.CircleRect.colliderect(self.paddle.player_paddle):
            self.ball.PongVelocityX *= -1
            self.ball.PongXpos = self.ball.PongXpos+ 20
        elif self.ball.CircleRect.colliderect(self.paddle.AI_paddle):
            self.ball.PongVelocityX *= -1
            self.ball.PongXpos = self.ball.PongXpos - 20
        elif self.paddle.player_paddle.y >= 700 -self.paddle.player_paddle.height:
            self.paddle.player_paddle.y = 619
        elif self.paddle.player_paddle.y <= 0 :
            self.paddle.player_paddle.y = 1
    def AIPaddle(self):
        if self.paddle.AI_paddle.centery <= self.ball.PongYpos:
            self.paddle.AI_paddle.y += self.paddle.PaddleVelocity

        elif self.paddle.AI_paddle.centery >= self.ball.PongYpos:
            self.paddle.AI_paddle.y -= self.paddle.PaddleVelocity

            
main = MAIN()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((20,20,20))
    main.draw_elements()
    main.move_elements()
    main.check_collsion()
    main.AIPaddle()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit