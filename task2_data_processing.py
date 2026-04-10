import os
import pandas as pd

df = pd.read_json('data/trends_20260409.json')
print(f'Loaded {df.shape[0]} stories from data/trends_20260408.json')

# cleaning the data

# duplicates identifying with post id
total_duplicates = df.duplicated(subset='post_id').sum()

# dropping the duplicates with same post id
df.drop_duplicates(subset='post_id', inplace=True)

# checking df size after dropping the duplicates
print(f'After removing duplicates:{df.shape[0]}')

# Missing values — drop rows where post_id, title, or score is missing

df = df.dropna(subset=['post_id','title', 'score'])
print(f'After removing nulls:{df.shape[0]}')

# Converting score and num_comments to integer type
df[['score', 'num_comments']] = df[['score', 'num_comments']].astype(int)

# Removing the stories with low scores
df  = df[df['score'] >= 5]
df['title'] = df['title'].astype(str).str.strip('')
print(f'After removing low scores:{df.shape[0]}')

os.makedirs('data', exist_ok = True)
with open('data/trends_clean.csv', 'w') as f:
    df.to_csv(f, index=False)

print(f'Saved {df.shape[0]} rows to data/trends_clean.csv')
print(df.groupby('category').size().rename_axis('Stories per category:').to_string())
