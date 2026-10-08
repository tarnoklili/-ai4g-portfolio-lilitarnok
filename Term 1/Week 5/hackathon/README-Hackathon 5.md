# Hackathon 5: Model Showdown

## 1. Project Overview

This project was completed for AI for Good Hackathon 5: Model Showdown.

The goal is to build and compare three machine learning classifiers for a real problem related to work, income, or economic security.

For this project, I chose to predict whether a credit card client will default on their payment next month.

The three models used are:

1. K-Nearest Neighbours (KNN)
2. Logistic Regression
3. Random Forest

The main evaluation metric is recall because missing a customer who is likely to default can be an important risk.

## 2. Problem Statement

Credit default can create financial problems for both customers and financial institutions. A prediction model can help identify customers who may be at risk of default so that a financial institution can consider appropriate support or risk management.

The prediction target is whether a customer's payment will default in the next month.

The positive class is:

`1 = default`

The negative class is:

`0 = no default`

## 3. SDG 8: Decent Work and Economic Growth

This project is connected to SDG 8, Decent Work and Economic Growth.

Financial security and responsible access to credit are connected to economic security. Predicting credit default risk can support better informed financial decisions.

The model should only be used as decision support. It should not automatically decide whether a person receives or is denied financial services.

## 4. User and Decision

The intended user is a financial institution or credit risk analyst.

The prediction can support the user in identifying customers who may have a higher risk of default.

The people affected by the prediction are the customers in the dataset.

A false negative is especially important in this project because it means that a customer who actually defaults is predicted as a non-defaulting customer. Therefore, recall was selected as the main metric.

## 5. Dataset

### Dataset source

The dataset is the UCI Machine Learning Repository dataset:

Default of Credit Card Clients

Source:
https://archive.ics.uci.edu/dataset/350/defaultofcreditcardclients

The dataset is based on credit card clients in Taiwan.

The dataset contains historical information from April to September 2005 and the target indicates whether the client defaulted on their payment in the following month.

The dataset contains:

- 30,000 rows
- 23 usable predictor features
- 1 target column
- No missing values according to the UCI dataset documentation

The dataset is licensed under CC BY 4.0.

Citation:

Yeh, I. C. (2009). Default of Credit Card Clients. UCI Machine Learning Repository. DOI: https://doi.org/10.24432/C55S3H

### Target and class balance

The target column is:

`default payment next month`

Class distribution:

- No default: 23,364
- Default: 6,636

This means that the dataset is imbalanced, with fewer default cases than non-default cases.

### Dataset limitations

The data represents historical credit card clients in Taiwan and comes from a specific time period. It may not represent customers from other countries, populations, or time periods.

The dataset also contains demographic and financial variables. These variables can introduce fairness and bias concerns. The model should therefore not be treated as a fully objective or automatic decision maker.

## 6. Data Preparation

The dataset was loaded directly from the UCI Machine Learning Repository.

The `ID` column was removed because it is an identifier and does not provide useful predictive information.

The target column was separated from the features.

The data was split into training and test sets before preprocessing:

- 80% training data
- 20% test data
- Stratified split
- `random_state=42`

Preprocessing was performed inside a scikit-learn `Pipeline` and `ColumnTransformer`.

Numerical features were scaled using `StandardScaler`.

Categorical features were encoded using `OneHotEncoder`.

This keeps preprocessing inside the training workflow and helps avoid data leakage.

## 7. Baseline

A `DummyClassifier` using the most frequent class was used as the baseline.

The baseline always predicts the majority class.

Its recall for the default class was:

`0.000`

This shows why accuracy alone is not a suitable main metric for this imbalanced classification problem.

## 8. Machine Learning Models

Three classifiers were trained and tuned using scikit-learn:

### KNN

K-Nearest Neighbours was used as one of the required classifiers.

The main hyperparameters tuned were:

- Number of neighbours
- Distance weighting

Best parameters:

- `n_neighbors = 3`
- `weights = distance`

### Logistic Regression

Logistic Regression was used as the second required classifier.

The main hyperparameter tuned was:

- `C`

Best parameter:

- `C = 10`

### Random Forest

Random Forest was selected as the third classifier.

The main hyperparameters tuned were:

- Number of estimators
- Maximum depth
- Minimum samples required to split a node

Best parameters:

