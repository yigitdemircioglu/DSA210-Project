Course: Sabancı University DSA 210 Introduction to Data Science 

Term: Spring 2024-2025 Term Project
# Turkish Series and Social Media Engagement Analysis

## Description ##
This project aims to investigate whether there is a relationship between the weekly TV ratings of selected Turkish series and their social media engagement. For each day of the week, one series will be selected, and its TV ratings as well as social media interaction metrics (such as TikTok view and like counts, Instagram Reels views/likes, X engagement, and Google Trends search volumes) will be collected and analyzed on a weekly basis.

## Motivation ##
Turkish series have a significant impact not only on traditional TV viewership but also on social media platforms. Social media interactions might reflect or even influence the popularity of these series. By exploring the correlation between TV ratings and digital engagement, this project seeks to understand how audience behavior in the digital realm relates to traditional viewership patterns.

## Data Sources ##

### TV Rating Data ###

Source: Official TV rating agencies or published data from television channels

Data: Weekly TV ratings for the selected series

### Social Media Engagement Data ###

Platforms and Metrics:

TikTok: Video view counts and like counts from official TikTok accounts related to the series

Instagram Reels: View and like counts for Reels

X (Twitter): (If available) Engagement metrics such as likes and view counts

Google Trends: Search volume data related to the series

Purpose: To assess how social media interactions correlate with the TV ratings of the series

## Data Integration ##
Both datasets will be collected on a weekly basis and aligned according to time. This ensures that any comparative analysis between TV ratings and social media engagement is based on synchronized time periods, reducing data gaps and ensuring a more reliable comparison.

## Methodology ##
### 1.Data Collection and Cleaning: ###

Gather TV rating and social media engagement data from the respective sources
Clean the data by addressing missing values and aligning time intervals

### 2.Exploratory Data Analysis (EDA): ###

Visualize the daily and weekly distributions of both TV ratings and social media metrics
Identify trends, distributions, and any outliers in each dataset

### 3.Correlation and Regression Analysis: ###

Conduct correlation tests to determine the relationship between TV ratings and social media engagement
If necessary, apply regression models to further assess the predictive effect of social media metrics on TV ratings

### 4.Data Visualization: ###

Present the analysis results with graphs and tables to support the findings
## Tools and Implementation ##
Programming Language: Python
Libraries:
  Data Manipulation: Pandas, NumPy
  
  Visualization: Matplotlib, Seaborn
  
  Statistical Analysis: SciPy, Statsmodels, scikit-learn
  
Version Control: GitHub (including comprehensive documentation, regular commits, a detailed README.md, and a requirements.txt file)

## Expected Outcomes and Future Work ##

### Expected Outcomes: ###

  Determine if there is a significant correlation between TV ratings and social media engagement
  
  Uncover insights into how digital interactions might reflect or influence traditional TV viewership

### Future Work: ###

  Expand the dataset by including more series and additional metrics
  
  Explore alternative modeling techniques and more detailed time series analyses for deeper insights
