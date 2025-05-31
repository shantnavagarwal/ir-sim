from irsim.world import ObjectBase


class RobotDiff(ObjectBase):
    def __init__(
        self, color="g", state_dim=3, **kwargs
    ):
        super(RobotDiff, self).__init__(
            role="robot",
            color=color,
            state_dim=state_dim,
            **kwargs,
        )

        assert (
            state_dim >= 3
        ), "for differential robot, the state dimension should be greater than 3"


    def plot(self, ax, **kwargs):

        show_goal = self.plot_kwargs.get("show_goal", True)
        show_arrow = self.plot_kwargs.get("show_arrow", True)

        super().plot(ax, show_goal=show_goal, show_arrow=show_arrow, **kwargs)


class RobotDiffQafka(RobotDiff):
    def __init__(self, id='ll_1', color="g", state_dim=3, **kwargs):
        super(RobotDiffQafka, self).__init__(color, state_dim, **kwargs)
        
        self.id = id
        self.goal_id = None
    
    def set_trajectory(self, goal_id, waypoints):
        """
        Function to set highlevel trajectory of the Qafka TwistBot
        """
        self.goal_id = goal_id
        # Calculate trajectory based on state and waypoints
        # call self.set_goal with trajectory. trajectory of goals at fixed dt of world
        pass

    def get_waypoints(self, next_goal):
        # Get's the trajectory robot has to follow
        pass
        