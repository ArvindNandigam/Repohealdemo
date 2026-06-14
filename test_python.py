import pandas as pd
import requests
import numpy as np


class DataProcessor:

    def __init__(self):
        self.data = []

    def load_data(self):
        df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})
        new_row = pd.DataFrame([{'name': 'Charlie', 'age': 35}])
        df = pd.concat(df, new_row, ignore_index=True)
        self.process_data(df)

    def process_data(self, df):
        self.calculate_statistics(df)

    def calculate_statistics(self, df):
        print(df.describe())
        values = np.array([1, 2, 3, 4, 5])
        print(values[0].item())
        self.fetch_remote_data()

    def fetch_remote_data(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        print(response.json())


if __name__ == '__main__':
    processor = DataProcessor()
    processor.load_data()
