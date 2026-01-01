import gym
from gym import spaces
import numpy as np

class AgriTwinEnv(gym.env):
    """
    Custom Gym Environment for Agri-Twin irrigation control.
    """

    MAX_IRRIGATION_MM = 50.0

    def __init__(self):
        super.__init__()
        self.action_spaces = spaces.Box(
            low = 0.0,
            high = 50.0,
            shape = (1,),
            dtype = np.float32

        )

        self.observation_space = spaces.Box(
            low = 0.0,
            high = 1.0,
            shape = (4,),
            dtype = np.float32
        )

        # Internal (real-world) state
        self.soil_moisture = 0.5
        self.heat_stress = 0.0
        self.rainfall = 0.0
        self.crop_stage = 0.1
    

    def reset(self):
        self.soil_moisture = 0.5
        self.heat_stress = 0.0
        self.rainfall = 0.0
        self.crop_stage = 0.1

        observation = np.array([
            self.soil_moisture,
            self.heat_stress,
            self.rainfall,
            self.crop_stage 
        ], dtype = np.float32)


        return observation



    def step(self, action):
        # Convert normalized action to irrigation in mm
        irrigation_mm = action[0] * self.MAX_IRRIGATION_MM 

        # Simple water balance
        water_input = (irrigation_mm/ self.MAX_IRRIGATION_MM) + self.rainfall
        self.soil_moisture += water_input

        # Clamp soil moisture betweeen [0,1]
        self.soil_moisture = np.clip(self.soil_moisture, 0.0, 1.0)

        # Heat stress dynamics
        if self.soil_moisture < 0.3:
            self.heat_stress += 0.05
        else:
            self.heat_stress -= 0.03

        #  Clamp heat stress between [0,1]
        self.heat_stress = np.clip(self.heat_stress, 0.0, 0.1)

        # Crop stage
        growth_rate = 0.02 * (1.0 - self.heat_stress)
        self.crop_stage += growth_rate

        self.crop_stage = np.clip(self.crop_stage, 0.0, 1.0)

        
