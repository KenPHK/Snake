import pygame
import random

def define_parameters():
    params = dict()
    
    # Setting
    params['game_width'] = 800
    params['game_height'] = 800
    params['block_size'] = 20
    
    return params

class Game:
    def __init__(self, game_width, game_height, block_size):
        pygame.display.set_caption('Snake Game')
        self.game_width = game_width
        self.game_height = game_height
        self.game_display = pygame.display.set_mode((self.game_width, self.game_height))
        self.block_size = block_size
        self.gameover = False
        self.score = 0
    
    def show_score(self):
        myfont = pygame.font.SysFont('Lucida Console', 20)
        text_score = myfont.render(str(self.score), True, (255, 255, 255))
        self.game_display.blit(text_score, (120, 440))
        
class Snake(object):
    def __init__(self, game):
        self.x = 0.45 * game.game_width
        self.y = 0.45 * game.game_height
        
        self.x_change = game.block_size
        self.y_change = 0
        
        self.position = []
        self.position.append([self.x, self.y])
        
        self.snake_size = game.block_size
        self.image = pygame.image.load('img/snakeBody.png')
        self.eaten = False
    
    def move(self, game, food):
        
        self.x += self.x_change
        self.y += self.y_change
        self.eat(food, game)
        if self.eaten == True:
            self.position.append([self.x, self.y])
            self.eaten = False
            game.score += 1
        else:
            for i in range(len(self.position) - 1):
                self.position[i] = self.position[i + 1]
            self.position[-1] = [self.x, self.y]
        self.alive(game)

    
    def alive(self, game):
        if self.x < self.snake_size or self.x > game.game_width - self.snake_size \
            or self.y < self.snake_size or self.y > game.game_height - self.snake_size:   # Touch the boundary
            game.gameover = True
        
        if [self.x, self.y] in self.position[0:-1]: # Touch itself
            game.gameover = True
                              
    def eat(self, food, game):
        if self.x == food.x and self.y == food.y:
            self.eaten = True
            food.spawn(game, self)
    
    def show(self, game):
        for [x, y] in self.position:
            pygame.draw.rect(game.game_display, (0, 255, 0), [x, y, self.snake_size, self.snake_size])
        
    
    
class Food(object):
    def __init__(self, game):
        self.food_size = game.block_size
        self.x = random.randrange(1, game.game_width//self.food_size) * self.food_size
        self.y = random.randrange(1, game.game_height//self.food_size) * self.food_size
        self.image = pygame.image.load('img/food.png')
        
    def spawn(self, game, snake):
        self.x = random.randrange(1, game.game_width//self.food_size) * self.food_size
        self.y = random.randrange(1, game.game_height//self.food_size) * self.food_size
        
        if [self.x, self.y] in snake.position:
            self.spawn(snake.position)
            
    def show(self, game):
        pygame.draw.rect(game.game_display, (255, 255, 255), [self.x, self.y, self.food_size, self.food_size])
 


 
def run(params):
    pygame.init()
    game = Game(params['game_width'], params['game_height'], params['block_size'])
    snake = Snake(game)
    food = Food(game)
    fps = pygame.time.Clock()
    while not game.gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                              
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.x_change = 0
                    snake.y_change = -1 * game.block_size
                    
                if event.key == pygame.K_DOWN:
                    snake.x_change = 0
                    snake.y_change = game.block_size
                    
                if event.key == pygame.K_LEFT:
                    snake.x_change = -1 * game.block_size
                    snake.y_change = 0
                    
                if event.key == pygame.K_RIGHT:
                    snake.x_change = game.block_size
                    snake.y_change = 0
                    
        snake.move(game, food)
        game.game_display.fill((0, 0, 0))
        game.show_score()
        snake.show(game)
        food.show(game)
        pygame.display.update()
        fps.tick(15)
    
    pygame.quit()
    
if __name__ == '__main__':
    params = define_parameters()
    
    run(params)
