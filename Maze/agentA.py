from agent import Agent
from priorityQueue import PriorityQueue
from abc import ABC, abstractmethod
import time

#DO NOT CHANGE THIS CLASS: EXTEND IT WITH YOUR OWN
class AgentA(Agent):

    def __init__(self, model):
        super().__init__(model)
        self.goal = None
        self.sequenceStep = None
        self.sequence = None
        self.actualPosition = 0

    def loop(self, env):
        print("Play AgentA...")
        env.render()
        done = False
        step_counter = 0
        all_rewards = 0
        
        while not done:  
            action = self.next_action(step_counter, env)
            self.check_action(action)
            obs, reward, done_env, _ = env.step(action)
            all_rewards += reward
            done = done_env and self.model.is_win_goal()
            env.render()
            step_counter += 1
        
        return all_rewards, step_counter

    def next_action(self, step_counter, env):
        goalId = self.model.get_goal(step_counter)[0]
        env.set_goal(goalId)

        if(self.goal != goalId):
            self.goal = goalId
            self.sequence = self.getSequence(self.actualPosition, self.goal)
            a = self.sequence
            print(a)
            self.sequenceStep = 0
        
        if(self.sequenceStep + 1 < len(self.sequence)):
            self.actualPosition = self.sequence[self.sequenceStep + 1][0]
        _return = self.sequence[self.sequenceStep][1]
        self.sequenceStep += 1
        print(self.actualPosition)
        time.sleep(0.5)
        return _return

    def getSequence(self, position, goal):
        dictionary = self.performAStar(position, goal)
        actualNode = goal
        sequence = []
        while(actualNode != position):
            previousNode = dictionary[actualNode]
            sequence.append(previousNode)
            actualNode = previousNode[0]
        
        sequence.reverse()
        return sequence


    def performAStar(self, position, goal):
        to_explore = PriorityQueue()
        explored = set()
        prevNode = dict({position: 0})
        costs = dict({position: 0})

        to_explore.push(position, 0 + self.model.h(position, goal))
        stepCounter = 0

        while (not(to_explore.is_empty())):
            node = to_explore.pop()[0]
            to_explore.remove(node)
            if (goal == node):
                return prevNode
            explored.add(node)

            actions = ['N','S','E','W']

            for action in actions:
                child, actionCost = self.step(node, action)
                if not(child == node):
                    prevCost = costs[node] + actionCost
                    cost = prevCost + self.model.h(child, goal)

                    if not(child in explored or child in to_explore):
                        to_explore.push(child, cost)
                        costs[child] = prevCost
                        prevNode[child] = (node, action)
                    elif child in to_explore and cost < to_explore.getCost(child):
                        to_explore.update(child, cost)
                        costs[child] = prevCost
                        prevNode[child] = (node, action)
        return None

    def step(self, node, action):
        nodeAction = str(node)+action
        actionCost = 1
        return int(self.model.diccionary[nodeAction]),actionCost