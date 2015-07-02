from UltimateStrat.Executor.Executor import Executor
import UltimateStrat.Hub as Hub

__author__ = 'jbecirovski'


class TacticExecutor(Executor):
    """
    TacticExecutor is a sequence of request that select skill for each players
    1 - what's player tactic ?
    2 - get specific tactic from tactic book
    3 - select skill, target, goal from tactic object
    4 - set skill, target, goal
    """
    def __init__(self):
        Executor.__init__(self)

    def exec(self):
        # Execution for each players
        for id_player in range(Hub.getCountPlayer()):

            # 1 - what's player tactic ?
            current_tactic = Hub.getPlayerTactic(id_player)

            # 2 - get specific tactic from tactic book
            tactic = self.tactic_book[current_tactic]

            # 3 - select skill, target, goal from tactic object
            action = tactic().apply(Hub, id_player)

            # 4 - set skill, target, goal
            Hub.setPlayerSkillTargetGoal(id_player, action)


