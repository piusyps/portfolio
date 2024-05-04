# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 4

# DSI-SG-42

## Project 4: Obesity and Stroke Model with CT Brain Scan

> Authors: Pius Yee, Michael King Sutanto, Eugene Matthew Cheong

## Contents

---

- [Background](#background)
- [Problem Statement](#problem-statement)
- [Data Dictionary](#data-dictionary)
- [Modeling](#modeling)
- [Conclusion and Recommendations](#recommendations)

---

## Executive Summary

Obesity and stroke are major health concerns facing society today. The World Health Organization (WHO) estimates that over 650 million adults are living with obesity, and stroke is the second leading cause of death globally. These conditions not only cause significant individual suffering but also place a tremendous burden on healthcare systems.

In view of this, there's a need for a streamlined system using detailed patient information, such as better classification of obesity status, to improve stroke risk assessment during triage, allowing physicians to refer at-risk patients promptly and reduce the likelihood of stroke occurrence.

In this project, we will build 3 models to power different aspects of identifying patients at risk of stroke:

1) `Obesity classification model`: The model first determines obesity classification based on patient information, including factors like weekly physical activity frequency. This classification is then used as one of the features for the stroke predictor model below.

2) `Stroke Detector Model`: The model helps determine the probability of getting stroke based on patient information, together with the *obesity classification* from the earlier model.

3) `CT Scan Image Stroke Detector`: The model helps determine the probability of getting stroke based on CT scan images.

With these models, we are able to identify the risk of stroke promptly.

---

## Problem Statement

The healthcare system faces a challenge in quickly identifying patients at risk of stroke upon arrival at the emergency department (A&E), despite standardized triage protocols. Swiftly discerning stroke risk based on initial health particulars such as obesity is difficult, leading to delays in referrals to specialists for preventive measures.

How might we help A&E identify patients at risk of stroke easier?

---

## Data Dictionary

### Obesity Dataset

- **CSV file :** obesity_level_clean.csv

| Column Name                    | Description                                                                                    |
| ------------------------------ | ---------------------------------------------------------------------------------------------- |
| Gender                         | The gender of the individual                                                                   |
| Age                            | The age of the individual.                                                                     |
| Height                         | The height of the individual                                                                   |
| Weight                         | The weight of the individual                                                                   |
| family_history_with_overweight | A binary indicator (0 or 1) showing whether there is a family history of overweight.           |
| FAVC                           | Frequent consumption of high-caloric food                                                      |
| FCVC                           | Frequency of consumption of vegetables                                                         |
| NCP                            | Number of main meals                                                                           |
| CAEC                           | Consumption of food between meals, with values like 'Sometimes', 'Frequently', etc.            |
| SMOKE                          | A binary indicator (0 or 1) showing whether the individual smokes.                             |
| CH2O                           | Consumption of water daily, in liters.                                                         |
| SCC                            | Caloric beverages consumption (0 or 1) where 1 indicates high consumption.                     |
| FAF                            | Physical activity frequency                                                                    |
| TUE                            | Time using technology devices                                                                  |
| CALC                           | Alcohol consumption, with values like 'Sometimes', 'Frequently', etc.                          |
| MTRANS                         | Mode of transportation, with values like 'Public_Transportation', 'Bike', etc.                 |
| obesity_status                 | Consist of underweight, normal, overweight, obesity_calls_1, obesity_calls_2, obesity_calls_3. |

---

### Stroke Dataset

- **CSV file :** healthcare-dataset-stroke-data.clean.csv

| Column Name       | Description                                             |
| ----------------- | ------------------------------------------------------- |
| gender            | Indicates the gender of the individual                  |
| age               | The age of the individual in years.                     |
| hypertension      | Indicates whether the individual has hypertension       |
| heart_disease     | Indicates whether the individual has any heart diseases |
| ever_married      | Indicates marital status                                |
| Residence_type    | Indicates the type of residence                         |
| avg_glucose_level | Average glucose level in the blood.                     |
| bmi               | Body Mass Index                                         |
| smoking_status    | Represents the smoking status of the individual         |
| stroke            | Indicates whether the individual had a stroke           |
| employment_type   | Indicates the employment type or status                 |
| diabetic_status   | Indicates the diabetic status of the individual         |
| obesity_status    | Indicates the obesity status                            |

---

### Brain CT Scan Dataset

Set of images with CT scans of the brain with stroke and normal.

---

## Modeling

Models used for tuning and selection

- `Obesity classification model`: Catboost (Best sensitivity score: 0.9271)
- `Stroke predector model`: XGBoost (Best sensitivity score: 0.8571)
- `CT scan image predector`: Convolutional Neural network (Best sensitivity score: 0.9077)

---

## Limitations

- **Limited Training Data :**
  Due to limited data, the model might be overly specific to the training data (overfitting) or lack the complexity to capture the data's patterns (underfitting), hindering its ability to generalize well to unseen examples.

- **Black box models :**
  Complex models like neural networks can be highly effective but often lack clear explanations for their decisions. This can make them unsuitable for domains where understanding the reasoning behind a prediction is crucial.

---

## Recommendations

We need to find more training data to improve our models. Here are some ways to address dataset limitations in specific areas:

- **Obesity :** For the obesity dataset, we could enhance data collection by incorporating additional variables such as waist circumference and fat mass. This additional variables has the potential to further improve the accuracy of the model.

- **Stroke :** The current stroke dataset exhibits a minority of stroke-positive examples. Enhancing the dataset by sourcing a larger dataset with a more balanced distribution of positive stroke cases could lead to significant improvements in the model's performance.

- **CT Image scan :** Enhancing the accuracy of our model is feasible by sourcing additional CT image scans for training purposes.

---

## Conclusion

In conclusion, our application, powered by three machine learning models focusing on obesity classification, stroke probability assessment, and Brain CT scan analysis, presents a promising avenue for aiding A&E departments in identifying patients at risk of stroke with greater ease and speed. By leveraging advanced technology, we can streamline the process of risk assessment, ultimately contributing to more timely interventions and improved patient outcomes.

### Files

**Code**
- 1.0 data_cleaning_eda_obesity.ipynb  
- 1.1 data_cleaning_eda_stroke.ipynb
- 2.0 model_obesity.ipynb
- 2.1 model_stroke.ipynb
- 3.0 brain_model.ipynb

**Datasets**
- healthcare-dataset-stroke-data-.clean.csv
- healthcare-dataset-stroke-data.csv
- obesity_level_clean.csv
- obesity_level.csv
- brain_datasets

**images**
- Loss.png
- Recall.png

**models**
- ctscan_model.h5
- ctscan_model.keras
- map_obesity.json
- model_obesity.pkl
- model_stroke.pkl