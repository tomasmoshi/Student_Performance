import pandas as pd
import os


def load_dataset():
    # Get root folder of project
    base_dir = os.path.dirname(os.path.dirname(__file__))
    csv_path = os.path.join(base_dir, "data", "Student_Performance.csv")
    return pd.read_csv(csv_path)


def load_cleaned_dataset():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    csv_path = os.path.join(base_dir, "data", "Student_Performance_Cleaned.csv")
    return pd.read_csv(csv_path)
