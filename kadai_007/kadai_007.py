import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib as jplt

df = pd.read_csv('sample_pandas_6.csv')
category_df = pd.read_csv('category.csv')

df = pd.merge(df, category_df[['商品番号', 'カテゴリー']], how='inner', on='商品番号')

cat= df['カテゴリー'].value_counts()
print(cat)

plt.bar(cat.index, cat.values)
plt.xlabel('カテゴリー')
plt.ylabel('出現頻度')
plt.title('カテゴリー別の出現頻度')
plt.xticks(rotation=45)
print(plt.show())

quantity_desc = df.groupby('商品番号')['カテゴリー'].describe()
print(quantity_desc)