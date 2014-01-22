class Agent(Object):
    """
    A class representing a agent that interacts with an
    Environment and learns from experience.

    Structure and methods are inspired by the dotRL project.
    """
    #def setup():
    #    raise NotImplementedError()

    def episode_start(self):
        """
        Prepares an agent for a new episode.
        """
        raise NotImplementedError()

    def episode_end(self):
        """
        Handles the ending of an episode.
        """
        raise NotImplementedError()

    def get_action_when_not_learning(self, state):
        """
        Takes an observation and generates an action. Used
        when examining the policy of the agent, so this should
        not affect the policy.
        """
        raise NotImplementedError()

    def get_action_when_learning(self, state):
        """
        Takes an observation and generates an action. Used
        when the agent is exploring an environment and learning
        from the interactions.
        """
        raise NotImplementedError()

    def learn(self, prev_state, action, current_state, reward):
        """
        Takes a transition or sample (previous state, action,
        current state, and reward) and updates the agent's
        parameters somehow to reflect learning from this
        experience.
        """
        raise NotImplementedError()
