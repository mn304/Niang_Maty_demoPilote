import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent

class Agent7(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "Niang_maty" # changement de mon nom  sur le kart  

    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    def endOfTrack(self):
        return self.isEnd




    

    def choose_action(self, obs):
        # on introduit un compteur de pas 
        self.compteur_pas = 0 
        #on ajoute 1 au compteur a chaque fois 
        self.compteur_pas += 1

        if self.compteur_pas <= 200:
            return {
                "acceleration": 1.0,  
                "steer": 0.0,         
                "brake": False,       
                "drift": False,
                "nitro": False,
                "rescue": False,
                "fire": False
            }
        elif self.compteur_pas <= 500:
            return {
                "acceleration": 0.0,  # On n'accélère plus en avant
                "steer": 0.0,         
                "brake": True,        # Le frein maintenu 
                "drift": False,
                "nitro": False,
                "rescue": False,
                "fire": False
            }
        else:
            return {
                "acceleration": 0.0,  
                "steer": 0.0,         
                "brake": True,        # On freine juste pour rester sur place
                "drift": False,
                "nitro": False,
                "rescue": False,
                "fire": False
            }
        
    


    



    