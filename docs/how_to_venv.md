# Как создать и подключить `.venv` в VS Code

## Windows (PowerShell)
```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## macOS / Linux (bash/zsh)
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

## Подключение в VS Code
- `Ctrl+Shift+P` → **Python: Select Interpreter** → выберите интерпретатор из `.venv`.
- Убедитесь, что Jupyter использует тот же интерпретатор (вверху ноутбука выберите kernel из `.venv`).

## Советы
- На Windows при ошибке запуска скриптов выполните в PowerShell от имени администратора:  
  `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Для разных проектов используйте отдельные `.venv`.
