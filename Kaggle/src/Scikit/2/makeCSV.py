import pandas as pd
import numpy as np

# データを
data = {"ID":np.arange(200),
        "Weight": np.random.randint(150,250,size=200),
        "Waist": np.random.randint(30,40,size=200),
        "JumpSkill": np.random.randint(1,4,size=200),
    }

# データフレームを作成
df = pd.DataFrame(data)
#DataFrameには辞書型をいれる。キーが列名、値が列のデータ

# CSVファイルに保存
file_path = "./in.csv"
df.to_csv(file_path,index=False)
# file_path = "./in.json"
# df.to_json(file_path, orient='records',indent=4,index=False)

