from agent import Agent
from abc import ABC, abstractmethod
from queue import PriorityQueue
from queue import Queue
import time

#DO NOT CHANGE THIS CLASS: EXTEND IT WITH YOUR OWN
class AgentLRTA():

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.goalId = None
        self.sequenceStep = None
        self.sequence = None
        self.actualPosition = 0
        self.H = {}
        self.result = {}

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
        while not done:  
            actualState = self.model.map_obs_to_state(env.observation)
            self.goalId = self.model.get_goal(step_counter)[0]
            env.set_goal(self.goalId)
            action, lastState = self.LRTA(actualState,action,lastState)
            obs, reward, done_env, _ = env.step(action)
            all_rewards += reward
            done = done_env and self.model.is_win_goal()
            env.render()
            step_counter += 1.
        return all_rewards, step_counter


    def step(self,node,action):
        estado = node[1]
        nodeAction = str(estado)+action
        actionCost = 1
        return self.model.diccionary[nodeAction],actionCost

    def LRTA(self,actualState,action,lastState):
        actions = ['S','E','W','N']
        costsList = []
        if (actualState == self.goalId):
            return None
        if not(actualState in self.H ):
            HVal = self.h(actualState)
            self.H[actualState] = HVal
        if (not(lastState == None)):
            self.result[str(lastState)+action] = actualState
            costsList = []
            for action in actions:
                stateAction = str(lastState)+action
                if(not(stateAction in self.result)):
                    self.result[stateAction] = None
                cost = self.LRTACost(lastState,action,self.result[str(lastState)+action],self.H)
                costsList.append(cost)
            self.H[lastState] = min(costsList)
        returnAction = None
        minCost = 0
        #cual de las acciones tiene menor costo, la cual sera la que se va a ejecutar en el ambiene 
        for action in actions:
            cost = 0
            stateAction = str(actualState)+action
            if(not(stateAction in self.result)):
                self.result[stateAction] = None
            cost = self.LRTACost(actualState,action,self.result[stateAction],self.H)
            if(returnAction == None):
                minCost = cost
                returnAction = action
            if (cost < minCost):
                minCost = cost
                returnAction = action
            costsList.append(cost)
        lastState = actualState

        return returnAction, lastState

    def LRTACost(self,lastState,action,actualState,H):
        if (actualState == None):
            return self.h(lastState)
        else:
            return 1 +H[actualState]

    def h(self, state):
        return self.model.h(state, self.goalId)

    
