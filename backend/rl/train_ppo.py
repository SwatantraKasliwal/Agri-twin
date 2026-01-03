from agritwin_env import AgriTwinEnv
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3 import PPO
import numpy as np

env = make_vec_env(AgriTwinEnv, n_envs = 1)
state = env.reset()
print("Initial state: ", state)

random_action = env.action_space.sample()
next_state, reward, done, info = env.step(random_action)
print("Next state: ", next_state)
print("Reward: ", reward)

model = PPO(
    policy = "MlpPolicy",
    env = env,
    verbose = 1,
    learning_rate = 3e-4,
    n_steps = 2048,
    batch_size = 64

)

model.learn(total_timesteps = 100_000)
model.save("ppo_agritwin")

print(model.policy)