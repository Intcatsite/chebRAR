# chebRAR Archiver

A simple graphical tool for packing and unpacking `.crar` archives.

**[English](#english) | [Русский](#русский)**

---

## <a name="english"></a>How to Use (For Users)

1.  Go to the [**Releases Page**](https://github.com/intcatsite/chebrar/releases).
2.  Download `chebrar.exe`.
3.  Run it.

That's it. The program will guide you.

<br>

<details>
<summary><b>For Developers (Click to expand)</b></summary>

### Running from Source
Requires Python 3.
```sh
# 1. Clone the repository
git clone https://github.com/intcatsite/chebrar.git
cd chebrar

# 2. Run the script
python main.py
```

### Building the Executable
Requires PyInstaller (`pip install pyinstaller`).
```sh
# Build a single .exe file without a console window
python -m PyInstaller --onefile --windowed --name=chebrar main.py
```
The final `.exe` will be in the `dist` folder.
</details>

---

## <a name="русский"></a>Как использовать (Для пользователей)

1.  Перейдите на [**страницу релизов (Releases)**](https://github.com/intcatsite/chebrar/releases).
2.  Скачайте файл `chebrar.exe`.
3.  Запустите его.

Это все. Программа сама подскажет, что делать.

<br>

<details>
<summary><b>Для разработчиков (Нажмите, чтобы раскрыть)</b></summary>

### Запуск из исходного кода
Требуется Python 3.
```sh
# 1. Клонируйте репозиторий
git clone https://github.com/intcatsite/chebrar.git
cd chebrar

# 2. Запустите скрипт
python main.py
```

### Сборка исполняемого файла
Требуется PyInstaller (`pip install pyinstaller`).
```sh
# Собрать один .exe файл без окна консоли
python -m PyInstaller --onefile --windowed --name=chebrar main.py
```
Готовый `.exe` файл будет находиться в папке `dist`.
</details>

---

### Contact

**[github.com/intcatsite](https://github.com/intcatsite)**
