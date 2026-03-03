import numpy as np
import matplotlib.pyplot as plt

sampleSpace = {1,2,3,4,5,6}

# Each dice face
x = np.array(list(sampleSpace))

# Probability for each face
y = np.ones(len(x)) / len(sampleSpace)

plt.stem(x, y)   # better for discrete probability
plt.xlabel("Dice Outcome")
plt.ylabel("Probability")
plt.title("Probability Distribution of Fair Dice")
plt.show()