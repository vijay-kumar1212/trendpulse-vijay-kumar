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

# Chart 3: Score vs Comments
df['is_popular'] = df['score'] >= df['score'].median()
pop = df[df['is_popular']]
non_pop = df[~df['is_popular']]

plt.figure(figsize=(10, 6))
plt.scatter(non_pop['score'], non_pop['num_comments'], alpha=0.5, label='Not Popular')
plt.scatter(pop['score'], pop['num_comments'], alpha=0.5, label='Popular')
plt.xlabel('Score')
plt.ylabel('Number of Comments')
plt.title('Score vs Comments (Popular vs Non-Popular)')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/chart3_scatter.png')
plt.show()
plt.close()


# dashboard
fig, axes = plt.subplots(2, 2, figsize=(18, 12))
fig.suptitle('TrendPulse Dashboard', fontsize=16)

# Chart 1
axes[0, 0].barh(titles, top10['score'])
axes[0, 0].set_xlabel('Score')
axes[0, 0].set_ylabel('Story Title')
axes[0, 0].set_title('Top 10 Stories by Score')

# Chart 2
axes[0, 1].bar(x, y, color=plt.cm.tab10.colors[:len(x)])
axes[0, 1].set_xlabel('Categories')
axes[0, 1].set_ylabel('Number of Stories')
axes[0, 1].set_title('Stories per Category')

# Chart 3
axes[1, 0].scatter(non_pop['score'], non_pop['num_comments'], alpha=0.5, label='Not Popular')
axes[1, 0].scatter(pop['score'], pop['num_comments'], alpha=0.5, label='Popular')
axes[1, 0].set_xlabel('Score')
axes[1, 0].set_ylabel('Number of Comments')
axes[1, 0].set_title('Score vs Comments (Popular vs Non-Popular)')
axes[1, 0].legend()

axes[1, 1].axis('off')

plt.tight_layout()
plt.savefig('outputs/dashboard.png')
plt.show()
plt.close()
