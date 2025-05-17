import numpy as np
import pandas as pd

# NumPyで乱数のデータを作成（3行×3列）
data = np.random.rand(3, 3)

# PandasのDataFrameに変換して、列名をつける
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# 表示
print("=== DataFrame ===")
print(df)

# 各列の平均を計算して表示
print("\n=== Mean of each column ===")
print(df.mean())
