import pygame
from .paddle import Paddle
from .ball import Ball

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.paddle_width = 10
        self.paddle_height = 100

        self.player = Paddle(10, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ai = Paddle(width - 20, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ball = Ball(width // 2, height // 2, 7, 7, width, height)

        self.player_score = 0
        self.ai_score = 0
        self.font = pygame.font.SysFont("Arial", 30)
        self.game_over = False
        self.best_of = 5  # Default
        self.max_score = (self.best_of // 2) + 1

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(-10, self.height)
        if keys[pygame.K_s]:
            self.player.move(10, self.height)

    def update(self):
        if self.game_over:
            return

        self.ball.move()
        self.ball.check_collision(self.player, self.ai)

        # Scoring
        if self.ball.x <= 0:
            self.ai_score += 1
            self.ball.reset()
        elif self.ball.x + self.ball.width >= self.width:
            self.player_score += 1
            self.ball.reset()

        self.ai.auto_track(self.ball, self.height)

        # Check game over
        if self.player_score == self.max_score or self.ai_score == self.max_score:
            self.game_over = True

    def render(self, screen):
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, self.player.rect())
        pygame.draw.rect(screen, WHITE, self.ai.rect())
        pygame.draw.ellipse(screen, WHITE, self.ball.rect())
        pygame.draw.aaline(screen, WHITE, (self.width // 2, 0), (self.width // 2, self.height))

        # Scoreboard
        player_text = self.font.render(str(self.player_score), True, WHITE)
        ai_text = self.font.render(str(self.ai_score), True, WHITE)
        screen.blit(player_text, (self.width // 4, 20))
        screen.blit(ai_text, (self.width * 3 // 4, 20))

        # Game Over screen
        if self.game_over:
            self.show_game_over(screen)

    def show_game_over(self, screen):
        winner = "Player Wins!" if self.player_score > self.ai_score else "AI Wins!"
        text = self.font.render(winner, True, WHITE)
        screen.blit(text, (self.width // 2 - text.get_width() // 2, self.height // 2 - 50))

        replay_text = self.font.render("Press 3 / 5 / 7 for Best Of or ESC to Quit", True, WHITE)
        screen.blit(replay_text, (self.width // 2 - replay_text.get_width() // 2, self.height // 2 + 10))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        waiting = False
                        pygame.event.post(pygame.event.Event(pygame.QUIT))
                        return
                    elif event.key in [pygame.K_3, pygame.K_5, pygame.K_7]:
                        self.best_of = int(event.unicode)
                        self.max_score = (self.best_of // 2) + 1
                        self.reset_game()
                        waiting = False



    def reset_game(self):
        self.player_score = 0
        self.ai_score = 0
        self.ball.reset()
        self.game_over = False
