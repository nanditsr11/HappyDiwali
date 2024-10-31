import pygame
import random
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Happy Diwali!")
clock = pygame.time.Clock()

# Define Colors
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
COLORS = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (128, 0, 128), (255, 165, 0), (255, 20, 147)]

# Font setup
font = pygame.font.Font(None, 80)
text_surface = font.render("Happy Diwali!", True, GOLD)
text_rect = text_surface.get_rect(center=(400, 150))

# Confetti Data
confetti_list = [{'pos': [random.randint(0, 800), random.randint(-600, 0)], 'speed': random.randint(1, 5), 'color': random.choice(COLORS)} for _ in range(50)]

# Star Data
stars = [{'pos': [random.randint(0, 800), random.randint(0, 600)], 'timer': random.randint(20, 60)} for _ in range(30)]

# Firework Data
fireworks = []

# Function to update fireworks
def update_fireworks():
    if random.random() < 0.05:  # 5% chance to create new firework
        color = random.choice(COLORS)
        x = random.randint(100, 700)
        y = random.randint(100, 300)
        fireworks.append({'particles': [[x, y, random.uniform(-2, 2), random.uniform(-2, 2), random.randint(3, 5)] for _ in range(30)], 'color': color})

    for firework in fireworks:
        for particle in firework['particles']:
            particle[0] += particle[2]
            particle[1] += particle[3]
            particle[4] -= 0.1  # Shrink over time
        firework['particles'] = [p for p in firework['particles'] if p[4] > 0]  # Remove small particles

# Function to draw confetti
def draw_confetti():
    for confetti in confetti_list:
        pygame.draw.circle(screen, confetti['color'], confetti['pos'], 5)
        confetti['pos'][1] += confetti['speed']
        if confetti['pos'][1] > 600:  # Reset confetti when it goes off-screen
            confetti['pos'][1] = random.randint(-50, -10)
            confetti['pos'][0] = random.randint(0, 800)

# Function to draw stars
def draw_stars():
    for star in stars:
        if star['timer'] > 0:
            pygame.draw.circle(screen, WHITE, star['pos'], 2)
        star['timer'] -= 1
        if star['timer'] <= 0:
            star['pos'] = [random.randint(0, 800), random.randint(0, 600)]
            star['timer'] = random.randint(20, 60)

# Function to draw fireworks
def draw_fireworks():
    for firework in fireworks:
        for particle in firework['particles']:
            pygame.draw.circle(screen, firework['color'], (int(particle[0]), int(particle[1])), int(particle[4]))

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(text_surface, text_rect)

    # Draw each effect
    draw_confetti()
    draw_stars()
    update_fireworks()
    draw_fireworks()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
