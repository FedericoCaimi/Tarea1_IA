from model import Model

class ModelExt(Model):
    def __init__(self, filename):
        super().__init__()
        self.reset()
        self.diccionary = self.createDiccionaryFormFile(filename)

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
        estado = (y*9)+y+x
        return estado
