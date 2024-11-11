import pygame
import random
import sys

# Initialisiere pygame
pygame.init()

# Spielvariablen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BIRD_WIDTH = 40
BIRD_HEIGHT = 40
PIPE_WIDTH = 70
PIPE_HEIGHT = 500
PIPE_GAP = 150
BIRD_X = 50
BIRD_Y = SCREEN_HEIGHT // 2
GRAVITY = 1
JUMP_STRENGTH = -15
PIPE_VELOCITY = 5
SPEED = 60

# Farben
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Bildschirm einrichten
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Schriftarten
font = pygame.font.SysFont('Arial', 30)

# Vogelklasse
class Bird:
    def __init__(self):
        self.x = BIRD_X
        self.y = BIRD_Y
        self.velocity = 0
        self.rect = pygame.Rect(self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT)

    def jump(self):
        self.velocity = JUMP_STRENGTH

    def move(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

# Pipe-Klasse
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
        self.top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - self.height - PIPE_GAP)

    def move(self):
        self.x -= PIPE_VELOCITY
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.top_rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)

# Funktion, um das Spiel zu starten
def main():
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    clock = pygame.time.Clock()
    running = True
    game_over = False

    while running:
        screen.fill(WHITE)

        # Überprüfen, ob das Spiel vorbei ist
        if game_over:
            game_over_text = font.render(f"Game Over! Score: {score}", True, BLACK)
            screen.blit(game_over_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3))
            pygame.display.flip()
            pygame.time.wait(2000)
            break

        # Ereignisbehandlung
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        # Vogel bewegen
        bird.move()

        # Hindernisse bewegen und generieren
        for pipe in pipes:
            pipe.move()
            pipe.draw()

        # Wenn ein Hindernis den Bildschirm verlässt, entferne es
        if pipes[0].x < -PIPE_WIDTH:
            pipes.pop(0)
            pipes.append(Pipe())
            score += 1

        # Kollision überprüfen (Vogel mit Hindernissen oder dem Bildschirmrand)
        if bird.rect.colliderect(pipes[0].top_rect) or bird.rect.colliderect(pipes[0].bottom_rect):
            game_over = True

        if bird.y <= 0 or bird.y + BIRD_HEIGHT >= SCREEN_HEIGHT:
            game_over = True

        # Vogel zeichnen
        bird.draw()

        # Punktzahl anzeigen
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Bildschirm aktualisieren
        pygame.display.flip()

        # Spielgeschwindigkeit
        clock.tick(SPEED)

    pygame.quit()
    sys.exit()

# Das Spiel starten
if __name__ == "__main__":
    main()
 
