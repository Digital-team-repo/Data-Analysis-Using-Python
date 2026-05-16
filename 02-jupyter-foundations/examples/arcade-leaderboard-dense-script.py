import random
from statistics import mean

import matplotlib.pyplot as plt

players = ["Avery", "Jordan", "Kai", "Mina", "Riley", "Sasha"]
scores = [random.randint(1200, 3800) for _ in players]
bonus_round = [random.randint(-300, 500) for _ in players]
final_scores = [s + b for s, b in zip(scores, bonus_round)]
ranked = sorted(zip(players, final_scores), key=lambda x: x[1], reverse=True)

print("Arcade Night Leaderboard")
for i, (name, score) in enumerate(ranked, start=1):
    print(f"{i}. {name}: {score}")

print(f"\nClass average score: {mean(final_scores):.1f}")
print(f"Top score gap: {ranked[0][1] - ranked[-1][1]}")

names = [n for n, _ in ranked]
values = [v for _, v in ranked]
colors = ["#1f77b4" if i == 0 else "#8fb9e3" for i in range(len(values))]

plt.figure(figsize=(8, 4))
plt.bar(names, values, color=colors)
plt.title("Arcade Night Final Scores")
plt.ylabel("Points")
plt.xlabel("Player")
plt.tight_layout()
plt.show()
