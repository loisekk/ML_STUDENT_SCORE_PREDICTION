
# main_assets_generator.py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import os

# -------- Create assets folder if not exists --------
if not os.path.exists("assets"):
    os.makedirs("assets")

# -------- Step 1: Prepare the data --------
data = {
    'Hours_studied': [1,2,3,4,5,6,7,8,9,10],
    'score': [12,25,30,45,50,55,60,73,82,90]
}
df = pd.DataFrame(data)
X = df[['Hours_studied']]
y = df['score']

# -------- Step 2: Train Linear Regression --------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# -------- Step 3: Generate score_prediction_graph.png --------
X_1d = X['Hours_studied'].values
y_pred_full = model.predict(X)

plt.figure(figsize=(8,5))
plt.scatter(X_1d, y, label="Actual Score", color="blue")
plt.plot(X_1d, y_pred_full, label="Predicted Line", color="red")
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.title("Hours Studied vs Score Prediction")
plt.legend()
plt.grid(True)
plt.savefig("assets/score_prediction_graph.png", dpi=300, bbox_inches="tight")
plt.close()

# -------- Step 4: Generate data_preview.png --------
fig, ax = plt.subplots(figsize=(6, 2))
ax.axis("tight")
ax.axis("off")
table = ax.table(cellText=df.head().values, colLabels=df.columns, loc="center")
table.scale(1, 1.5)
plt.title("Dataset Preview (First 5 Records)")
plt.savefig("assets/data_preview.png", dpi=300, bbox_inches="tight")
plt.close()

# -------- Step 5: Generate terminal_output.png --------
terminal_text = f"Predictions: {y_pred}\nMean Squared Error: {mse:.2f}"

plt.figure(figsize=(8,3))
plt.text(0.01, 0.5, terminal_text, fontsize=11, family="monospace")
plt.axis("off")
plt.title("Model Output (Terminal)")
plt.savefig("assets/terminal_output.png", dpi=300, bbox_inches="tight")
plt.close()

print("✅ All images generated in assets/ folder!")
