import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('sales_data.csv')
print(data)

# Sales Trend Graph
plt.plot(data['Month'], data['Sales'], marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.savefig('sales_trend.png')
plt.show()

# Profit Graph
plt.bar(data['Month'], data['Profit'])
plt.title('Monthly Profit Analysis')
plt.savefig('profit_trend.png')
plt.show()

print("Best Month:", data.loc[data['Sales'].idxmax(), 'Month'])
