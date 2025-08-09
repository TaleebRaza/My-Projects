from random import randrange
import pygame, neat, time, os

pygame.font.init()

# Window Dimensions
WIDTH, HEIGHT = 500, 800

# Loading Images
BIRD_IMAGES = [pygame.transform.scale2x(pygame.image.load(os.path.join("flappy bird images", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("flappy bird images", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("flappy bird images", "bird3.png")))]
PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("flappy bird images", "pipe.png")))
BASE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("flappy bird images", "base.png")))
BG_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("flappy bird images", "bg.png")))

STAT_FONT = pygame.font.SysFont("comicsans", 50)


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

def draw_window(win, birds, pipes, base, score):
    win.blit(BG_IMAGE, (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIDTH - 10 - text.get_width(), 10))

    base.draw(win)

    for bird in birds:
        bird.draw(win)
    pygame.display.update()


def fitness_function(genomes, config):
    nets = []
    ge = []
    birds = []

    for _, g in genomes:
        net  = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        g.fitness = 0
        ge.append(g)

    base = Base(730)
    pipes = [Pipe(600)]
    score = 0

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].TOP_PIPE_IMG.get_width():
                pipe_ind = 1
        else:
            running = False
            break

        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1

            output = nets[x].activate((
                bird.y,  # Bird's Y position
                abs(bird.y - pipes[pipe_ind].height),  # Distance from top pipe
                abs(bird.y - pipes[pipe_ind].bottom),  # Distance from bottom pipe
            ))
            if output[0] > 0.5:
                bird.jump()

        add_pipe = False
        pipes_to_remove = []

        for pipe in pipes:
            for x, bird in enumerate(birds):
                if pipe.collide(bird):
                    ge[x].fitness -= 1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if pipe.x + pipe.TOP_PIPE_IMG.get_width() < 0:
                 pipes_to_remove.append(pipe)
            pipe.move()

        if add_pipe:
            score += 1
            for g in ge:
                g.fitness += 5
            pipes.append(Pipe(600))

        for x in pipes_to_remove:
            pipes.remove(x)

        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_width() >= 730 or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)
        base.move()
        draw_window(window, birds, pipes, base, score)


def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_file)

    population = neat.Population(config)

    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    winner = population.run(fitness_function, 50)

if __name__ == '__main__':
    local_directory = os.path.dirname(__file__)
    config_file_path = os.path.join(local_directory, "Config file")

    run(config_file_path)