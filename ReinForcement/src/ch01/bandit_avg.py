import numpy as np
import matplotlib.pyplot as plt


class Bandit():
    def __init__(self,arms=10):
        self.arms = arms
        self.rates = np.random.rand(arms)

    def play(self, arm):
        rate = self.rates[arm]
        self.rates += 0.1 * np.random.randn(self.arms)
        if rate > np.random.rand():
            return 1
        else:
            return 0

class Agent():
    def __init__(self,epsilon,action_size=10):
        self.epsilon =  epsilon
        self.Qs = np.zeros(action_size)
        self.ns = np.zeros(action_size)

    def update(self,action, reward):
        self.ns += 1
        self.Qs[action] += (reward - self.Qs[action])/self.ns[action]


    def get_action(self):
        if self.epsilon > np.random.rand():
            return np.random.randint(0,len(self.ns))
        else:
            return np.argmax(self.Qs)

            




runs = 200
steps = 1000
epsilon = 0.05
all_rates = np.zeros((runs,steps))

for run in range(runs):
    #初期化
    bandit = Bandit()
    agent  = Agent(epsilon)
    total_reward = 0
    rates=[]

    #処理
    for step in range(steps):
        action = agent.get_action()
        reward = bandit.play(action)
        agent.update(action, reward)
        total_reward += reward
        rates.append(total_reward / (step+1))

    #結果の保存
    all_rates[run] = rates

avg_rates = np.average(all_rates, axis=0)

plt.ylabel("Rates")
plt.xlabel("Steps")
plt.plot(avg_rates)
plt.savefig("rates_avg.jpg")