# -*- coding: utf-8 -*-
"""phase-3-experiment-1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1arU6GsB9MaB2X4hxVhobzvVOKWkua7aD

#Assignment 1 (Project Phase 1)

##Group Name: **Data Dreamers**

##**Members**:
- **Md. Fahim Islam -> 2131059642**
- **Amit Chakraborty-> 2132692642**
- **Aditto Rahman   -> 2122332042**
- **Nahid Hassan    -> 2031269642**


- Dataset: Road Traffic Accident Dataset, Rawalpindi-Punjab, Pakistan
- Two possible targets- ***Injury Type*** or ***Patient Status***

# Imports
"""

import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer
from sklearn.impute import SimpleImputer
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.preprocessing import Normalizer

"""## Data Import"""

df = pd.read_csv('/content/RTA Data 2020 to July 2023.csv')

"""#Selecting Our Target Variable

- For this assignment, we have selected **Injury Type** as the target variable.


"""

# Missing values
df.isnull().sum()

"""#Droping Features


"""

df['EcNumber'].value_counts()

"""##EcNumber Correlation check"""

df_sub = df[['EcNumber', 'InjuryType']].copy()
df_sub['EcNumber'] = df_sub['EcNumber'].astype('category').cat.codes
df_sub['InjuryType'] = df_sub['InjuryType'].astype('category').cat.codes
df_sub.dropna(inplace=True)

# Calculate the correlation matrix
correlation = df_sub.corr()

# Plot the heatmap for the correlation matrix
plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation between EcNumber and InjuryType')
plt.tight_layout()
plt.show()

"""The value 0.00095 represents the correlation between EcNumber and InjuryType. A correlation of 0.00095 is extremely close to zero, meaning that there is no significant linear relationship between these two variables. That's why we deleted the EcNumber name region.

##HospitalName Correlation check
"""

df['HospitalName'].value_counts()

df_sub = df[['HospitalName', 'InjuryType']].copy()
df_sub['HospitalName'] = df_sub['HospitalName'].astype('category').cat.codes
df_sub['InjuryType'] = df_sub['InjuryType'].astype('category').cat.codes
df_sub.dropna(inplace=True)

# Calculate the correlation matrix
correlation = df_sub.corr()

# Plot the heatmap for the correlation matrix
plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation between HospitalName and InjuryType')
plt.tight_layout()
plt.show()

"""The correlation between HospitalName and InjuryType is 0.12, which is a very weak positive correlation. This indicates that the two variables have a very minimal linear relationship, meaning the hospital where a patient was treated has little influence on the type of injury in the data.So we will remove this column

##CallTime Correlation check
"""

df['CallTime'].value_counts()

df_sub = df[['CallTime', 'InjuryType']].copy()

df_sub['CallTime'] = df_sub['CallTime'].astype('category').cat.codes
df_sub['InjuryType'] = df_sub['InjuryType'].astype('category').cat.codes
df_sub.dropna(inplace=True)
correlation = df_sub.corr()


# Plot heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation between CallTime and InjuryType')
plt.tight_layout()
plt.show()

"""The off-diagonal value of -0.0042 shows a very weak negative correlation between "CallTime" and "InjuryType." This means that there is almost no linear relationship between these two variables, For that reason we deleted the "CallTime" column.

##EcYear Correlation check
"""

df['EcYear'].value_counts()

df_sub = df[['EcYear', 'InjuryType']].copy()

df_sub['EcYear'] = df_sub['EcYear'].astype('category').cat.codes
df_sub['InjuryType'] = df_sub['InjuryType'].astype('category').cat.codes
df_sub.dropna(inplace=True)
correlation = df_sub.corr()

# Plot heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation between EcYear and InjuryType')
plt.tight_layout()
plt.show()

"""The off-diagonal value of -0.0076 shows a very weak negative correlation between "EcYear" and "InjuryType." This means that there is almost no linear relationship between these two variables, For that reason we deleted the "EcYear" column.

##Info About Dropping

` EcNumber, HospitalName, EcYear, PatientStatus and CallTime were removed as they do not exhibit any significant correlation with the target variable.`
"""

df = df.drop(['EcNumber', 'HospitalName', 'EcYear', 'CallTime'], axis=1)

df['PatientStatus'].value_counts()

df.info()

"""#Filling the Missing Values

"""

#missing values
df.isnull().sum()

