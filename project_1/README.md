# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Exploring climate data of Singapore

### Overview

The rise in temperature could have a negative impact on Singapore's tourism industry.

According to a CNA report, a warmer Singapore could spell trouble for its tourism industry.  Experts warn that these changes could make Singapore less appealing to tourists, particularly those seeking cooler climates or outdoor activities. (CNA, 2024)

The study suggests Singapore will experience hotter days, more frequent dry spells, and increased extreme weather events. It could affect the tourists' experience in many open spaces including the Mandai Wildlife Reserve. (CNA, 2024)

Also, the report also mentioned if rainfall increases in Singapore, it could deter some tourists seeking the clear skies and sunshine the city is known for. (CNA, 2024)

Overall, there are potential challenges Singapore's tourism industry might face due to climate change and emphasizes the need for adaptation strategies. Itt is important to find out the correlation between climate data and the visitor numbers, and integrate into the business and operational planning.

Citation: (CNA,2024):
https://www.channelnewsasia.com/singapore/sg-tourists-climate-change-heat-sea-level-rise-warmer-weather-ecotourism-green-4050806?cid=youtube_cna_social_29012018_cna



### Problem Statement

I am working for the Mandai Wildlife Group, which operates the Singapore Zoo, River Wonders, and Night Safari in Singapore. The management is considering using weather forecasts as a factor to predict visitor numbers for operational and business planning. 

The project aims to investigate whether a correlation exists between historical climate data in Singapore and historical visitor numbers. If a strong correlation is found, the management could include weather forecasts to improve the accuracy of predictive models for visitor numbers. 

This would help optimize staff scheduling, maintenance schedules, and resource allocation, leading to cost savings and improved operational efficiency.


---

### Datasets

The datasets used are:

a) rainfall-monthly-number-of-rain-days.csv: Monthly number of rain days from Jan 1982 to Aug 2022. A day is considered to have “rained” if the total rainfall for that day is 0.2mm or more.

b) wet-bulb-temperature-hourly.csv: Hourly wet bulb temperature from Jan 1982 to Nov 2022.

c) data_places.csv: Historical data of number of visitors to Night Safari, River Wonders and Singapore Zoo from Jan 2011 to Nov 2023.

d) rainfall-monthly-total.csv: Total month rainfall from Jan 1982 to Aug 2022.

e) relative-humidity-monthly-mean.csv: Monthly mean of humidity from Jan 1982 to Nov 2022

f) sunshine-duration-monthly-mean-daily-duration.csv: Monthly mean of daily sunshine duration from Jan 1982 to Nov 2022.

g) surface-air-temperature-monthly-mean.csv: Monthly mean of surface air temperature from Jan 1982 to Nov 2022.

---

### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|night_safari|float|data_places|Total number of visitors to Night Safari in thousands| 
|river_wonders|float|data_places|Total number of visitors to River Wonders in thousands| 
|singapore_zoo|float|data_places|Total number of visitors to Singapore Zoo in thousands| 
|wet_bulb_temperature|float|wet-bulb-temperature-hourly|Mean of monthly wet bulb temperature which converted from hourly| 
|no_of_rainy_days|float|rainfall-monthly-number-of-rain-days|Monthly number of rainy days| 
|mean_rh|float|relative-humidity-monthly-mean|Mean relative humidity in %| 
|total_rainfall|float|rainfall-monthly-total|Total rainfall in mm| 
|mean_sunshine_hrs|float|sunshine-duration-monthly-mean-daily-duration|Mean of daily sunshine duration in hour| 
|mean_temp|float|surface-air-temperature-monthly-mean|Monthly mean surface air temperature| 


---

### Brief summary of analysis

Based on my analysis, no correlation found between climate and number of visitors in Night Safari, River Wonders and Singapore Zoo.

I used all kind of explonatory data visualization including heatmap. All the correlation cooefficient are less than 0.3, which considered weak.

---

### Conclusions and recommendations

Conclusion:
1) Weak correlation between climate data and number of visit to Night Safari, River Wonders and Singapore Zoo
2) All correlation coefficient below 0.3 which generally considered as a "weak" threshold.
3) This is a good finding: people tend to think the climate could impact visitor numbers, but the data proves this incorrect.

Recommendation:
1) The management should rely on factors other than climate when forecasting visitor numbers.
2) Given that some visitors come to the zoo regardless of weather conditions, the management should consider enhancing weather-related measures to improve the customer experience, such as adding covered walkways.

---

