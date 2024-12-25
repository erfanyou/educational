from math import factorial as fac
from pprobs.distribution import Joint
import matplotlib.pyplot as plt

def comb(n, k):
    """Calculate the number of combinations (n choose k)."""
    if k > n or n < 0 or k < 0:
        return 0
    return fac(n) // (fac(k) * fac(n - k))

def prob(g, b):
    """Calculate the probability of drawing g green balls and b blue balls."""
    # Ensure that the constraints match the problem
    if (g > 2 or b > 3) or (g + b > 3):
        return 0
    return (comb(2, g) * comb(3, b) / comb(4, 3 - g - b)) / comb(9, 3)

# Create the joint distribution
dist = Joint(prob, range(0, 5), range(0, 5))

# Display the probability table
print(dist.probability_table())


ax=plt.figure(dpi=100,figsize=(6,6)).add_subplot(projection='3d')

for i in range(5):
    for j in range(5):
        ax.scatter(i, j, dist.prob(i, j), c='r', marker='o')
plt.show()


# marginal distribution
print(round(dist.get_prob(2,range(0,5)),3))
print(round(dist.get_prob(range(0,5),range(0,5)),3))
