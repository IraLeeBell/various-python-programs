# This program was shown in a YouTube video by Sari Sabaan,
# entitled "Using a Supercomputer". Published Sep 20, 2020

import random

# flip a coin a billion times
trials = 1000000000
coin = []

heads, tails = 0, 0
for amount in range(trials):
	flip = random.randint(0, 1)
	if flip == 0:
		coin.append("Heads")
	else:
		coin.append('Tails')
probability = coin.count('Heads') / len(coin)
print(probability)

