# Solubility Prediction Using Machine Learning

## Project Overview

This project predicts the solubility of chemical compounds using machine learning techniques. Molecular descriptors such as MolLogP, Molecular Weight, Number of Rotatable Bonds, and Aromatic Proportion are used as input features.

## Workflow

1. Data Collection and Preprocessing
2. Feature Engineering
3. Model Training

   * Linear Regression
   * Random Forest Regressor
4. Model Evaluation
5. Model Serialization using Pickle
6. Flask Web Application Development
7. Real-Time Prediction Interface

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Flask
* HTML
* CSS

## Input Features

* MolLogP
* MolWt
* NumRotatableBonds
* AromaticProportion

## Model Comparison

| Model                   | R² Score | MAE    | RMSE   |
| ----------------------- | -------- | ------ | ------ |
| Linear Regression       | 0.7892   | 0.7798 | 1.0103 |
| Random Forest Regressor | 0.8664   | 0.5784 | 0.8043 |

### Analysis

The Random Forest Regressor outperformed Linear Regression across all evaluation metrics:

* Higher **R² Score (0.8664)** indicates better predictive capability.
* Lower **MAE (0.5784)** indicates smaller average prediction errors.
* Lower **RMSE (0.8043)** indicates fewer large prediction errors.

Based on these results, the Random Forest Regressor was selected as the final model and integrated into the Flask web application for real-time solubility prediction.

## Model Comparison Graph

![Model Comparison](image.png)

## Output

Predicted Solubility Value

## Future Improvements

* Deep Learning Models
* Additional Molecular Descriptors
* Cloud Deployment
* Batch Prediction Support
