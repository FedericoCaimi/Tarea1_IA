from model import Model

class ModelExt(Model):
    def __init__(self, model_file):
        super().__init__(model_file)
        self.reset()
        relative_path = 'gym_maze/envs/maze_samples/'
        filename = relative_path + model_file
        self.diccionary = self.createDiccionaryFormFile(filename)
        self.x, self.y = self.positionXY(model_file)

    def positionXY(self, model_file):
        posv = model_file.find('v')
        posx = model_file.find('x')
        posG =  model_file.find('_')
        x = model_file[posv+1:posx]
        y = model_file[posx+1:posG]
        return x, y

    def createDiccionaryFormFile(self, filename):
        diccionary = {}
        with open(filename, 'r') as file: 
            for line in file:
                espacio1 = line.find(' ')
                estado = line[0:espacio1]

                espacio2 = line.find(' ',espacio1+1,len(line))
                evento = line[espacio1+1:espacio2]

                estadoSig = line[espacio2+1:len(line)-1]

                diccionary[estado+evento] = estadoSig
        return diccionary

    #modificar para que no dependa del tamaño del laberinto o que obtenga el tamaño por parametros
    def map_obs_to_state(self,obs):
        x = obs[0]
        y = obs[1]
        estado = (y*(int(self.x)-1))+y+x
        return estado

    #heuristica de distancia entre el estad actual y el objetivo 
    def h(self,actualState, goal):
        y = 0
        x = 0
        exitY = abs(actualState-goal)
        while exitY >= int(self.x):
            y += 1
            if((actualState-goal) > 0):
                actualState -= int(self.x)
            else:
                actualState += int(self.x)
            exitY = abs(actualState-goal)
        x = abs(actualState-goal)

        return y+x