"""##Handling Missing Values
`While several columns contain missing values, the number of missing entries is relatively low, with a maximum of 5 missing values in the **responseTime** column. Given the small number of missing values, it is not a significant issue. To address this, we can apply a forward fill technique, which propagates the last valid observation to the next missing one. In this case, we have opted for the forward fill method to handle the missing values efficiently.`
"""

forwardfill = [
    'Reason', 'responsetime', 'EducationTitle', 'InjuryType', 'Cause',
    'BicycleInvovled', 'BikesInvolved', 'BusesInvolved', 'CarsInvolved',
    'CartInvovled', 'RickshawsInvolved', 'TractorInvovled', 'TrainsInvovled',
    'TrucksInvolved', 'VansInvolved', 'OthersInvolved', 'Age','Gender' ,'PatientStatus'
]


df[forwardfill] = df[forwardfill].fillna(method='ffill')


df.isnull().sum()

"""#Duplicate Value"""

df[df.duplicated()]

df.duplicated().sum()

"""##Handle Duplicate value"""

df.drop_duplicates(inplace =True)

df.shape

df.info()

"""#Encoding the categorical columns

##Data Type Conversion
Upon reviewing the data types in the dataframe, we observe that the following columns are of object type:

* EmergencyArea
* Gender
* Reason
* EducationTitle
* InjuryType
* Cause


Since machine learning models require numerical data, these categorical columns must be transformed into numerical format through encoding techniques. We will apply appropriate encoding methods to convert these columns into numerical values, making them suitable for analysis and modeling.

## Ordinal Encoding
"""

df['EducationTitle'].value_counts()

"""###Info EducationTitle Encoding

```
For the columns EducationTitle, we will apply Ordinal Encoding,
because these features have a strong inherent order:

- EducationTitle represents educational level that follows a defined hierarchy (PhD < Master < Primary < Matric).
By using ordinal encoding, we can capture the meaningful order in these features.
```

###EducationTitle Visualization Bar chart
"""

df['EducationTitle'].value_counts().plot(kind='bar', color=['blue', 'red'])


plt.show()

"""###EducationTitle encoding"""

encoder=OrdinalEncoder()
df['EducationTitle'] = encoder.fit_transform(df[['EducationTitle']])
df.info()

df['EducationTitle'].plot(kind='hist', color=['blue'])


plt.show()

"""The histogram shows the distribution of EducationTitle in a dataset. It reveals that most people have education title 5, with fewer people having higher titles and even fewer having lower titles. There are also a few outliers with very high education titles.








\

###EducationTitle Visualization Box plot
"""

#boxplot for column EducationTitle
plt.figure(figsize=(12, 6))
sns.boxplot(x=df['EducationTitle'])

plt.show()

"""The median education title is 5, indicating that 50% of the individuals have an education title less than or equal to 5.

The box plot shows a slight right skew, as the whisker on the right side is longer than the whisker on the left side. This indicates that there are a few individuals with higher education titles, but the majority of individuals have lower education titles.

"""

df['InjuryType'].value_counts()

"""###Info InjuryType Encoding

```
We are using ordinal encoding for "InjuryType" because this method assigns numerical values to categories based on a meaningful order.
 In the case of injury severity, there is a natural hierarchy from minor to more serious conditions. For example:

1. Minor
2. Single Fracture
3. Head Injury
4. Multiple Fractures
5. Spinal Injury

By using ordinal encoding, you can capture this ordinal relationship, where higher numbers represent more severe injuries.
```

###InjuryType Visualization Bar Chart
"""

df['InjuryType'].value_counts().plot(kind='bar', color=['blue', 'red'])


plt.show()

"""###InjuryType Encoding"""

injury_order = [['Minor','Single Fracture', 'Multiple Fractures','Spinal Injury','Head Injury']]

ordinal_encoder = OrdinalEncoder(categories=injury_order)

df['InjuryType'] = ordinal_encoder.fit_transform(df[['InjuryType']])

df['InjuryType'].value_counts()

"""###InjuryType Visualization histogram

"""

injury_type =['Minor','Single Fracture', 'Multiple Fractures','Spinal Injury','Head Injury']
counts =  [34765,6736,3499 ,778  , 381]

# Set up the figure
plt.figure(figsize=(8, 5))

# Create the bar plot
sns.barplot(x=injury_type, y=counts, color="orange")

