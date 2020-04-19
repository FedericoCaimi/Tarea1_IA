from abc import ABC, abstractmethod
from queue import PriorityQueue
from queue import Queue

#DO NOT CHANGE THIS CLASS: EXTEND IT WITH YOUR OWN
class AgentLRTA():

    def __init__(self, model):
        super().__init__()
        self.model = model

    def run(self, env):
        self.model.reset()
        return self.loop(env)

    def loop(self, env):
        print("LRTA...")
        env.render()
        done = False
        step_counter = 0
        all_rewards = 0
        lastState = None
        action = ''
        H = []
        while not done:  

            actualState = self.model.map_obs_to_state(env.observation)
            goalId = self.model.get_goal(step_counter)[0]

            action = self.LRTA(actualState,action,lastState)
            obs, reward, done_env, _ = env.step(action)
            all_rewards += reward
            done = done_env and self.model.is_win_goal()
            env.render()
            step_counter += 1
        return all_rewards, step_counter


    def step(self,node,action):
        estado = node[1]
        nodeAction = str(estado)+action
        actionCost = 1
        return self.model.diccionary[nodeAction],actionCost

    def LRTA(self,actualState,action,lastState):
        actions = ['N','E','S','W']

        if (actualState == goalId):
            break
        if not(actualState in H ):
            HVal = h(actualState)#falta funcion heuristica 
            H[actualState] = HVal
        if (not(lastState == None)):
            result[lastState+action] = actualState
            costsList = []
            for action in actions:
                cost = self.LRTACost(lastState,action,result[lastState+action],H)
                costsList.append(cost)
            H[lastState] = min(costsList)
        returnAction = None
        minCost = 0
        #cual de las acciones tiene menor costo, la cual sera la que se va a ejecutar en el ambiene 
        for action in actions:
            cost = self.LRTACost(actualState,action,result[actualState+action],H)
            #guardo el priemr costo para comparar
            if(returnAction == None):
                minCost = cost
                returnAction = action
            if (cost < minCost):
                minCost = cost
                returnAction = action
            costsList.append(cost)
        lastState = actualState

        return returnAction

    def LRTACost(self,lastState,action,actualState,H):
        if (actualState == None):
            return h(lastState)#falta funcion heuristica 
        else:
            return 1 +H[actualState]



    
