import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# -----------------------------
# 1. Load datasets
# -----------------------------

# Load weekly rating
rating = pd.read_csv("Rating - Uzak Şehir.csv")
rating['Day'] = pd.to_datetime(rating['Day'] + " 2025", format="%d %B %Y")
rating = rating.sort_values("Day")

# Load TikTok
tiktok = pd.read_csv("Uzak Şehir - TikTok.csv")
tiktok['Date'] = pd.to_datetime(tiktok['Date'], dayfirst=True)
tiktok['Week'] = tiktok['Date'].dt.to_period('W').apply(lambda r: r.start_time)
tiktok_weekly = tiktok.groupby('Week')[['Like', 'View']].sum().reset_index()

# Load Instagram
insta = pd.read_csv("Uzak Şehir - Insta.csv")
insta['Date'] = pd.to_datetime(insta['Date'], dayfirst=True)
insta['Week'] = insta['Date'].dt.to_period('W').apply(lambda r: r.start_time)
insta_weekly = insta.groupby('Week')[['Like', 'View']].sum().reset_index()

# Load Google Trends
trends = pd.read_csv("Trends - Uzak Şehir.csv", skiprows=1)
trends.columns = ['Day', 'Search Volume']
trends['Day'] = pd.to_datetime(trends['Day'])
trends['Week'] = trends['Day'].dt.to_period('W').apply(lambda r: r.start_time)
trends_weekly = trends.groupby('Week')['Search Volume'].mean().reset_index()

# -----------------------------
# 2. Merge datasets on week
# -----------------------------

# Rating'e week bilgisi ekle
rating['Week'] = rating['Day'].dt.to_period('W').apply(lambda r: r.start_time)

# Rename for merge clarity
rating = rating.rename(columns={"All People": "TV Rating"})

# Merge everything
df = rating[['Week', 'TV Rating']].merge(tiktok_weekly, on='Week', how='left', suffixes=('', '_TikTok'))
df = df.merge(insta_weekly, on='Week', how='left', suffixes=('', '_Insta'))
df = df.merge(trends_weekly, on='Week', how='left')

df.columns = ['Week', 'TV Rating', 'TikTok Likes', 'TikTok Views', 'Instagram Likes', 'Instagram Views', 'Google Search Volume']

# Drop weeks with missing values in any column
df_clean = df.dropna()

# -----------------------------
# 3. Correlation heatmap
# -----------------------------

plt.figure(figsize=(10, 6))
sns.heatmap(df_clean.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Between TV Rating and Social Media Metrics")
plt.tight_layout()
plt.show()

# -----------------------------
# 4. Time series plot
# -----------------------------

plt.figure(figsize=(12, 6))
sns.lineplot(x='Week', y='TV Rating', data=df_clean, label='TV Rating', marker='o')
sns.lineplot(x='Week', y='TikTok Likes', data=df_clean, label='TikTok Likes', marker='o')
sns.lineplot(x='Week', y='Instagram Likes', data=df_clean, label='Instagram Likes', marker='o')
sns.lineplot(x='Week', y='Google Search Volume', data=df_clean, label='Google Search', marker='o')
plt.title("Weekly Trend Comparison: TV Rating vs Social Media")
plt.xlabel("Week")
plt.ylabel("Engagement / Rating")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# -----------------------------
# 5. Hypothesis test (Pearson)
# -----------------------------

corr, pval = pearsonr(df_clean["TV Rating"], df_clean["TikTok Likes"])
print(f"\n📈 Pearson Correlation between TV Rating and TikTok Likes:")
print(f"Correlation coefficient: {corr:.3f}")
print(f"P-value: {pval:.4f}")

if pval < 0.05:
    print("✅ There is a statistically significant relationship.")
else:
    print("❌ No statistically significant relationship found.")
