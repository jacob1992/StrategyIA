from PythonFramework.Strategy.Strategy import Strategy
from PythonFramework.Command import Command
from PythonFramework.Util.Pose import Pose
from PythonFramework.Util.Position import Position
import random

__author__ = 'jbecirovski and felixpelletier23'

class ExampleStrategy(Strategy):
    def __init__(self, field, referee, team, opponent_team, is_team_yellow=False):
        Strategy.__init__(self, field, referee, team, opponent_team)

    def on_start(self):

        # send command
        for i in range(6):
            position = Position(random.randint(-2000, 2000), random.randint(-2000, 2000))
            self._send_command(Command.MoveToAndRotate(self.team.players[i], self.team, Pose(position)))

    def on_halt(self):
        self.on_start()

    def on_stop(self):
        self.on_start()
