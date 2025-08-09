from random import randrange

import pygame, neat, time, os


# Window Dimensions
WIDTH, HEIGHT = 500, 800

# Loading Images
BIRD_IMAGES = [pygame.transform.scale2x(pygame.image.load(os.path.join("flappy bird images", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("flappy bird images", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("flappy bird images", "bird3.png")))]
PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("flappy bird images", "pipe.png")))
BASE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("flappy bird images", "base.png")))
BG_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("flappy bird images", "bg.png")))

# Class Bird
class Bird:
    IMGS = BIRD_IMAGES
    MAX_ROTATION = 25
    ROT_VELOCITY = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        # Start off these values at x, y (center of screen)
        self.x = x
        self.y = y

        self.tilt = 0
        self.tick_count = 0
        self.velocity = 0
        self.height = self.y

        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.velocity = -10.5 # Set velocity to -vie to move up
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1 # one frame passed (FPS)

        displacement = self.velocity * self.tick_count + 1.5 * self.tick_count**2

        if displacement >= 16:
            displacement = 16
        elif displacement < 0:
            displacement -= 2

        self.y += displacement

        if displacement < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VELOCITY

    def draw(self, win):
        total_images = len(self.IMGS)

        self.img = self.IMGS[(self.img_count // self.ANIMATION_TIME) % total_images]

        self.img_count += 1
        if self.img_count > self.ANIMATION_TIME * total_images:
            self.img_count = 0

        if self.tilt < -80:
            self.img = self.IMGS[1]

        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Pipe:
    GAP = 200
    VELOCITY = 5

    def __init__(self, x):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        self.TOP_PIPE_IMG = pygame.transform.flip(PIPE_IMAGE, 0, 1)
        self.BOTTOM_PIPE_IMG = PIPE_IMAGE

        self.passed = False

        self.set_height()

    def set_height(self):
        self.height = randrange(50, 450)
        self.top = self.height - self.TOP_PIPE_IMG.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VELOCITY

    def draw(self, win):
        win.blit(self.TOP_PIPE_IMG, (self.x, self.top))
        win.blit(self.BOTTOM_PIPE_IMG, (self.x, self.bottom))

    def collide(self, bird):
        bird_mask = bird.get_mask()

        top_pipe_mask = pygame.mask.from_surface(self.TOP_PIPE_IMG)
        bottom_pipe_mask = pygame.mask.from_surface(self.BOTTOM_PIPE_IMG)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        bottom_point = bird_mask.overlap(bottom_pipe_mask, bottom_offset)
        top_point = bird_mask.overlap(top_pipe_mask, top_offset)

        if bottom_point or top_point:
            return True
        else:
            return False

class Base:
    VELOCITY = 5
    WIDTH = BASE_IMAGE.get_width()
    IMG = BASE_IMAGE

    def __init__(self, y):
        self.y = y

        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VELOCITY
        self.x2 -= self.VELOCITY

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))

def draw_window(win, bird):
    win.blit(BG_IMAGE, (0, 0))
    bird.draw(win)
    pygame.display.update()


def main():
    bird = Bird(200, 200)
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        bird.move()
        draw_window(window, bird)


    pygame.quit()
    quit()

main()