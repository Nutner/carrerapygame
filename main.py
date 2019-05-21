import pygame,sys
import random

class Runner():
    def __init__(self,x=0,y=0):
        self.costume =pygame.image.load("images/redm.png")
        self.position = (x,y)
        self.name= "Tortuga"
        
    def run(self):
        self.position[0] += random.randint(1,6)

    
    

class Game():
    corredores = []
    __startLine = 20
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de tortugas")
        
        firstRunner = Runner(self.__startLine,240)
        firstRunner.name = "speedy"
        self.corredores.append(firstRunner)
        
        
          
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                   
            self.__screen.blit(self.__background,(0,0))
            self.__screen.blit(self.corredores[0].costume,self.corredores[0].position)
            pygame.display.flip()
                       
        pygame.quit()
        sys.exit()
        
        
        
if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.competir()