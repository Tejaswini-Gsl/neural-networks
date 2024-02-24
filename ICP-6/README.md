
# ICP 6
video link: https://drive.google.com/drive/u/0/folders/1BH4jtOKo4usih3-rt07A5-m6BnMtze6A

1. pd.read_csv("diabetes.csv", header=None).values - loads a CSV diabetes.csv .
1(a). header=None - CSV file does not contain a header row.
1(b). .values - converts the DataFrame into a NumPy array for processing with Keras.
2. np.random.seed(155) -NumPy's random number generator to 155,
3. Sequential() -	Splits the data into training and testing sets, with a 30% test size
4. my_first_nn.add(Dense(20, input_dim=8, activation='relu')) -	
 input_dim- 8 features of the dataset
 output_dim- 20 neurons 
 activation='relu'-  Rectified Linear Unit (ReLU), an activation function used in neural networks
 activation='sigmoid'- Sigmoid Activation Function is generally used when we have binary classification problem or regression where the output is 0 or 1
 activation= 'tanh'- Hyperbolic tangent as an activation function  [input values between -1 and 1]
5. model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc']) - Compiles
binary cross entropy loss-  as it is suitable for classification tasks. 
Adam optimizer -  commonly used because it adaptively adjusts the learning rate during training. 
accuracy metric will be calculated at each epoch
6. my_first_nn.fit(X_train, Y_train, epochs=100, initial_epoch=0)
epochs- one complete pass through the entire training dataset
initial_epoch- 0 means that we start from the beginning
7.  StandardScaler()- 
8. fit_transform(X_train) - fits the scaler to the training data (X_train) and then transforms it. This means it calculates the mean and standard deviation of each feature in the training set and then standardizes the training data 
9. transform(X_test) -transform the test data (X_test) using the mean and standard deviation calculated from the training data.
10. np.prod() - computes the product of the dimensions of a single image 
ex: (28x28 pixels), resulting in 784
11. to_categorical() - convert the integer labels (0 to 9) into one-hot encoded vectors. One-hot encoding is a representation of categorical variables as binary vectors, where each integer value is represented as 1 or 0 

Why increase the dense layers?
increases the depth of the model, allowing it to potentially learn more complex relationships in the data.
Note: Remember, the impact of adding more layers can vary depending on many factors, including the nature of the dataset, the choice of activation functions, and how well the model is regularized to prevent overfitting.

why use Standard Scale?
we often deal with data that's like comparing mountains to pencils. Some data points might be very big numbers, and others might be very small. If we try to use these numbers as they are to teach a computer to recognize patterns, the big numbers might overshadow the small ones, making it hard for the computer to learn properly.
so StandardScalerhelps us to adjust everything to a common scale without losing the differences in the sizes or values





