# Global Sales — VS Code Starter

Учебный проект для вебинара: работа аналитика данных в VS Code — от исследования до кода проекта и Git.

## Цели
- Установить и настроить VS Code под задачи DS.
- Создать виртуальную среду `.venv` и подключить её в VS Code.
- Провести EDA в Jupyter Notebook.
- Написать класс предобработчика данных в `src/project_name/preprocessor.py`.
- Научиться делать коммиты и пушить проект на GitHub.

---

## Быстрый старт

### 1) Клонирование/загрузка
Скачайте архив или клонируйте репозиторий (если он уже на GitHub).

### 2) Создание и активация `.venv` (виртуальной среды)

**Windows (PowerShell):**
```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**macOS / Linux (bash/zsh):**
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Или использовать встронный конструктор VS Code от extention Python Environments
- Выбрать Select Intepreter через JN тетрадку
- В следующем выборе нажать на Python Envirioments
- Далее выбрать Create Envirioment. Важно! В системе уже должен быть установлен Python
- Далее выбрать venv
- В выпадающем списке выбьрать Python версию, если у вас их несколько
- Выбрать имя
- Если есть файл requirements.txt, то VS Code предложит Install project dependences 

> В VS Code нажмите `Ctrl+Shift+P` → **Python: Select Interpreter** → выберите интерпретатор из папки `.venv`.

### 3) Подготовка данных
Скачайте датасет **Global Sales Performance Dataset** (Kaggle) и сохраните основной CSV в `data/raw/large_sales_data.csv`.
Если файл называется иначе — скорректируйте путь в ноутбуке/коде.
```python
import kagglehub

# Download latest version
path = kagglehub.dataset_download("shohinurpervezshohan/global-sales-performance-dataset")

print("Path to dataset files:", path)
```


### 4) Запуск проекта в VS Code
- Откройте папку проекта в VS Code (`File → Open Folder…`).
- Установите рекомендуемые расширения (Python, Jupyter, GitLens).
- Запустите ноутбук `notebooks/01_eda_global_sales.ipynb`.
- Откройте `src/project_name/preprocessor.py` и реализуйте TODO.

### 5) Git (локально → GitHub)
```bash
git init
git add .
git commit -m "init: project scaffold for webinar"
# далее в интерфейсе VS Code: Publish to GitHub (или вручную через git remote add origin ...; git push -u origin main)
```

---

## Структура проекта

```
global_sales_vscode_starter/
├─ data/
│  ├─ raw/                  # исходные данные (в .gitignore)
│  └─ processed/            # сохранение обработанных данных
├─ notebooks/
│  └─ 01_eda_global_sales.ipynb
├─ src/
│  └─ project_name/
│     ├─ __init__.py
│     └─ preprocessor.py    # класс предобработки (задание №2)
├─ tests/
│  └─ test_preprocessor.py
├─ docs/
│  ├─ 1_task_research.md      # ТЗ №1 (исследование и инсайты)
│  └─ 2_task_preprocessor.md  # ТЗ №2 (класс предобработчика)
│  └─ how_to_venv.md          # установка виртуальной среды
├─ scripts/
│  └─ example_run_preprocess.py
├─ .vscode/
│  └─ settings.json
├─ .gitignore
├─ requirements.txt
└─ README.md
```

---

## Полезные команды

- Форматирование кода (Black Formatter):
- Прожать Cytl + "," или File -> Preferences -> Settings
- В поиске ввести Notebook, найти в дереве Notebook и в меню справа найти строку Editor: Default Formater
- Выбрать Black Formater
- Ниже выбрать на какие действия форматировать код 

- Запуск тестов (pytest):
```bash
pytest -q
```
