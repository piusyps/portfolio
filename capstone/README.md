# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Capstone Project

# DSI-SG-42

## Capstone Project: Enhanced ATM Security using Facial Demographic Verification

> Authors: Pius Yee


## Executive Summary

Automated Teller Machines (ATMs) have become an essential part of our daily lives, providing convenient access to cash. However, their reliance on physical cards and PINs makes them vulnerable to theft. Techniques like ATM skimming, where fraudsters steal card information and PINs, pose a significant threat to both financial institutions and consumers. These stolen credentials can be used to withdraw money illegally, leaving victims with financial losses and a sense of insecurity.

This project aims to address these security concerns by proposing a novel approach that leverages existing ATM camera infrastructure. By implementing a system that analyzes video footage and predicts a user's age, gender, and race, we can introduce an additional layer of security. This information, when compared with the cardholder's details on file, can potentially identify suspicious activity and trigger alerts to the cardholder or bank in real-time.

---

The project aims to enhance the ATM security by:-

- Analyze video footage captured by ATM cameras.
- Predict the age, gender, and race of the ATM user with a high degree of accuracy.
- Compare this predicted information with the cardholder's details on file.
- Identify discrepancies between predicted user characteristics and cardholder information that might suggest suspicious activity.
- Trigger real-time alerts to the cardholder or bank in case of potential fraud.

In order to do this, I will construct three models to detect demographics from faces:

1) `Gender Classification Model`: Determines whether the individual is male or female.

2) `Race Classification Model`: Identifies the ethnicity, such as white, Asian, black, etc.

3) `Age Classification Model`: Estimates the age of the individual.

*Using these models, we can ascertain demographic information from faces. Subsequently, we will integrate the three models into a face recognition system:*

4) `Face detection Model`: Recognizes faces from video footage and utilizes the aforementioned three models to determine demographic characteristics.

---

## Problem Statement

How can we utilize facial recognition technology to provide additional security for bank customers?

---

## Data Dictionary

### UTKFace dataset

| Column Name | Description |
|---|---|
| filename | Image filename in the UTKface dataset |
| Age | The age of the individual. |
| Gender | The gender of the individual, 'Male' or 'Female'. |
| Race | The ethnicity of the individual, which are "White", "Black", "Asian", "Indian" and "others" |

---

## Modeling

Models used for tuning and selection

- `Gender Classification Model`: VGGFace Pre-trained model (Best accuracy score: 0.93)
- `Race Classification Model`: VGGFace Pre-trained model (Best accuracy score: 0.84)
- `Age Classification Model`: VGGFace Pre-trained model (Best sensitivity score: 0.63)

---

## Limitations

- `Age model`: 
    - The model has limited accuracy (0.6) when trying to determine age from facial features. 
    - This is because judging age from appearance alone is difficult and subjective, as people can look much younger or older than their actual age.
    
- `Gender and Race model`: 
    - Despite good performance in gender and race prediction, the model might be inaccurate due to limitations of facial features. 
    - Just like age, appearance can vary significantly from a person's actual gender and race.

 - `Face Detection model`:
    - The model cannot detect faces with face masks on.

---

## Recommendations

- Appearance age
    - Due to the difference between appearance and actual demographics, banks might need to store additional data about a customer's perceived appearance.
    - In cases like a 30-year-old customer consistently appearing like a 20-year-old, the system should adapt to recognize their "appearance age".
    - This solves the problem of profiles mismatching a customer's visual presentation.

- Banks may consider mandatory mask removal for cash withdrawals at ATMs.

- Consider finding additional datasets to balance the training data for age and race.

---

## Conclusion

- The models effectively tackle the problem statement by enhancing ATM security.
- The models improve ATM security by using face detection to flag suspicious withdrawals where the person doesn't match the cardholder. This builds customer trust in the bank's ATMs.

## Directories/files
### codes
- `1.0_data_preprocessing_eda.ipynb`: Data pre-processing and EDA
- `2.0_Modelling_gender.ipynb`: Modelling for Gender
- `2.1_Modelling_race.ipynb`: Modelling for Race
- `2.2_ Modelling_age.ipynb`: Modelling for Age
- `3.0_Face_detection_with_prediction.ipynb`: Modelling for face detection
- `app.py`: Using Face Detection with webcam
- `requirements.txt`: listing the external Python libraries to run the project

### datasets
- `utkface`: The image dataset to train the models
- `df_main.csv`: Dataframe consists of the info about UTKface dataset (i.e. gender, race, age etc)
- `image and video files`: the input test data for face detection. The output files are saved in directory _"output_files"_

### models
- `model_age.keras`: trained keras file for age 
- `model_gender.keras`: trained keras file for gender
- `model_race.keras`: trained keras file for race

### output_files
- output files saved from the face detection model

### presentation
- `capstone_slides.pptx`: presentation slide (ppt format)
- `capstone_slides.pdf`: presentation slide (pdf format)