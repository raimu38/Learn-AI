import numpy as np

class Bandit:
    def __init__(self, arms=10):
        self.rates = np.random.rand(arms)
    
    def play(self, arm):
        rate = self.rates[arm]
        if rate > np.random.rand():
            return 1
        else:
            return 0



class Agent:
    def __init__(self,epsilon, action_size = 10):
        self.epsilon = epsilon
        self.Qs = np.zeros(action_size)
        self.ns = np.zeros(action_size)

    def update(self, action, reward):
        self.ns[action] += 1
        self.Qs[action] += (reward - self.Qs[action])/self.ns[action]

    def get__ation(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(0,len(self.Qs))
        return np.argmax(self.Qs)
    

import matplotlib.pyplot as plt

steps = 1000
epsilon = 0.1

bandit = Bandit()
agent = Agent(epsilon)
total_reward = 0
total_rewards = []
rates = []


for step in range(steps):
    action = agent.get__ation()
    reward = bandit.play(action)
    agent.update(action, reward)
    total_reward += reward

    total_rewards.append(total_reward)
    rates.append(total_reward / (step+1))

print(total_reward)


plt.ylabel('Total reward')
plt.xlabel('Steps')

plt.plot(total_rewards)
plt.savefig("reward.jpg")

plt.clf()
plt.ylabel('Rates')
plt.xlabel('Steps')
plt.plot(rates)
plt.savefig("steps.jpg")


# bandit1 = Bandit()

# for i in range(3):
#     print(bandit1.play(0))

# print(f"0番目のスロットの勝率は{bandit1.rates[0]}ですね")

# Q = 0
# bandit = Bandit()
# print(f"rate:{bandit.rates[0]}")
# for n in range(1,100):
#     reward = bandit.play(0)
#     Q = (reward - Q)/n + Q
# print(f"Q:{Q}")

# Qs = np.zeros(10)
# ns = np.zeros(10)


# for n in range(10):
#     action = np.random.randint(0,10)
#     reward = bandit.play(action)

#     ns[action] += 1
#     Qs[action] += (bandit.rates[action] - Qs[action])/ns[action]
#     print(Qs)
# print(ns)
# print(np.sum(ns))