import pygame
import sys
from moviepy.editor import VideoFileClip
import threading
import math

# Initializing pygame
pygame.init()

# Setting up the display
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multimedia Car Animation with Rotating Wheels")

clock = pygame.time.Clock()

# Colors used
PINK = (255, 105, 180)
DARK_PINK = (200, 70, 130)
LIGHT_PINK = (255, 182, 193)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
SKY = (135, 206, 235)
ROAD = (50, 50, 50)
WHITE = (255, 255, 255)
TREE_GREEN = (0, 155, 0)

# Loading the multimedia assets used
pygame.mixer.music.load("background_music.wav")  # Background music
pygame.mixer.music.play(-1)  # Loop audio

# Background drawing function 
def draw_background(surface):
    surface.fill(SKY)  #blue Sky
    pygame.draw.rect(surface, ROAD, (0, HEIGHT - 100, WIDTH, 100))  # Road

    # Drawing the trees
    for i in range(0, WIDTH, 150):
        pygame.draw.rect(surface, (101, 67, 33), (i + 50, HEIGHT - 180, 20, 80))  # Tree trunk
        pygame.draw.circle(surface, TREE_GREEN, (i + 60, HEIGHT - 200), 30)  # Tree leaves

    #Drawing the sun
    for i in range(12):
       angle = math.radians(i * 30)
       start_x = WIDTH - 80 + int(50 * math.cos(angle))
       start_y = 80 + int(50 * math.sin(angle))
       end_x = WIDTH - 80 + int(70 * math.cos(angle))
       end_y = 80 + int(70 * math.sin(angle))
       pygame.draw.line(surface, (255, 223, 0), (start_x, start_y), (end_x, end_y), 2)
       # Drawing  the sun in the top right corner
       pygame.draw.circle(surface, (255, 255, 0), (WIDTH - 80, 80), 40)  # Bright yellow sun


# Wheel rotation angle
wheel_angle = 0

# Function to draw the car wheels
def draw_wheel(surface, center, radius, angle):
    """Draws a rotating wheel with spokes."""
    pygame.draw.circle(surface, (0, 0, 0), center, radius)  # Wheel outline
    
    # Draw 4 rotating spokes
    for i in range(4):  
        # Calculate spoke positions
        spoke_x = center[0] + radius * math.cos(math.radians(angle + i * 90))
        spoke_y = center[1] + radius * math.sin(math.radians(angle + i * 90))
        
        pygame.draw.line(surface, (255, 255, 255), center, (spoke_x, spoke_y), 3)

# Function to draw a van
def draw_van(surface, x, y, wheel_angle):
    body_color = (255, 105, 180)  # Pink body
    window_color = (173, 216, 230)  # Light blue for windows
    wheel_color = (0, 0, 0)  # Black wheel colour

    # Car body 
    pygame.draw.rect(surface, body_color, (x, y - 40, 140, 60))  # Main body
    pygame.draw.rect(surface, body_color, (x + 20, y - 70, 100, 30))  # Upper cabin

    # Windows on upper cabin
    pygame.draw.rect(surface, window_color, (x + 25, y - 65, 25, 20))
    pygame.draw.rect(surface, window_color, (x + 55, y - 65, 25, 20))
    pygame.draw.rect(surface, window_color, (x + 85, y - 65, 25, 20))

    # Draw rotating wheels
    draw_wheel(surface, (x + 30, y + 20), 15, wheel_angle)  # Front wheel
    draw_wheel(surface, (x + 110, y + 20), 15, wheel_angle)  # Rear wheel

# Animation loop setup
x_pos = -140  # Start off-screen to the left
car_y = HEIGHT - 100  # Lower on the screen
wheel_speed = 5  # Rotation speed

running = True
while running:
    # Clears and redraws the background and the car
    draw_background(screen)
    draw_van(screen, x_pos, car_y, wheel_angle)

    # Moves the van to the right
    x_pos += 4  # Speed of the car

    # Rotate wheels 
    wheel_angle += wheel_speed  # Rotates left for forward motion

    # Reset position once off-screen to the right
    if x_pos > WIDTH:
        x_pos = -140  # Start again from left outside screen

    # Handle quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Refresh the display
    pygame.display.flip()
    clock.tick(30)  # 30 frames per second

# Quit
pygame.quit()
sys.exit()