# Add title and labels
plt.title('InjuryType Histogram', fontsize=14)
plt.xlabel('InjuryType', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Display counts on top of bars
for i, count in enumerate(counts):
    plt.text(i, count + 200, f'{count}', ha='center', fontsize=10)

# Show the plot
plt.tight_layout()
plt.show()

df['PatientStatus'].value_counts()

"""###Info Patient status Encoding

```
For the columns Patient status, we will apply Ordinal Encoding,
because these features have a strong inherent order
```

###InjuryType Visualization Bar Chart
"""

df['PatientStatus'].value_counts().plot(kind='bar', color=['blue', 'red'])


plt.show()

"""###PatientStatus Encoding

"""

encoder = OrdinalEncoder()
df['PatientStatus'] = encoder.fit_transform(df[['PatientStatus']])
df.info()

df['PatientStatus'].value_counts()

"""##Label Encoding"""

df['EmergencyArea'].value_counts()

"""###Info EmergencyArea Encoding

```
The EmergencyArea column contains numerous unique locations, with varying frequencies of incidents at each.
 Label encoding was applied to convert these categorical values into numerical labels for machine learning models.
  While label encoding simplifies the data for models, it doesn't capture the significance of frequent locations.
```

###EmergencyArea Encoding
"""

df['EmergencyArea'].value_counts()

encoder = LabelEncoder()
df['EmergencyArea'] = encoder.fit_transform(df['EmergencyArea'])
df.info()

df['EmergencyArea'].value_counts()

"""###EmergencyArea Visualization Box Plot"""

plt.figure(figsize=(10, 6))
sns.boxplot(x=df['EmergencyArea'])

plt.show()

"""The median value, represented by the line inside the box, is approximately 20,000. This suggests that the middle 50% of the data
 points fall within the range of 10,000 to 25,000.

There are no visible outliers, as there are no data points outside of the whiskers.

###EmergencyArea Visualization Histogram
"""

df['EmergencyArea'].plot(kind='hist', color='red')
plt.title('Distribution of EmergencyArea')
plt.xlabel('EmergencyArea')
plt.ylabel('Frequency')
plt.show()

"""The histogram shows a relatively uniform distribution, with a consistent frequency across most of the "Emergency Area" values. There is no clear peak or skew in the data.

The range of "Emergency Area" values appears to be from approximately 0 to 35,000.

The frequency of each value seems to be around 4,000-5,000, with some minor variations.
"""

df['EmergencyArea']  = (df['EmergencyArea'] - df['EmergencyArea'].mean())/df['EmergencyArea'].max()

"""###Info Cause Encoding




```
Label encoding is used for the Cause column to convert categorical values (e.g., "Over Speed," "Carelessness")
into numeric labels that machine learning models can process.
This is especially helpful for algorithms
like decision trees or random forests, which handle numerical data efficiently.
```


"""

df['Cause'].value_counts()

"""###Cause Visualization Bar chart



"""

df['Cause'].value_counts().plot(kind='bar', color=['blue', 'red'])


plt.show()

"""###Cause Label Encoding"""

encoder = LabelEncoder()
df['Cause'] = encoder.fit_transform(df['Cause'])
df.info()

df['Cause'].value_counts()

"""###Cause Visualization Histogram

"""

df['Cause'].plot(kind='hist', color='red')
plt.title('Distribution of Cause')
plt.xlabel('Cause')
plt.show()

df['Reason'].value_counts()

"""###Fill 'Same' data with forward fill"""

df['Reason'] = df['Reason'].replace(['Same', 'same','Same ','.'], pd.NA)

# Forward fill the NaN values with the value from the previous row
df['Reason'] = df['Reason'].fillna(method='ffill')

df['Reason'].value_counts()

"""###Reason Encoding"""

encoder = LabelEncoder()
df['Reason'] = encoder.fit_transform(df['Reason'])
df.info()

df['Reason'].value_counts()

"""###Reason Visualization Box plot"""

plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Reason'])

plt.show()

"""The median value, represented by the line inside the box, is approximately 15,000. This suggests that the middle 50% of the data points fall within the range of 10,000 to 20,000.

There are no visible outliers, as there are no data points outside of the whiskers.

###Reason Visualization Histogram
"""

df['Reason'].plot(kind='hist', color=[ 'red'])
plt.show()

"""The histogram shows a skewed distribution, with a peak around the values 10,000 to 15,000 and a longer tail extending towards higher values.

The range of values appears to be from approximately 0 to 25,000.

"""

df['Reason']  = (df['Reason'] - df['Reason'].mean())/df['Reason'].max()

"""##One Hot Encoding

###Info Gender Encoding

```
We utilize one-hot encoding for Gender and Injury Type due to the lack of a coherent ordinal relationship
among their values. This technique allows us to represent categorical variables as binary vectors, ensuring that
each category is treated independently.

```
"""

df['Gender'].value_counts()

#print the '0' column whole row from gender
df[df['Gender'] == '0']

"""As the TotalPatientsInEmergency is not in perfect form same goes for Gender we can just delete this row"""

#drop the row where Gender value is '0'
df.drop(df[df['Gender'] == '0'].index, inplace=True)
df['Gender'].value_counts()

"""###Gender Visualization Pie chart

"""

df['Gender'].value_counts().plot(kind='pie', colors=['orange', 'blue','purple'])
plt.show()

"""###Gender Visualization Bar chart

"""

df['Gender'].value_counts().plot(kind='bar', color=['red', 'orange','purple'])
plt.show()

"""###Gender One Hot Encode"""

#convert gender into one-hot encoding
df = pd.get_dummies(df, columns=['Gender'])
df.info()

"""##Convert TotalPatientsInEmergency into numerical"""

df['TotalPatientsInEmergency'].value_counts()

df['TotalPatientsInEmergency'] = df['TotalPatientsInEmergency'].astype(float)
df.info()

"""###TotalPatientEmergency Visualization Histogram

"""

plt.figure(figsize=(10, 6))
plt.hist(df['TotalPatientsInEmergency'], bins=20, color='skyblue', edgecolor='black')

# Title and labels
plt.title('Distribution of Total Patients in Emergency', fontsize=16)
plt.xlabel('Number of Patients', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Optional: Add grid and adjust spines
plt.grid(axis='y', alpha=0.75)
plt.gca().spines[['top', 'right']].set_visible(False)

# Show the plot
plt.tight_layout()
plt.show()

"""The distribution is heavily skewed to the right, with a long tail extending towards higher numbers of patients. This indicates that there are a few instances with a very large number of patients, which significantly impacts the overall distribution.

#Assignment 2(Phase 2)

#For InjuryType

##Split Into Train and Test Sets for InjuryType
"""

X = df.drop(columns=['InjuryType'])
Y = df['InjuryType']

#Perform train-test split (80% train, 20% test)
X_train_InjuryType_p2, X_test_InjuryType_p2, y_train_InjuryType_p2, y_test_InjuryType_p2 = train_test_split(X, Y, test_size=0.2, random_state=42)

"""##Model Train"""

model = LogisticRegression(random_state=42)
model.fit(X_train_InjuryType_p2, y_train_InjuryType_p2)
y_pred_InjuryType_p2 = model.predict(X_test_InjuryType_p2)

"""##Accuracy, Precision, Recall, F1 Score measure

"""

#accuray , precision recall f1 score measure
accuracy_InjuryType_p2 = accuracy_score(y_test_InjuryType_p2, y_pred_InjuryType_p2)
precision_InjuryType_p2 = precision_score(y_test_InjuryType_p2, y_pred_InjuryType_p2, average='weighted', zero_division=0)
recall_InjuryType_p2 = recall_score(y_test_InjuryType_p2, y_pred_InjuryType_p2, average='weighted')
f1_InjuryType_p2 = f1_score(y_test_InjuryType_p2, y_pred_InjuryType_p2, average='weighted')

print(f"Accuracy: {accuracy_InjuryType_p2:.4f}")
print(f"Precision: {precision_InjuryType_p2:.4f}")
print(f"Recall: {recall_InjuryType_p2:.4f}")
print(f"F1 Score: {f1_InjuryType_p2:.4f}")

"""##confusion matrix plot"""

#confusion matrix plot
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
# Compute the confusion matrix
cm = confusion_matrix(y_test_InjuryType_p2, y_pred_InjuryType_p2)
labels = model.classes_

# Plotting the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="YlOrBr", xticklabels=labels, yticklabels=labels)
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("Confusion Matrix for Logistic Regression Model")
plt.show()

"""##Accuracy, Precision, Recall, F1 Score plot"""

metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
scores = [accuracy_InjuryType_p2, precision_InjuryType_p2, recall_InjuryType_p2, f1_InjuryType_p2]

# Plotting the metrics
plt.figure(figsize=(8, 6))
sns.barplot(x=metrics, y=scores, palette="Greens")
plt.ylim(0, 1)
plt.ylabel("Score")
plt.title("Model Performance Metrics")
for i, v in enumerate(scores):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center', fontweight='bold')
plt.show()

"""##Solver and Max_iter"""

solvers = ['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga']
max_iters = [50, 100, 150, 200, 250, 300]

solver_results = []
max_iter_results = []
for solver in solvers:
    model_solver = LogisticRegression(solver=solver)
    model_solver.fit(X_train_InjuryType_p2, y_train_InjuryType_p2)
    y_pred_solver = model_solver.predict(X_test_InjuryType_p2)

    # Calculate metrics
    accuracy_solver = accuracy_score(y_test_InjuryType_p2, y_pred_solver)


    solver_results.append((solver, accuracy_solver))

# Evaluate each max_iter
for max_iter in max_iters:
    model_max_iter = LogisticRegression(max_iter=max_iter)
    model_max_iter.fit(X_train_InjuryType_p2, y_train_InjuryType_p2)
    y_pred_max_iter = model_max_iter.predict(X_test_InjuryType_p2)

    # Calculate metrics
    accuracy_max_iter = accuracy_score(y_test_InjuryType_p2, y_pred_max_iter)


    max_iter_results.append((max_iter, accuracy_max_iter))

solvers = [result[0] for result in solver_results]
solver_accuracies = [result[1] for result in solver_results]

max_iters = [result[0] for result in max_iter_results]
max_iter_accuracies = [result[1] for result in max_iter_results]

# Plot Accuracy vs Solver
plt.figure(figsize=(10, 5))
plt.plot(solvers, solver_accuracies, marker='o', color='b')
plt.xlabel('Solver')
plt.ylabel('Accuracy')
plt.title('Accuracy vs Solver')
plt.grid(True)
plt.show()

# Plot Accuracy vs Max_iter
plt.figure(figsize=(10, 5))
plt.plot(max_iters, max_iter_accuracies, marker='o', color='r')
plt.xlabel('Max Iterations')
plt.ylabel('Accuracy')
plt.title('Accuracy vs Max_iter')
plt.grid(True)
plt.show()

"""#For PatientStatus

##Split Into Train and Test Sets for PatientStatus
"""

X = df.drop(columns=['PatientStatus'])
Y = df['PatientStatus']


X_train_PatientStatus_p2, X_test_PatientStatus_p2, y_train_PatientStatus_p2, y_test_PatientStatus_p2 = train_test_split(X, Y, test_size=0.2, random_state=42)

"""##Model Train"""

model = LogisticRegression(random_state=42)
model.fit(X_train_PatientStatus_p2, y_train_PatientStatus_p2)
y_pred_PatientStatus_p2 = model.predict(X_test_PatientStatus_p2)

"""##Accuracy, Precision, Recall, F1 Score measure

"""

#accuray , precision recall f1 score measure
accuracy_PatientStatus_p2 = accuracy_score(y_test_PatientStatus_p2, y_pred_PatientStatus_p2)
precision_PatientStatus_p2 = precision_score(y_test_PatientStatus_p2, y_pred_PatientStatus_p2, average='weighted', zero_division=0)
recall_PatientStatus_p2 = recall_score(y_test_PatientStatus_p2, y_pred_PatientStatus_p2, average='weighted')
f1_PatientStatus_p2 = f1_score(y_test_PatientStatus_p2, y_pred_PatientStatus_p2, average='weighted')

print(f"Accuracy: {accuracy_PatientStatus_p2:.4f}")
print(f"Precision: {accuracy_PatientStatus_p2:.4f}")
print(f"Recall: {accuracy_PatientStatus_p2:.4f}")
print(f"F1 Score: {accuracy_PatientStatus_p2:.4f}")

"""##confusion matrix plot"""

#confusion matrix plot
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
# Compute the confusion matrix
cm = confusion_matrix(y_test_PatientStatus_p2, y_pred_PatientStatus_p2)
labels = model.classes_

# Plotting the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="YlOrBr", xticklabels=labels, yticklabels=labels)
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("Confusion Matrix for Logistic Regression Model")
plt.show()

"""##Accuracy, Precision, Recall, F1 Score plot"""

metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
scores = [accuracy_PatientStatus_p2, precision_PatientStatus_p2, recall_PatientStatus_p2, f1_PatientStatus_p2]

# Plotting the metrics
plt.figure(figsize=(8, 6))
sns.barplot(x=metrics, y=scores, palette="Greens")
plt.ylim(0, 1)
plt.ylabel("Score")
plt.title("Model Performance Metrics")
for i, v in enumerate(scores):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center', fontweight='bold')
plt.show()

"""##Solver and Max_iter"""

solvers = ['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga']
max_iters = [50, 100, 150, 200, 250, 300]

solver_results = []
max_iter_results = []
for solver in solvers:
    model_solver = LogisticRegression(solver=solver)
    model_solver.fit(X_train_PatientStatus_p2, y_train_PatientStatus_p2)
    y_pred_solver = model_solver.predict(X_test_PatientStatus_p2)

    # Calculate metrics
    accuracy_solver = accuracy_score(y_test_PatientStatus_p2, y_pred_solver)


    solver_results.append((solver, accuracy_solver))

# Evaluate each max_iter
for max_iter in max_iters:
    model_max_iter = LogisticRegression(max_iter=max_iter)
    model_max_iter.fit(X_train_PatientStatus_p2, y_train_PatientStatus_p2)
    y_pred_max_iter = model_max_iter.predict(X_test_PatientStatus_p2)

    # Calculate metrics
    accuracy_max_iter = accuracy_score(y_test_PatientStatus_p2, y_pred_max_iter)


    max_iter_results.append((max_iter, accuracy_max_iter))

solvers = [result[0] for result in solver_results]
solver_accuracies = [result[1] for result in solver_results]

max_iters = [result[0] for result in max_iter_results]
max_iter_accuracies = [result[1] for result in max_iter_results]

# Plot Accuracy vs Solver
plt.figure(figsize=(10, 5))
plt.plot(solvers, solver_accuracies, marker='o', color='b')
plt.xlabel('Solver')
plt.ylabel('Accuracy')
plt.title('Accuracy vs Solver')
plt.grid(True)
plt.show()

# Plot Accuracy vs Max_iter
plt.figure(figsize=(10, 5))
plt.plot(max_iters, max_iter_accuracies, marker='o', color='r')
plt.xlabel('Max Iterations')
plt.ylabel('Accuracy')
plt.title('Accuracy vs Max_iter')
plt.grid(True)
plt.show()

"""# Assignment 3(Phase 3)

# For InjuryType

#Model Train using decision tree

##Split Into Train and Test Sets for InjuryType
"""

X = df.drop(columns=['InjuryType'])
Y = df['InjuryType']

#Perform train-test split (80% train, 20% test)
X_train_InjuryType_p3_dt, X_test_InjuryType_p3_dt, y_train_InjuryType_p3_dt, y_test_InjuryType_p3_dt = train_test_split(X, Y, test_size=0.2, random_state=42)

"""## Model Train"""

from sklearn.tree import DecisionTreeClassifier

# Train the train set on desicion tree model

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train_InjuryType_p3_dt, y_train_InjuryType_p3_dt)
y_pred_InjuryType_p3_dt = model.predict(X_test_InjuryType_p3_dt)

"""##Accuracy, Precision, Recall, F1 Score measure

"""

#accuray , precision recall f1 score measure
accuracy_InjuryType_p3_dt = accuracy_score(y_test_InjuryType_p3_dt, y_pred_InjuryType_p3_dt)
precision_InjuryType_p3_dt = precision_score(y_test_InjuryType_p3_dt, y_pred_InjuryType_p3_dt, average='weighted', zero_division=0)
recall_InjuryType_p3_dt = recall_score(y_test_InjuryType_p3_dt, y_pred_InjuryType_p3_dt, average='weighted')
f1_InjuryType_p3_dt = f1_score(y_test_InjuryType_p3_dt, y_pred_InjuryType_p3_dt, average='weighted')

print(f"Accuracy: {accuracy_InjuryType_p3_dt:.4f}")
print(f"Precision: {precision_InjuryType_p3_dt:.4f}")
print(f"Recall: {recall_InjuryType_p3_dt:.4f}")
print(f"F1 Score: {f1_InjuryType_p3_dt:.4f}")

"""##confusion matrix plot"""

#confusion matrix plot
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
# Compute the confusion matrix
cm = confusion_matrix(y_test_InjuryType_p3_dt, y_pred_InjuryType_p3_dt)
labels = model.classes_

# Plotting the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="YlOrBr", xticklabels=labels, yticklabels=labels)
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("Confusion Matrix for Decision Tree Model")
plt.show()

"""##Accuracy, Precision, Recall, F1 Score plot"""

metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
scores = [accuracy_InjuryType_p3_dt, precision_InjuryType_p3_dt, recall_InjuryType_p3_dt, f1_InjuryType_p3_dt]

# Plotting the metrics
plt.figure(figsize=(8, 6))
sns.barplot(x=metrics, y=scores, palette="Greens")
plt.ylim(0, 1)
plt.ylabel("Score")
plt.title("Decision Tree Model Performance Metrics")
for i, v in enumerate(scores):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center', fontweight='bold')
plt.show()

"""#Model Train using SVM

##Split Into Train and Test Sets for InjuryType
"""

X = df.drop(columns=['InjuryType'])
Y = df['InjuryType']

#Perform train-test split (80% train, 20% test)
X_train_InjuryType_p3_svm, X_test_InjuryType_p3_svm, y_train_InjuryType_p3_svm, y_test_InjuryType_p3_svm = train_test_split(X, Y, test_size=0.2, random_state=42)

"""## Model Train"""

# Model train using svm
from sklearn.svm import SVC

model = SVC(random_state=42)
model.fit(X_train_InjuryType_p3_svm, y_train_InjuryType_p3_svm)
y_pred_InjuryType_p3_svm = model.predict(X_test_InjuryType_p3_svm)

"""##Accuracy, Precision, Recall, F1 Score measure

"""

#accuray , precision recall f1 score measure
accuracy_InjuryType_p3_svm = accuracy_score(y_test_InjuryType_p3_svm, y_pred_InjuryType_p3_svm)
precision_InjuryType_p3_svm = precision_score(y_test_InjuryType_p3_svm, y_pred_InjuryType_p3_svm, average='weighted', zero_division=0)
recall_InjuryType_p3_svm = recall_score(y_test_InjuryType_p3_svm, y_pred_InjuryType_p3_svm, average='weighted')
f1_InjuryType_p3_svm = f1_score(y_test_InjuryType_p3_svm, y_pred_InjuryType_p3_svm, average='weighted')

print(f"Accuracy: {accuracy_InjuryType_p3_svm:.4f}")
print(f"Precision: {precision_InjuryType_p3_svm:.4f}")
print(f"Recall: {recall_InjuryType_p3_svm:.4f}")
print(f"F1 Score: {f1_InjuryType_p3_svm:.4f}")

"""##confusion matrix plot"""

#confusion matrix plot
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
# Compute the confusion matrix
cm = confusion_matrix(y_test_InjuryType_p3_svm, y_pred_InjuryType_p3_svm)
labels = model.classes_

# Plotting the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="YlOrBr", xticklabels=labels, yticklabels=labels)
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("Confusion Matrix for SVM Model")
plt.show()

"""##Accuracy, Precision, Recall, F1 Score plot"""

metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
scores = [accuracy_InjuryType_p3_svm, precision_InjuryType_p3_svm, recall_InjuryType_p3_svm, f1_InjuryType_p3_svm]

# Plotting the metrics
plt.figure(figsize=(8, 6))
sns.barplot(x=metrics, y=scores, palette="Greens")
plt.ylim(0, 1)
plt.ylabel("Score")
plt.title("Model Performance Metrics")
for i, v in enumerate(scores):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center', fontweight='bold')
plt.show()

"""# For PatientStatus

#Model Train using decision tree

##Split Into Train and Test Sets for PatientStatus
"""

X = df.drop(columns=['PatientStatus'])
Y = df['PatientStatus']


X_train_PatientStatus_p3_dt, X_test_PatientStatus_p3_dt, y_train_PatientStatus_p3_dt, y_test_PatientStatus_p3_dt = train_test_split(X, Y, test_size=0.2, random_state=42)

"""## Model train"""

# Model train using decision tree
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train_PatientStatus_p3_dt, y_train_PatientStatus_p3_dt)
y_pred_PatientStatus_p3_dt = model.predict(X_test_PatientStatus_p3_dt)

