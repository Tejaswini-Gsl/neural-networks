
# ICP 5

1. pandas.read_csv('glass.csv') -	Reads the CSV file 'glass.csv' into a Pandas DataFrame.
2. df.drop(columns=[df.columns[-1]]) -	Drops the last column from the DataFrame, assuming it is the target variable.
3. train_test_split(X, y, test_size=0.3, random_state=42) -	Splits the data into training and testing sets, with a 30% test size
4. GaussianNB() -	Initializes a Gaussian Naive Bayes model.
5. LinearSVC(max_iter=10000, random_state=42) - Initializes a Linear Support Vector Machine model with a maximum iteration of 10000 and a random state of 42.
6. model.fit(X_train, y_train) - Trains the model on the training data.
7. model.predict(X_test) -	Makes predictions on the test data using the trained model.
8. accuracy_score(y_test, nb_pred) - Calculates the accuracy of the predictions.
9. classification_report(y_test, nb_pred) -	Prints a classification report, which includes precision, recall, F1-score, and support for each class.