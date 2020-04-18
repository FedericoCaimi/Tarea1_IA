from abc import ABC, abstractmethod
from queue import PriorityQueue
from priorityQueue import PriorityQueue
import time
#from queue import Queue

#DO NOT CHANGE THIS CLASS: EXTEND IT WITH YOUR OWN
class AgentUCS():

    def __init__(self, model):
        super().__init__()
        self.model = model

    def run(self, env):
        self.model.reset()
        return self.loop(env)

    def loop(self, env):
        print("UCS...")
        env.render()
        done = False
        step_counter = 0
        all_rewards = 0
        initialState = 0
        while not done:  
            goalId = self.model.get_goal(step_counter)[0]
            actions = ['N','E','S','W']
            resultado = self.searchUCS(initialState,goalId,actions)
            camino = []
            camino = self.camino(resultado,initialState,str(goalId))
            
            for i in range(len(camino)):
                time.sleep(0.5)
                goalIdNow = self.model.get_goal(step_counter)[0]
                env.set_goal(goalIdNow)
                if goalIdNow != goalId:
                    nodeAction = str(actionEstado[1])+actionEstado[0]
                    initialState = self.model.diccionary[nodeAction]
                    break
                actionEstado = camino.pop()
                self.check_action(actionEstado[0])
                obs, reward, done_env, _ = env.step(actionEstado[0])
                all_rewards += reward
                done = done_env and self.model.is_win_goal()
                env.render()
                step_counter += 1
        return all_rewards, step_counter

    def next_action(self, step_counter, env):
        goalId = self.model.get_goal(step_counter)[0]
        env.set_goal(goalId)
        return input()

    def check_action(self, action):
        if action not in ['N','E','S','W']:
            raise ValueError("Run Ended - Invalid Action")

    def step(self,node,action):
        estado = node[0]
        nodeAction = str(estado)+action
        actionCost = 1
        return self.model.diccionary[nodeAction],actionCost

    def searchUCS(self,initialState, goal, actions):
        to_explore = PriorityQueue()
        explored = set()
        prevNode = dict()
        prevNode[initialState] = None
        to_explore.push(initialState,0)
        while (not(to_explore.is_empty())):
            node = to_explore.pop()#get()
            to_explore.remove(node)
            if (node[0] == str(goal)):
                return prevNode #node, prevNode
            explored.add(node[0])

            for action in actions:
                child, actionCost = self.step(node, action)
                cost = node[1] + actionCost
                booleano = child in to_explore
                if not(child in explored or child in to_explore):
                    to_explore.push(child,cost)
                    prevNode[child] = str(node[0])+action
                elif (child in to_explore and cost < to_explore.getCost(child)):
                    to_explore.update(child, cost)
                    prevNode[child] = str(node[0])+action
        return None
    #obtengo el resultado 
    def camino(self,dicc,initialState,goal):
        done = False
        stack = []
        while not done:
            stateAction = dicc[goal]
            state = stateAction[0:len(stateAction)-1]
            action = stateAction[len(stateAction)-1:len(stateAction)]
            goal = state
            stack.append([action,state])
            if (state == str(initialState)):
                done = True
        return stack

       

    