"""##Accuracy, Precision, Recall, F1 Score measure

"""

#accuray , precision recall f1 score measure
accuracy_PatientStatus_p3_dt = accuracy_score(y_test_PatientStatus_p3_dt, y_pred_PatientStatus_p3_dt)
precision_PatientStatus_p3_dt = precision_score(y_test_PatientStatus_p3_dt, y_pred_PatientStatus_p3_dt, average='weighted', zero_division=0)
recall_PatientStatus_p3_dt = recall_score(y_test_PatientStatus_p3_dt, y_pred_PatientStatus_p3_dt, average='weighted')
f1_PatientStatus_p3_dt = f1_score(y_test_PatientStatus_p3_dt, y_pred_PatientStatus_p3_dt, average='weighted')

print(f"Accuracy: {accuracy_PatientStatus_p3_dt:.4f}")
print(f"Precision: {precision_PatientStatus_p3_dt:.4f}")
print(f"Recall: {recall_PatientStatus_p3_dt:.4f}")
print(f"F1 Score: {f1_PatientStatus_p3_dt:.4f}")

"""##confusion matrix plot"""

#confusion matrix plot
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
# Compute the confusion matrix
cm = confusion_matrix(y_test_PatientStatus_p3_dt, y_pred_PatientStatus_p3_dt)
labels = model.classes_

