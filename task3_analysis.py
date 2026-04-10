import pandas as pd
import numpy as np

df = pd.read_csv('data/trends_clean.csv', encoding='latin-1')
pd.set_option('display.max_columns', None)
print(f'Loaded data: {df.shape}')
print(f'First 5 rows: \n {df.head(5)}')
print(f'Average score   : {int(df['score'].mean())}')
print(f'Average comments:{int(df['num_comments'].mean())}')


# Basic Analysis with numpy
print('--- NumPy Stats ---')
print(f'Mean score   : {np.mean(df['score'])}')
print(f'Median score : {np.median(df['score'])}')
print(f'Std deviation: {np.std(df['score'])}')
print(f'Max score    : {np.max(df['score'])}')
print(f'Min score    : {np.min(df['score'])}')

top_category = df.groupby('category').size().idxmax()
count =  df.groupby('category').size().max()
print(f'Most stories in: {top_category} ({count} stories)')
top = df.loc[df['num_comments'].idxmax()]
print(f'Most commented story: {top['title']}  — {top['num_comments']} comments')

df.to_csv('data/trends_analysed.csv', index=False, encoding='utf-8')
print('Saved to data/trends_analysed.csv')