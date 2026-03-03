import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv , VecNormalize
import os

# 训练的时候不要弹窗 (render_mode=None)，因为渲染画面会拖慢训练速度
env = gym.make("Ant-v4" ,render_mode=None)

#定义模型
# MlpPolicy: 使用全连接网络 (MLP) 作为策略网络 (相当于我们前两天学的 SimpleNet)
# env: 告诉 AI 它要在哪里玩
# verbose=1: 打印训练日志
model = PPO("MlpPolicy",env , verbose=True ,device="cpu")

print("开始训练")
# total_timesteps=10000: 让 AI 在环境里尝试 1万步
model.learn(total_timesteps=3000000)
print("训练结束")

#保存模型
model.save("ppo_Ant-v4")
print("模型保存为 ppo_Ant-v4.zip")

# 删除环境，释放内存

del model
env.close()
