import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
trail_color = (50, 50, 50)

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("DVD Logo Path Tracking")

# Load DVD logo (using a simple rectangle for simplicity)
logo_width, logo_height = 140, 140  # Standard size similar to the article's reference
logo_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
logo_x, logo_y = random.randint(0, screen_width - logo_width), random.randint(0, screen_height - logo_height)

# Movement speed
speed_x = 3
speed_y = 3

# To store the path of the logo
path = []

# Corners hit tracker and bounce counter
corners_hit = set()
bounce_count = 0

# Function to check if the logo hits a corner and return which one
def check_corner(x, y, width, height, screen_width, screen_height):
    if x == 0 and y == 0:
        return "Top-left"
    elif x == screen_width - width and y == 0:
        return "Top-right"
    elif x == 0 and y == screen_height - height:
        return "Bottom-left"
    elif x == screen_width - width and y == screen_height - height:
        return "Bottom-right"
    return None

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed_x *= 1.5
                speed_y *= 1.5
            elif event.key == pygame.K_DOWN:
                speed_x /= 1.5
                speed_y /= 1.5

    # Move the logo
    logo_x += speed_x
    logo_y += speed_y

    # Add the current position to the path
    path.append((logo_x + logo_width // 2, logo_y + logo_height // 2))  # Store center of the logo

    # Check for collisions with the screen edges and bounce
    if logo_x <= 0 or logo_x + logo_width >= screen_width:
        speed_x = -speed_x
        logo_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))  # Change color
        bounce_count += 1

    if logo_y <= 0 or logo_y + logo_height >= screen_height:
        speed_y = -speed_y
        logo_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))  # Change color
        bounce_count += 1

    # Check if the logo hits a corner
    corner_hit = check_corner(logo_x, logo_y, logo_width, logo_height, screen_width, screen_height)
    if corner_hit and corner_hit not in corners_hit:
        corners_hit.add(corner_hit)
        print(f"The logo hit the {corner_hit} corner!")

    # Fill the screen with black
    screen.fill(black)

    # Draw the path of the logo
    if len(path) > 1:
        pygame.draw.lines(screen, trail_color, False, path, 2)  # Draw the path with lines

    # Draw the logo
    pygame.draw.rect(screen, logo_color, (logo_x, logo_y, logo_width, logo_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

    # Predict if a corner should be hit based on bounce count (approx every 550 bounces)
    if bounce_count >= 550:
        print("The logo should have hit a corner based on bounce frequency.")
        bounce_count = 0  # Reset count for continued observation

# Final message after the loop ends
if corners_hit:
    print(f"Conclusion: The logo hit the following corners: {', '.join(corners_hit)}.")
else:
    print("Conclusion: The logo did not hit any corners during the simulation.")

# Quit pygame
pygame.quit()
