class FinancialGoal:

    def __init__(self, goal, achieved, user_settings):
        self.goal = goal
        self.achieved = achieved
        self.user_settings = user_settings

    def set_goal(self, goal):
        self.goal = goal

    def set_achieved(self, achieved):
        self.achieved = achieved

    def set_user_settings(self, user_settings):
        self.user_settings = user_settings

    def get_goal(self):
        return self.goal

    def get_achieved(self):
        return self.achieved

    def get_user_settings(self):
        return self.user_settings
