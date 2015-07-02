from UltimateStrat.Executor.Executor import Executor
import UltimateStrat.Hub as Hub


__author__ = 'jbecirovski'


class CoachExecutor(Executor):
    """
    CoachExecutor is a sequence of requests that select Play for game :
    1 - what's new state ?
    2 - what's current play
    3 - what's play with new state ?
    4 - compare current play ans generate play
    5 - set play and init sequence if play is not same
    """
    def __init__(self):
        Executor.__init__(self)

    def exec(self):
        # 1 - what's current state ?
        state = Hub.getNextState()

        # 2 - what's current play
        current_play = Hub.getCurrentPlay()

        # 3 - what's play with state ?
        play = Hub.getNextPlay(state)

        # 4 - compare current play and generate play
        if not current_play == play:
            # 5 - set play and init sequence if play is not same
            Hub.setPlay(play)
            Hub.initPlaySequence()

