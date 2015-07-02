from PythonFramework.Strategy.Strategy import Strategy
from PythonFramework.Command import Command
from UltimateStrat.Executor.CoachExecutor import CoachExecutor
from UltimateStrat.Executor.PlayExecutor import PlayExecutor
from UltimateStrat.Executor.TacticExecutor import TacticExecutor
from UltimateStrat.Executor.SkillExecutor import SkillExecutor
import UltimateStrat.Hub as Hub
import sys, time

__author__ = 'jbecirovski'

class UltimateStrategy(Strategy):
    def __init__(self, field, referee, team, opponent_team, is_team_yellow=False):
        Strategy.__init__(self, field, referee, team, opponent_team)

        # Create InfoManager
        self.team.is_team_yellow = is_team_yellow
        Hub.initialize(field, team, opponent_team)

        # Create Executors
        self.ex_coach = CoachExecutor()
        self.ex_play = PlayExecutor()
        self.ex_tactic = TacticExecutor()
        self.ex_skill = SkillExecutor()


    def on_start(self):

        Hub.update()
        # Main Strategy sequence
        self.ex_coach.exec()
        self.ex_play.exec()
        self.ex_tactic.exec()
        self.ex_skill.exec()

        # send command
        for i in range(6):
            self._send_command(Command.MoveToAndRotate(self.team.players[i], self.team, Hub.getPlayerNextPose(i)))

    def on_halt(self):
        self.on_start()

    def on_stop(self):
        self.on_start()
