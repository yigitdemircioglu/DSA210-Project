import pandas as pd
import numpy as np

# Rating dosyasını yükle
df = pd.read_csv("Rating - Uzak Şehir.csv")

# 'Day' kolonunu datetime formatına çevir (tarih sıralamak için)
df['Day'] = pd.to_datetime(df['Day'] + " 2025", format="%d %B %Y")
df = df.sort_values("Day")

# 0 olan All People değerlerini eksik gibi işaretle
df['All People'] = df['All People'].replace(0, np.nan)

# Interpolation (lineer tahmin)
df['All People'] = df['All People'].interpolate(method='linear', limit_direction='both')

# Yeni dosya olarak kaydet
df.to_csv("Rating - Uzak Şehir - Interpolated.csv", index=False)

print("✅ Missing values filled with linear interpolation and saved as 'Rating - Uzak Şehir - Interpolated.csv'")
