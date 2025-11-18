class FinancialGoal:

    def __init__(self, goal, achieved, user_settings):
        self.goal = goal
        self.achieved = achieved

    def set_goal(self, goal):
        self.goal = goal

    def set_achieved(self, achieved):
        self.achieved = achieved

    def get_goal(self):
        return self.goal

    def get_achieved(self):
        return self.achieved

    def to_string(self):
        return f'Goal: {self.goal} | Achieved: {self.achieved}'