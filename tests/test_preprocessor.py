import sys, os
sys.path.append(os.path.abspath("src"))

import pandas as pd
from global_sales.preprocessor import Preprocessor, PreprocessConfig # для Windows
# from src.global_sales.preprocessor import Preprocessor, PreprocessConfig # для Linux

def test_revenue_in():
    df = pd.DataFrame({"Revenue": [10, 20], "Units_sold": [2, 3]})
    pp = Preprocessor(PreprocessConfig())
    out = pp.transform(df)
    assert "Revenue" in out.columns
