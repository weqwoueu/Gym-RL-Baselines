import gymnasium as gym
from stable_baselines3 import PPO
# 1. 创建带画面的环境
env = gym.make("Hopper-v4", render_mode="human")

#加载刚刚训练好的模型
modle = PPO.load("ppo_Hopper-v4")


#初始化环境（reset）
# observation 是初始状态：[小车位置, 小车速度, 杆角度, 杆角速度]
observation,info = env.reset()
print("AI接管中...(ctrl + c停止)")

while True:
    # 4. 让模型预测动作
    # model.predict 会返回两个值，我们只需要第一个 action
    # deterministic=True: 考试模式，不要随机探索，选概率最大的动作
    action , _states = modle.predict(observation , deterministic=True)
    # 5. 执行动作
    observation, reward , terminated , truncated ,info = env.step(action)

    if terminated :
        observation,info = env.reset()

env.close()

