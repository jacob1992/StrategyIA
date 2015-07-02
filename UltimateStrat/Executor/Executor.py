from abc import abstractmethod
import UltimateStrat.Hub as Hub
from UltimateStrat.STP.Skill.SkillBase import SkillBase
from UltimateStrat.STP.Tactic.TacticBase import TacticBase
from UltimateStrat.STP.Play.PlayBase import PlayBase

__author__ = 'jbecirovski'


class Executor:
    def __init__(self):
        self.play_book = PlayBase()
        self.tactic_book = TacticBase()
        self.skill_book = SkillBase()

    @abstractmethod
    def exec(self):
        pass
