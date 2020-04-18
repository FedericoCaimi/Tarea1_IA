from abc import ABC, abstractmethod

#DO NOT CHANGE THIS CLASS: EXTEND IT WITH YOUR OWN
class Agent():

    def __init__(self, model):
        super().__init__()
        self.model = model

    def run(self, env):
        self.model.reset()
        return self.loop(env)

    def loop(self, env):
        print("Play manually...")
        env.render()
        done = False
        step_counter = 0
        all_rewards = 0
        
        while not done:  
            self.model.map_obs_to_state(env.observation)
            action = self.next_action(step_counter, env)
            self.check_action(action)
            obs, reward, done_env, _ = env.step(action)
            all_rewards += reward
            done = done_env and self.model.is_win_goal()
            #print(self.model.diccionary)
            #self.model.map_obs_to_state(obs)
            env.render()
            step_counter += 1
        return all_rewards, step_counter

    def next_action(self, step_counter, env):
        goalId = self.model.get_goal(step_counter)[0]
        env.set_goal(goalId)
        return input()

    def check_action(self, action):
        if action not in ["N", "E", "S", "W"]:
            raise ValueError("Run Ended - Invalid Action")