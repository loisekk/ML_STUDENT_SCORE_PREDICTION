import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import plotly.graph_objects as go
import plotly.figure_factory as ff
import os

if not os.path.exists("assets"):
    os.makedirs("assets")

# -------- Data --------
data = {
    'Hours_studied': [1,2,3,4,5,6,7,8,9,10],
    'score': [12,25,30,45,50,55,60,73,82,90]
}
df = pd.DataFrame(data)
X = df[['Hours_studied']]
y = df['score']

# -------- Train --------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred_full = model.predict(X)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# -------- Graph 1: Prediction Plot --------
fig1 = go.Figure()

fig1.add_trace(go.Scatter(
    x=df['Hours_studied'], y=y,
    mode='markers',
    marker=dict(size=12, color='#00C2FF', line=dict(color='white', width=1.5)),
    name='Actual Score'
))

fig1.add_trace(go.Scatter(
    x=df['Hours_studied'], y=y_pred_full,
    mode='lines',
    line=dict(color='#FF4B6E', width=3, dash='solid'),
    name='Regression Line'
))

# Confidence band (±1 std)
residuals = y.values - y_pred_full
std = residuals.std()
fig1.add_trace(go.Scatter(
    x=list(df['Hours_studied']) + list(df['Hours_studied'])[::-1],
    y=list(y_pred_full + std) + list(y_pred_full - std)[::-1],
    fill='toself',
    fillcolor='rgba(255,75,110,0.12)',
    line=dict(color='rgba(255,255,255,0)'),
    name='±1 Std Band'
))

fig1.update_layout(
    title=dict(text='Hours Studied vs Score Prediction', font=dict(size=20, color='white'), x=0.5),
    xaxis=dict(title='Hours Studied', color='white', gridcolor='#333', zerolinecolor='#444'),
    yaxis=dict(title='Score', color='white', gridcolor='#333', zerolinecolor='#444'),
    paper_bgcolor='#0F0F1A',
    plot_bgcolor='#0F0F1A',
    legend=dict(font=dict(color='white'), bgcolor='rgba(0,0,0,0)'),
    font=dict(color='white'),
    width=900, height=500
)
fig1.write_image("assets/score_prediction_graph.png", scale=2)
print("✅ score_prediction_graph.png saved")

# -------- Graph 2: Data Preview Table --------
preview = df.head()
fig2 = go.Figure(data=[go.Table(
    header=dict(
        values=[f'<b>{c}</b>' for c in preview.columns],
        fill_color='#1A1A2E',
        font=dict(color='#00C2FF', size=14),
        line_color='#333',
        align='center',
        height=36
    ),
    cells=dict(
        values=[preview[c] for c in preview.columns],
        fill_color=[['#0F0F1A','#161625']*5],
        font=dict(color='white', size=13),
        line_color='#333',
        align='center',
        height=32
    )
)])
fig2.update_layout(
    title=dict(text='Dataset Preview (First 5 Records)', font=dict(size=18, color='white'), x=0.5),
    paper_bgcolor='#0F0F1A',
    margin=dict(l=20, r=20, t=60, b=20),
    width=600, height=280
)
fig2.write_image("assets/data_preview.png", scale=2)
print("✅ data_preview.png saved")

# -------- Graph 3: Terminal Output / Metrics Card --------
metrics = {
    'Metric': ['Predictions (test)', 'Mean Squared Error', 'R² Score', 'Coefficient', 'Intercept'],
    'Value': [
        str(np.round(y_pred, 2)),
        f'{mse:.2f}',
        f'{r2:.4f}',
        f'{model.coef_[0]:.4f}',
        f'{model.intercept_:.4f}'
    ]
}
mdf = pd.DataFrame(metrics)

fig3 = go.Figure(data=[go.Table(
    header=dict(
        values=['<b>Metric</b>', '<b>Value</b>'],
        fill_color='#1A1A2E',
        font=dict(color='#00C2FF', size=14),
        line_color='#333',
        align='left',
        height=36
    ),
    cells=dict(
        values=[mdf['Metric'], mdf['Value']],
        fill_color=[['#0F0F1A','#161625']*5],
        font=dict(color=['#FFD700','#7CFC00'], size=13, family='monospace'),
        line_color='#333',
        align='left',
        height=32
    )
)])
fig3.update_layout(
    title=dict(text='Model Output — Terminal View', font=dict(size=18, color='white'), x=0.5),
    paper_bgcolor='#0F0F1A',
    margin=dict(l=20, r=20, t=60, b=20),
    width=700, height=320
)
fig3.write_image("assets/terminal_output.png", scale=2)
print("✅ terminal_output.png saved")
print("\n✅ All assets generated in assets/ folder!")