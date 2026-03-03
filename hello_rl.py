import gymnasium as gym
import time

#创建倒立摆环境(CartPole-v1)
# render_mode="human": 意思是把动画弹窗显示出来给我们看
env = gym.make("Hopper-v4" ,render_mode="human")

#初始化环境（reset）
# observation 是初始状态：[小车位置, 小车速度, 杆角度, 杆角速度]
observation,info = env.reset()

print("开始乱动")
for _ in range(1000):
    # 因为我们在 make 里设置了 human，这里它会自动画图，不用手动调 render()
     # action_space.sample(): 随机瞎选 (0是向左推, 1是向右推)
     action = env.action_space.sample()
 # 5. 执行一步 (Step) -> 核心交互协议
    # 告诉环境：我要用这个力矩推车！
    # 环境返回 5 个值：
    # - observation: 推完之后，现在车和杆的状态
    # - reward: 奖励 (这步得了多少分？坚持住就是 +1)
    # - terminated: 是不是挂了？(杆子倒了/车跑出屏幕了)
    # - truncated: 是不是超时了？(比如坚持了 500 帧都没倒)
    # - info: 调试信息
     observation, reward , terminated , truncated ,info = env.step(action)

     time.sleep(0.05)#慢一点好看

     if terminated or truncated:
          print("倒了，重置")
          observation,info = env.reset()
env.close()

###cheshi

