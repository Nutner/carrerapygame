import pygame,sys
import random

class Runner():
    __costumes = ("redm","bluem","purplem","orangem","yellowm")
    
    def __init__(self,x=0,y=0):
        newCostume = random.randint(0,4)
    
        self.costume =pygame.image.load("images/{}.png".format(self.__costumes[newCostume]))
        self.position = [x,y]
        self.name = ""
        
    def run(self):
        self.position[0] += random.randint(1,6)
        
class Game():
    runners = []
    __startLine = 20
    __finishLine = 620
    __posY = (160,200, 240,280)
    __names = ("David","Raquel","Sara","Raul")
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de tortugas")
        
        for i in range(4):
            theRunner = Runner(self.__startLine,self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
            
    def close(self):
        pygame.quit()
        sys.exit()
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    
            for arunner in self.runners:
                arunner.run()
                if arunner.position[0] >= self.__finishLine :
                    print("{} ha ganado".format(arunner.name))
                    gameOver = True
                
            self.__screen.blit(self.__background,(0,0))
            
            for runner in self.runners:
                self.__screen.blit(runner.costume, runner.position)
            
            pygame.display.flip()
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
         
                       
        
        
if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.competir()