import pygame
import random

def define_parameters():
    params = dict()
    
    # Setting
    params['game_width'] = 440
    params['game_height'] = 440
    
    return param

class Game:
    def __init__(self, game_width, game_height):
        pygame.display.set_caption('Snake Game')
        self.game_width = game_width
        self.game_height = game_height
        self.game_display = pygame.display.set_mode((self.game_width, self.game_height))
        
        self.gameover = False
        self.player = Player(self)
        self.food = Food()
        self.score = 0
        
class Snake(object):
    def __init__(self, game):
        self.x = 0.45 * game.game_width
        self.y = 0.45 * game.game_height
        
        self.position = []
        self.position.append([self.x, self.y)
        
        self.snake_block = 10
        self.image = pygame.image.load('img/snakeBody.png')
    
    def move(self):
                              
        self.isDie()
    
    def isDie(self):
        if self.x < 10 or self.x > game.game_width - 10 \
            or self.y < 10 or self.y > game.game_height - 10:   # Touch the boundary
            game.gameover = True
        
        if [self.x, self.y] in self.position: # Touch itself
            game.gameover = True
                              
    def eat(self):
        pass
    
    def grow(self):
        pass
    
    def show(self):
        for [x, y] in self.position:
            game.game_display.blit(self.image, (x, y))
        
    
    
class Food(object):
    def __init__(self, game):
        self.x = random.randrange(1, game.game_width//10) * 10
        self.y = random.randrange(1, game.game_height//10) * 10
        self.image = pygame.image.load('img/food.png')
        
    def spawn(self, game, snake):
        self.x = random.randrange(1, game.game_width//10) * 10
        self.y = random.randrange(1, game.game_height//10) * 10
        
        if [self.x, self.y] in snake.position:
            self.spawn(snake.position)
            
    def show(self, game):
        game.game_display.blit(self.image, (self.x, self.y))
 
 
 def display(player, food, game, record):

 
def run(params):
    pygame.init()
    game = Game(params['game_width'], params['game_height'])
    snake = Snake(game)
    food = Food()
    
    while not game.gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                              
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
        
        snake.show()
        food.show()
        pygame.display.update()
    
if __name__ == '__main__':
    params = define_parameters()
    
    run(params)
