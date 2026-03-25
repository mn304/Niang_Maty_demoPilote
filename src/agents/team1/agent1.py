from pathlib import Path
import numpy as np
import random
from utils.track_utils import compute_curvature, compute_slope
from omegaconf import OmegaConf

from agents.kart_agent import KartAgent
from agents.team1.agent_center import AgentCenter
from agents.team1.agent_speed import AgentSpeed
from agents.team1.agent_obstacles import AgentObstacles
from agents.team1.agent_rescue import AgentRescue
from agents.team1.agent_items import AgentItems
from agents.team1.agent_drift import AgentDrift

class Agent1(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "agant1"

        path_conf = Path(__file__).resolve().parent
        path_conf = str(path_conf) + '/ConfigFileTeam1.yaml'   #Chemin du fichier de configuration
        self.conf = OmegaConf.load(path_conf)                           #Importation du fichier de configuration

        self.agentCenter = AgentCenter(env, self.conf, self.path_lookahead)
        self.agentSpeed = AgentSpeed(env, self.conf, self.agentCenter, self.path_lookahead)
        self.agentObstacles = AgentObstacles(env, self.conf, self.agentSpeed, self.path_lookahead)
        self.agentRescue = AgentRescue(env, self.conf, self.agentObstacles)
        self.agentItems = AgentItems(env, self.conf, self.agentRescue)
        self.AgentDrift = AgentDrift(env, self.conf, self.agentItems)

    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
    
        self.compteur_pas += 1
        # On braque à fond avec l'accélérateur et le drift pour pivoter
        if self.compteur_pas <= 50:
            return {
                "acceleration": 1.0,
                "steer": 1.0,         # Braque à droite toute
                "brake": False,
                "drift": True,        # Drift pour tourner sur place
                "nitro": False,
                "rescue": False,
                "fire": False
            }
        else:
            
            direction = 0.0 

            return {
                "acceleration": 0.0,  
                "steer": direction,   
                "brake": True,        
                "drift": False,
                "nitro": False,
                "rescue": False,
                "fire": False
            }

    




    

    