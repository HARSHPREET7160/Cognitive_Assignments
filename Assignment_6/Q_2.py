import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Subjects': ['Math', 'Physics', 'Chemistry', 'Biology', 'Computer Science'],
    'Scores': [85, 90, 78, 88, 95]
}

df=pd.DataFrame(data)
sns.set_style("whitegrid")
plt.figure(figsize=(8,5))

ax = sns.barplot(x='Subjects', y='Scores', data=df, palette='husl')

for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()),
                ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.title("Scores in Different Subjects", fontsize=14)
plt.xlabel("Subjects", fontsize=12)
plt.ylabel("Scores", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()