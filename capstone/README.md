# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 4

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

- `Gender Classification Model`: VGGFace (Best accuracy score: 0.93)
- `Race Classification Model`: VGGFace (Best accuracy score: 0.84)
- `Age Classification Model`: VGGFace (Best sensitivity score: 0.63)

---

## Limitations

- `Age model`: The model's performance is limited, with an accuracy of only 0.6. This is primarily due to the inherent difficulty of accurately determining age from facial features alone.  Age perception is subjective, as individuals can appear significantly older or younger than their chronological age, making it a challenging task for the model.

- `Gender and Race model`: While the model performs well in classifying gender and race, there's a potential risk of inaccurate predictions for both categories based on facial features alone. Similar to age estimation, facial appearance can differ significantly from a person's actual gender and race.

---

## Recommendations

Given the limitations outlined above, banks may need to maintain additional customer data to align with the demographic appearance rather than the actual demographic in the customer profile. For instance, if a 30-year-old customer appears to be 20 years old, the system should be capable of recognizing them as having an appearance age of 20 years old after several detections. This approach would address the issue of appearance not matching the customer's actual profile.

---

## Conclusion

The models effectively tackle the problem statement by enhancing ATM security. They assist in identifying suspicious cash withdrawals through face detection, where the individual withdrawing cash does not match the cardholder's profile. This introduces an additional layer of security for ATM customers, instilling greater trust and confidence in the bank's ATM services.

