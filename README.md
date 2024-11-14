# traffic-accident-analysis-punjab-pakistan

This project explores machine learning approaches to predict outcomes related to road traffic accidents in Rawalpindi, Punjab, Pakistan. Using the "Road Traffic Accident Dataset," we aim to build models for one of two potential targets:
- **Injury Type**: Classification of the injury severity level
- **Patient Status**: Status of the patient post-accident


## Project Phases

The assignment is divided into multiple phases to systematically approach data preprocessing, model selection, training, evaluation, and final analysis.


## Project Phases

### Phase 1
- **Task:** Apply data preprocessing

### Phase 2
1. Apply data preprocessing
2. Train Logistic Regression model on the train set
3. Test the trained model on the test set
4. Evaluate the performance on the test set using the following metrics:
   - **Accuracy**
   - **Confusion Matrix**
   - **Precision**
   - **Recall**
   - **F1 Score**
5. Plot the following learning curves:
   - **Accuracy (y-axis) vs Solver (x-axis)**
   - **Accuracy (y-axis) vs Max_iter (x-axis)**

Models are built for two targets: **Injury Type** and **Patient Status**

**Note:**
- Solver options: `{lbfgs, liblinear, newton_cg, newton-cholesky, sag, saga}`
- Max_iter options: `{50, 100, 150, 200, 250, 300}`

### Phase 3
1. Apply necessary data preprocessing
2. Train the following models on the train set:
   - Decision Tree
   - Support Vector Machine (SVM)
3. Evaluate the performance of the trained models on the test set using the following metrics:
   - **Accuracy**
   - **Precision**
   - **F1 Score**
   - **Recall**
   - **Confusion Matrix**
4. Prepare a comparison table for the performance of all models, including Logistic Regression from Phase 2.
5. Plot the following curves:
   - **Decision Tree:** Accuracy (y-axis) vs Max_depth (x-axis)
   - **SVM:** Accuracy (y-axis) vs Kernel (x-axis)

Models are built for two targets: **Injury Type** and **Patient Status**

**Note:**
- Decision Tree `Max_depth` options: `{4, 5, 6, 7, 8, 9}`
- SVM `Kernel` options: `{linear, poly, rbf, sigmoid}`