# Plotting the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="YlOrBr", xticklabels=labels, yticklabels=labels)
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("Confusion Matrix for Decision Tree Model")
plt.show()

"""##Accuracy, Precision, Recall, F1 Score plot"""

metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
scores = [accuracy_PatientStatus_p3_dt, precision_PatientStatus_p3_dt, recall_PatientStatus_p3_dt, f1_PatientStatus_p3_dt]

# Plotting the metrics
plt.figure(figsize=(8, 6))
sns.barplot(x=metrics, y=scores, palette="Greens")
plt.ylim(0, 1)
plt.ylabel("Score")
plt.title("Model Performance Metrics")
for i, v in enumerate(scores):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center', fontweight='bold')
plt.show()

"""#Model Train using SVM

##Split Into Train and Test Sets for PatientStatus
"""

X = df.drop(columns=['PatientStatus'])
Y = df['PatientStatus']


X_train_PatientStatus_p3_svm, X_test_PatientStatus_p3_svm, y_train_PatientStatus_p3_svm, y_test_PatientStatus_p3_svm = train_test_split(X, Y, test_size=0.2, random_state=42)

"""## Model Train"""

# model train using svm
from sklearn.svm import SVC

model = SVC(random_state=42)
model.fit(X_train_PatientStatus_p3_svm, y_train_PatientStatus_p3_svm)
y_pred_PatientStatus_p3_svm = model.predict(X_test_PatientStatus_p3_svm)

