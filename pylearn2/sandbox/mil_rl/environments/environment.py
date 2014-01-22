class Environment():
    """
    A class representing a environment that maintains a state,
    provides observations to an Agent, and updates its state
    based on actions performed by an Agent.

    Structure and methods are inspired by the dotRL project.
    """
    #def setup():
    #    raise NotImplementedError()

    def get_current_state(self):
        """
        Returns the current state of the environment.
        """
        raise NotImplementedError()

    def perform_action(self, action):
        """
        Takes an action and updates the state accordingly.
        Returns a reward for the performed action.
        """
        raise NotImplementedError()
