import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent


class Agent6(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "niang_maty" # changment du nom du kart a mon nom et prenom 

    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    #ma fonction pour faire un tour complet 
    
    






    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
        acceleration = random.random()
        steering = random.random()
        action = {
            "acceleration": 0.2, #je met l'acceleration a 0,2 pour quon est le tour complet sans foncer au mur
            "steer": 0.9, #le volant a 0,9 pour qu'il tourne le volant le plus a gauche 
            "brake": True , 
            "drift": False,
            "nitro": bool(random.getrandbits(1)),
            "rescue":bool(random.getrandbits(1)),
            "fire": bool(random.getrandbits(1)),
        }
        return action
