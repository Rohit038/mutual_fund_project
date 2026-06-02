import pandas as pd
import os

csv_folder = "data/raw"

for file in os.listdir(csv_folder):
    if file.endswith(".csv"):

        path = os.path.join(csv_folder, file)

        print("\n" + "="*50)
        print(f"File: {file}")

        df = pd.read_csv(path)

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())