import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("global_market_esg_data.csv")

# Data Visualization
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["ESG_Policy_Strength"], y=df["ROI (%)"])
plt.xlabel("ESG Policy Strength")
plt.ylabel("Return on Investment (ROI %)")
plt.title("ESG Policy Strength vs Investment Return")
plt.savefig("esg_vs_roi.png")
plt.close()

# Model Training
X = df[["ESG_Policy_Strength", "ROI (%)", "Debt_to_Equity_Ratio"]]
y = df["Market_Risk_Index"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Save Predictions
results_df = pd.DataFrame({"Actual Market Risk Index": y_test.values, "Predicted Market Risk Index": y_pred})
results_df.to_csv("market_risk_predictions.csv", index=False)

# Save Summary Report
df.describe().to_csv("data_summary_report.csv")

print("✅ Analysis completed. Results saved.")

