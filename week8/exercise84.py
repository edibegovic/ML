
import numpy as np
import random

# Initialize
Q = np.zeros([4, 5, 4])
rewards = np.zeros([4, 5])
rewards[3, 4] = 100
pos = [0, 0]
goal_pos = [3, 4]
epsilon = 0.9
lr = 0.2
dr = 0.5

def next_action():
    if random.uniform(0, 1) < epsilon:
        return random.randint(0, len(Q[pos[0], pos[1]])-1)
    else:
        return np.argmax(Q[pos[0], pos[1]])

def move(action):
    if action == 0 and pos[0] is not 0:
        return [pos[0] - 1, pos[1]]
    elif action == 1 and pos[0] is not 3:
        return [pos[0] + 1, pos[1]]
    elif action == 2 and pos[1] is not 0:
        return [pos[0], pos[1] - 1]
    elif action == 3 and pos[1] is not 4:
        return [pos[0], pos[1] + 1]
    else:
        return pos

for _ in range(100):
    # print(_)
    pos = [0, 0]
    while pos != goal_pos:
        prev_pos = pos
        action = next_action()
        pos = move(action)
        Q[prev_pos[0], prev_pos[1], action] += lr * (rewards[pos[0], pos[1]] + 
                dr * np.max(Q[pos[0], pos[1], :]) - 
                Q[prev_pos[0], prev_pos[1], action]) 


# Pretty print 🌈
%clear
mapping = ["🎉", "↓", "←", "→"]
out = '\n'.join(([' '.join(k) 
      for k in np.array([mapping[np.argmax(a)]
      for a in Q.reshape(20, 4)])
      .reshape(4, 5)]))
print(out)
