# 🎓 ML Student Score Predictor

<p align="center">
  <b>Predict student scores from study hours using Linear Regression — clean, visual, and beginner-friendly.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-LinearRegression-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-Live%20Demo-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge"/>
</p>

<p align="center">
  <a href="https://youtu.be/N26aOZcfPAM">▶️ Watch Demo</a> &nbsp;•&nbsp;
  <a href="https://share.streamlit.io/YOUR-USERNAME/ML-Student-Score-Prediction/main/streamlit-ui.py">🌐 Live App</a> &nbsp;•&nbsp;
  <a href="#-how-to-run-locally">🚀 Quick Start</a>
</p>

---

## 📌 What Is This?

A minimal yet complete **Machine Learning project** that answers one simple question:

> *"If a student studies for X hours, what score can they expect?"*

Built with real data, a trained Linear Regression model, and an interactive Streamlit UI — this project covers the entire ML workflow from raw data to deployed prediction.

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 📊 Data Visualization | Scatter plots & regression line via Matplotlib |
| 🤖 ML Model | Scikit-learn Linear Regression, trained & evaluated |
| 📉 Error Metrics | MAE, MSE, and R² score reporting |
| 🌐 Interactive UI | Streamlit app for live, browser-based predictions |
| 📁 Clean Structure | Modular code, easy to read and extend |

---

## 📊 Demo Visuals

### Regression Fit
<p align="center">
  <img src="assets/score_prediction_graph.png" width="650" alt="Score Prediction Graph"/>
</p>

### Dataset Preview
<p align="center">
  <img src="assets/data_preview.png" width="650" alt="Dataset Preview"/>
</p>

### Terminal Output
<p align="center">
  <img src="assets/terminal_output.png" width="650" alt="Terminal Output"/>
</p>

---

## 🧠 How It Works

```
Study Hours (X)  →  Linear Regression Model  →  Predicted Score (y)
                         y = mx + b
```

1. Load the dataset (hours vs. scores)
2. Split into training and test sets
3. Fit a Linear Regression model
4. Evaluate using MAE, MSE, R²
5. Predict scores for new inputs

---

## 💻 Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| Pandas & NumPy | Data handling |
| Scikit-learn | ML model |
| Matplotlib | Plotting |
| Streamlit | Interactive web app |

---

## 🚀 How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/YOUR-USERNAME/ML-Student-Score-Prediction.git
cd ML-Student-Score-Prediction
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the core script**
```bash
python main.py
```

**4. Launch the Streamlit app**
```bash
streamlit run streamlit-ui.py
```

---

## 📁 Project Structure

```
ML-Student-Score-Prediction/
│
├── assets/                  # Visual outputs (graphs, screenshots)
├── data/
│   └── student_scores.csv   # Dataset
├── main.py                  # Core ML script
├── streamlit-ui.py          # Interactive Streamlit app
├── requirements.txt
└── README.md
```

---

## 📈 Model Performance

| Metric | Value |
|--------|-------|
| R² Score | ~0.95 |
| Mean Absolute Error | ~4.2 |
| Mean Squared Error | ~23.6 |

> *Values may vary slightly depending on train/test split.*

---

## 🎥 Demo Video

<p align="center">
  <a href="https://youtu.be/N26aOZcfPAM">
    <img src="https://img.shields.io/badge/▶%20Watch%20on-YouTube-red?style=for-the-badge&logo=youtube"/>
  </a>
</p>

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open a [pull request](https://github.com/YOUR-USERNAME/ML-Student-Score-Prediction/pulls) or [file an issue](https://github.com/YOUR-USERNAME/ML-Student-Score-Prediction/issues).

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and share.

---

## 👤 Author

**Yash Brahmankar**

<p>
  <a href="https://github.com/YOUR-USERNAME"><img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github"/></a>
  <a href="https://linkedin.com/in/YOUR-PROFILE"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin"/></a>
</p>

---

<p align="center">⭐ If you found this useful, drop a star — it genuinely helps!</p>
