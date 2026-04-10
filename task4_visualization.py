import pandas as pd
import os
import matplotlib.pyplot as plt
os.makedirs('outputs', exist_ok=True)
df = pd.read_csv('data/trends_analysed.csv', encoding='latin-1')

# Chart 1: Top 10 Stories by Score

top10 = df.nlargest(10, 'score').sort_values('score')
titles = top10['title'].apply(lambda x: x[:47] + '...' if len(str(x)) > 50 else x)

plt.figure(figsize=(12, 6))
plt.barh(titles, top10['score'])
plt.xlabel('Score')
plt.ylabel('Story Title')
plt.title('Top 10 Stories by Score')
plt.tight_layout()
plt.savefig('outputs/chart1_top_stories.png')
plt.show()
plt.close()

# Chart 2: Stories per Category

cat_counts = df['category'].value_counts().to_dict()
x = list(cat_counts.keys())
y = list(cat_counts.values())
plt.figure(figsize=(12, 6))
plt.bar(x, y, color=plt.cm.tab10.colors[:len(x)])
plt.xlabel('Categories')
plt.ylabel('Number of Stories')
plt.title('Stories per Category')
plt.savefig('outputs/chart2_categories.png')
plt.show()

# Use a different colour for each bar

