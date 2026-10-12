# ТЗ №2 — Класс предобработчика данных

**Задача:** Реализовать класс `Preprocessor` в `src/global_sales/preprocessor.py` для применения фильтров и очистки данных.

## Требования
- Поддержать:
  - Фильтры по значениям/диапазонам (например, Region in [...], Revenue в [min, max]).
  - Удаление дубликатов (опционально).
  - Обработка пропусков: simple (median/mode), drop, none.
  - Опциональное удаление выбросов по IQR для `Revenue`.
- Настройки через `PreprocessConfig`.

## Пример использования
```python
from src.global_sales.preprocessor import load_csv, Preprocessor, PreprocessConfig

df = load_csv("data/raw/large_sales_data.csv")
cfg = PreprocessConfig(filters={"Region": ["East", "South"], "Revenue": {"min": 5, "max": 500}}, outlier_strategy="iqr")
pp = Preprocessor(cfg)
clean = pp.transform(df)
clean.to_csv("data/processed/large_sales_data_clean.csv", index=False)
```

## Критерии готовности
- Тест `tests/test_preprocessor.py` проходит.
- Код отформатирован и документирован (docstring).
