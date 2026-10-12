import sys, os
sys.path.append(os.path.abspath("src"))

from global_sales.preprocessor import load_csv, Preprocessor, PreprocessConfig # для Windows
# from src.global_sales.preprocessor import load_csv, Preprocessor, PreprocessConfig # для Linux

if __name__ == "__main__":
    df = load_csv("data/raw/large_sales_data.csv")
    cfg = PreprocessConfig(filters={"Region": ["East"]}, outlier_strategy="iqr")
    pp = Preprocessor(cfg)
    clean = pp.transform(df)
    clean.to_csv("data/processed/large_sales_data_clean.csv", index=False)
    print("Saved -> data/processed/large_sales_data_clean.csv")
