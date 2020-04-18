import mazeEnvExtended
import time
import traceback
from agent import Agent
from model import Model
from agentUCS import AgentUCS
from modelExt import ModelExt
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'gym_maze\envs\maze_samples\Maze10x10_1.txt')

envs = [
    (mazeEnvExtended.MazeEnv10x10_1, "MazeEnv10x10_1")
]

agents = [
    #(Agent, "InputAgent")
    (AgentUCS, "UCS")
    #(AgentA, "A"),
    #(AgentLRTA, "LRTA"),
]

models = [
    #(Model, "GoalModel"),
    (ModelExt, "GoalModelExt")
]

def main():

    for env, e_name in envs:
        for agent, a_name in agents:
            for model, m_name in models:
                print(e_name, a_name, m_name)
                try:  
                    run(env(), agent(model(filename)))
                except Exception as e:
                    print(str(e))
                    print(traceback.format_exc())
                print("------------")
            print("-----------------------")
        print("-----------------------------------")

def run(env, agent):
    try:
        _prepare_env(env)

        start_time = time.time()
        print("Starting:", start_time)
        wins, step_counter = agent.run(env)
        print("--- %s seconds ---" % (time.time() - start_time))
        print("Catched:", wins, "Steps:", step_counter)
    finally:
        print("deleting env")
        del env

def _prepare_env(env):
    env.reset()
    env.should_trace_location(True)

if __name__ == "__main__":
    main()


