import pandas as pd
import numpy as np

# 设置随机种子，确保结果可复现
np.random.seed(42)

# 城市列表
cities = ["New York", "Miami", "Shanghai", "Amsterdam", "Paris", "London", "Tokyo", "Berlin", "Singapore", "Sydney"]

# 生成数据集
data = {
    "City": np.random.choice(cities, 200),
    "Year": np.random.randint(2015, 2024, 200),
    "Climate Risk Score": np.random.uniform(1, 10, 200),  # 气候风险评分 1-10
    "Price Change (%)": np.random.uniform(-20, 15, 200),  # 房价变动（%）
    "Green Certified": np.random.choice(["Yes", "No"], 200),  # 是否绿色认证 
    "Capitalization Rate": np.random.uniform(3, 8, 200),  # 资本化率（%）
    "Green Investment (%)": np.random.uniform(5, 40, 200),  # 绿色投资占比（%）
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 保存 CSV 文件
csv_filename = "climate_trade_finance_data.csv"
df.to_csv(csv_filename, index=False)

print(f"✅ CSV 文件已生成：{csv_filename}")
print(df.head())  # 显示前5行数据
print(df.describe())  # 统计摘要
import pandas as pd
import numpy as np

# 设置随机种子，确保结果可复现
np.random.seed(42)

# 城市列表
cities = ["New York", "Miami", "Shanghai", "Amsterdam", "Paris", "London", "Tokyo", "Berlin", "Singapore", "Sydney"]

# 生成数据集
data = {
    "City": np.random.choice(cities, 200),
    "Year": np.random.randint(2015, 2024, 200),
    "Climate Risk Score": np.random.uniform(1, 10, 200),  # 气候风险评分 1-10
    "Price Change (%)": np.random.uniform(-20, 15, 200),  # 房价变动（%）
    "Green Certified": np.random.choice(["Yes", "No"], 200),  # 是否绿色认证 
    "Capitalization Rate": np.random.uniform(3, 8, 200),  # 资本化率（%）
    "Green Investment (%)": np.random.uniform(5, 40, 200),  # 绿色投资占比（%）
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 保存 CSV 文件
csv_filename = "climate_trade_finance_data.csv"
df.to_csv(csv_filename, index=False)

print(f"✅ CSV 文件已生成：{csv_filename}")
print(df.head())  # 显示前5行数据
print(df.describe())  # 统计摘要
import pandas as pd
import numpy as np

# 设置随机种子，保证结果可复现
np.random.seed(42)

# 城市列表
cities = ["New York", "Miami", "Shanghai", "Amsterdam", "Paris", "London", "Tokyo", "Berlin", "Singapore", "Sydney"]

# 生成数据集
data = {
    "City": np.random.choice(cities, 200),
    "Year": np.random.randint(2015, 2024, 200),
    "Climate Risk Score": np.random.uniform(1, 10, 200),  # 1-10 气候风险评分
    "Price Change (%)": np.random.uniform(-20, 15, 200),  # 房价变动（%）
    "Green Certified": np.random.choice(["Yes", "No"], 200),  # 是否绿色认证 
    "Capitalization Rate": np.random.uniform(3, 8, 200),  # 资本化率（%）
    "Green Investment (%)": np.random.uniform(5, 40, 200),  # 绿色投资占比（%）
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 保存 CSV 文件
csv_filename = "climate_trade_finance_data.csv"
df.to_csv(csv_filename, index=False)

print(f"CSV 文件已生成：{csv_filename}")
print(df.head())  # 显示前5行数据
print(df.describe())  # 统计摘要

