import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv , VecNormalize
import os


env = gym.make("Ant-v4" ,render_mode=None)
#嵌套一层(必须要套一层 DummyVecEnv，这是 SB3 的规定)
env = DummyVecEnv([lambda: env])

# 【关键】加上归一化包装器
# 它可以自动统计运行时的均值和方差，把 Observation 和 Reward 都归一化
env = VecNormalize(env , norm_obs=True, norm_reward=True, clip_obs=10.)

print("开始训练")
model = PPO("MlpPolicy" , env , verbose=1, device="cpu")
model.learn(total_timesteps=1000000)

#保存模型和归一化参数 (两个都要存！)
model.save("ppo_Ant-v4")
print("模型保存为 ppo_Ant-v4.zip")
env.save("vec_normalize.pkl") # <--- 必须保存这个！否则测试时数据分布不对
print("环境保存为 vec_normalize.pkl")