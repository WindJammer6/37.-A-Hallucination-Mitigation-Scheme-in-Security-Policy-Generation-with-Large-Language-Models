import matplotlib.pyplot as plt
import numpy as np

# Data
methods = ["Baseline LLM", "Prompt Ensembling"]
correct = [0, 27]
wrong = [50, 23]

x = np.arange(len(methods))  # positions for groups
bar_width = 0.35

fig, ax = plt.subplots(figsize=(7,5))

# Bars side by side
ax.bar(x - bar_width/2, correct, bar_width, label="Correct", color="steelblue")
ax.bar(x + bar_width/2, wrong, bar_width, label="Wrong", color="indianred")

# Labels and formatting
ax.set_ylabel("Number of XML Policies", fontsize=12)
ax.set_title("Syntactic Correctness of Generated XML Policies", fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(methods, fontsize=12)
ax.set_ylim(0, 55)
ax.legend(loc="upper right", fontsize=12)

plt.tight_layout()
plt.show()
