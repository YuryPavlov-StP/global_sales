from typing import Optional, List, Dict, Any
import pandas as pd
import numpy as np


class PreprocessConfig:
    region_col: str = "Region"
    category_col: str = "Product_Category"
    quantity_col: str = "Units_Sold"
    revenue_col: str = "Revenue"
    profit_col: str = "Profit"
    filters: Dict[str, Any] = {}  # e.g. {"Region": ["East", "South"]}
    drop_duplicates: bool = True
    handle_missing: str = "simple"  # "simple" | "drop" | "none"
    outlier_strategy: Optional[str] = None  # None | "iqr"

class Preprocessor:
    def __init__(self, config: Optional[PreprocessConfig] = None):
        self.config = config or PreprocessConfig()

    def _apply_filters(self, df: pd.DataFrame) -> pd.DataFrame:
        # TO DO: добавить обработку фильтров по регионам и значения по min/max
        for col, val in self.config.filters.items():
            
            continue
        return df

    def _handle_missing(self, df: pd.DataFrame) -> pd.DataFrame:
        # TO DO: добавить обработку пропусков
        
        return df

    def _deduplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        # TO DO: добавить удаление дубликатов

        return df

    def _remove_outliers_iqr(self, df: pd.DataFrame, cols: Optional[List[str]] = None) -> pd.DataFrame:
        # TO DO: добавить удаление выбросов по IQR в выбранных столбцах

        return df

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        # TO DO: описать последовательность действий
        df = df.copy()
        
        return df


def load_csv(path: str) -> pd.DataFrame:
    """Загрузка CSV с разумными опциями."""
    return pd.read_csv(path, encoding="utf-8", low_memory=False)
