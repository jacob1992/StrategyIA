from UltimateStrat.Executor.Executor import Executor
import UltimateStrat.Hub as Hub

__author__ = 'jbecirovski'


class SkillExecutor(Executor):
    """
    SkillExecutor is a sequence of request that select next pose for each players
    1 - what's player skill ?
    2 - what's player target ?
    3 - what's player goal ?
    4 - get skill object
    5 - generate next pose
    6 - set next pose
    """
    def __init__(self):
        Executor.__init__(self)

    def exec(self):
        # Execution for each players
        for id_player in range(Hub.getCountPlayer()):
            # 1 - what's player skill ?
            current_skill = Hub.getPlayerSkill(id_player)

            # 2 - what's player target ?
            current_target = Hub.getPlayerTarget(id_player)

            # 3 - what's player goal ?
            current_goal = Hub.getPlayerGoal(id_player)

            # 4 - get skill object
            skill = self.skill_book[current_skill]

            # 5 - generate next pose
            next_pose = skill().act(Hub.getPlayerPose(id_player), current_target, current_goal)

            # 6 - set next pose
            Hub.setPlayerNextPose(id_player, next_pose)