- `n_estimators = 100`
- `max_depth = None`
- `min_samples_split = 5`

## 9. Hyperparameter Tuning

All three models were tuned using 5-fold cross-validation on the training data.

Recall was used as the scoring metric for all three models.

The final cross-validation recall results were:

| Model | CV Recall |
|---|---:|
| KNN | 0.355 ± 0.009 |
| Logistic Regression | 0.360 ± 0.012 |
| Random Forest | 0.373 ± 0.009 |

A KNN hyperparameter tuning plot is included in the notebook.

## 10. Final Model Comparison

The baseline is included as the first row.

| Model | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Baseline | 0.779 | 0.000 | 0.000 | 0.000 |
| KNN | 0.772 | 0.479 | 0.361 | 0.412 |
| Logistic Regression | 0.817 | 0.661 | 0.353 | 0.460 |
| Random Forest | 0.816 | 0.653 | 0.362 | 0.466 |

Random Forest achieved the highest recall and F1 score among the three final models.

Logistic Regression achieved slightly higher accuracy and precision.

## 11. Error Analysis

The final Random Forest model was selected for further error analysis.

Its confusion matrix was:

```text
[[4417, 256],
 [ 846, 481]]
```

The model produced 846 false negatives.

A false negative means that a customer who actually defaulted was predicted as a non-defaulting customer.

This is important because false negatives are the main reason recall was selected as the primary metric.

The notebook also compares false negatives with true positives to investigate differences in their characteristics.

## 12. Subgroup Analysis

Recall was also compared between the two available SEX groups in the test set.

The results were:

- SEX 1: recall = 0.358
- SEX 2: recall = 0.366

The results are relatively close, but subgroup performance should still be monitored if a model like this were used in a real setting.

## 13. Ethical Reflection

This model concerns people's financial situations, so incorrect predictions can have real consequences.

The dataset represents a historical population in Taiwan and may not represent other populations or current customers. Demographic variables such as sex, age, education, and marriage status also raise fairness concerns.

The model should therefore not be used as an automatic decision maker for credit access.

The purpose of the model in this project is decision support. A human should review important decisions, and the model's errors and subgroup performance should be monitored.

The choice of recall as the main metric is one way of responding to the cost of false negatives. However, improving recall does not remove the risk of unfair or incorrect decisions.

## 14. Final Recommendation

The recommended model is the Random Forest classifier.

It was selected because recall was the main metric and Random Forest achieved the highest final recall among the three models:

`Random Forest recall = 0.362`

It also achieved the highest F1 score:

`Random Forest F1 = 0.466`

Logistic Regression had slightly better accuracy and precision, but Random Forest performed better on the primary metric.

The difference should still be interpreted carefully because the models' cross-validation results have some variation across folds.

The Random Forest model should therefore be used as a decision-support tool rather than as an automatic decision maker.

## 15. Live Prediction

The notebook ends with a made-up customer example.

The recommended Random Forest model returns both:

- A predicted class
- The probability of default

This demonstrates how the trained model can be used on a new case.

## 16. How to Run

The notebook is designed to run in Google Colab without extra installations.

1. Open the `.ipynb` notebook in Google Colab.
2. Run the notebook from top to bottom.
3. The dataset is downloaded directly from the UCI Machine Learning Repository.
4. The notebook loads and explores the data.
5. The models are trained and tuned.
6. The final models are evaluated.
7. The notebook produces the comparison table, error analysis, and live prediction.

Main Python libraries used:

- Python
- pandas
- NumPy
- scikit-learn
- matplotlib

## 17. Project Files

The main project file is the Hackathon 5 Jupyter notebook.

The notebook contains:

- Dataset loading
- Data exploration
- Data preprocessing
- Baseline model
- Three classifiers
- Hyperparameter tuning
- Cross-validation
- Final evaluation
- Confusion matrices
- Error analysis
- Subgroup analysis
- Live prediction
- Final recommendation

## 18. Sources

UCI Machine Learning Repository:
https://archive.ics.uci.edu/dataset/350/defaultofcreditcardclients

Scikit-learn:
https://scikit-learn.org/stable/

Dataset citation:

Yeh, I. C. (2009). Default of Credit Card Clients. UCI Machine Learning Repository. DOI: https://doi.org/10.24432/C55S3H
