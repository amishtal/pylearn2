class RL_Experiment(object)
    """
    A class that represents the basic loop of a reinforcement
    learning experiment.
    """
    def __init__(self, environment, agent):
        self.environment = environment
        self.agent = agent

    def main_loop(self):
        # Set up agent and environment.
        # Get initial environment state.
        # Main Loop:
        #  Get agent action for current observation.
        #  Apply agent action to environment, getting
        #      new observation and reward.
        #  Train agent (obs, action, reward, new_obs).
        #  If episode is over:
        #    Call episode clean up functions for agent.
        #    

        while True:   # Outer training loop
            while True: #
                pass
                break
            break
