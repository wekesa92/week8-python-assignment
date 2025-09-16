import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load dataset
df = pd.read_csv("../data/metadata.csv")

# Preview
print(df.shape)
print(df.info())
df.head()

# Handle missing values
df = df.dropna(subset=['title', 'publish_time'])  # drop rows missing important info

# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# Publications per year
year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
sns.barplot(x=year_counts.index, y=year_counts.values, color="skyblue")
plt.title("Publications by Year")
plt.xticks(rotation=45)
plt.show()

# Top journals
top_journals = df['journal'].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(y=top_journals.index, x=top_journals.values, color="orange")
plt.title("Top 10 Journals")
plt.show()

# Word cloud from titles
text = " ".join(title for title in df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

