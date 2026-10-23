
# supervised_ml.py

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Prepare the dataset
# X = Hours studied
# y = Exam scores

X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

y = [30, 40, 45, 55, 65,
     70, 80, 85, 90, 95]

# 2. Create the Linear Regression model
model = LinearRegression()

# 3. Train the model
model.fit(X, y)

# 4. Get input from the user
hours = float(input("Enter hours studied: "))

# 5. Predict the exam score
prediction = model.predict([[hours]])

# 6. Display the prediction
print(f"Predicted exam score: {prediction[0]:.2f}")

# 7. Bonus: Plot the dataset and regression line
plt.scatter(X, y, color="blue", label="Actual exam scores")

plt.plot(
    X,
    model.predict(X),
    color="red",
    label="Regression line"
)

plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Student Exam Score Prediction")
plt.legend()
plt.grid(True)
plt.show()