"""##Accuracy, Precision, Recall, F1 Score measure
  
"""

#accuray , precision recall f1 score measure
accuracy_PatientStatus_p3_svm = accuracy_score(y_test_PatientStatus_p3_svm, y_pred_PatientStatus_p3_svm)
precision_PatientStatus_p3_svm = precision_score(y_test_PatientStatus_p3_svm, y_pred_PatientStatus_p3_svm, average='weighted', zero_division=0)
recall_PatientStatus_p3_svm = recall_score(y_test_PatientStatus_p3_svm, y_pred_PatientStatus_p3_svm, average='weighted')
f1_PatientStatus_p3_svm = f1_score(y_test_PatientStatus_p3_svm, y_pred_PatientStatus_p3_svm, average='weighted')

print(f"Accuracy: {accuracy_PatientStatus_p3_svm:.4f}")
print(f"Precision: {precision_PatientStatus_p3_svm:.4f}")
print(f"Recall: {recall_PatientStatus_p3_svm:.4f}")
print(f"F1 Score: {f1_PatientStatus_p3_svm:.4f}")

"""##confusion matrix plot"""

#confusion matrix plot
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
# Compute the confusion matrix
cm = confusion_matrix(y_test_PatientStatus_p3_svm, y_pred_PatientStatus_p3_svm)
labels = model.classes_

# Plotting the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="YlOrBr", xticklabels=labels, yticklabels=labels)
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("Confusion Matrix for SVM Model")
plt.show()

"""##Accuracy, Precision, Recall, F1 Score plot"""

metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
scores = [accuracy_PatientStatus_p3_svm, precision_PatientStatus_p3_svm, recall_PatientStatus_p3_svm, f1_PatientStatus_p3_svm]

# Plotting the metrics
plt.figure(figsize=(8, 6))
sns.barplot(x=metrics, y=scores, palette="Greens")
plt.ylim(0, 1)
plt.ylabel("Score")
plt.title("Model Performance Metrics")
for i, v in enumerate(scores):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center', fontweight='bold')
plt.show()

"""# Comparison table for the performance of all models"""

# comparison table for the performance of all models