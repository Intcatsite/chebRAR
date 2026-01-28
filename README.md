# chebRAR Archiver

A simple, user-friendly graphical tool for creating and extracting ZIP-compatible `.crar` archives. Built with Python and tkinter.

**[English](#english) | [Русский](#русский)**

---

## <a name="english"></a>English

### About The Project

chebRAR has evolved from a simple command-line script into a full-fledged GUI application. The goal is to provide a straightforward, no-fuss tool for basic archiving tasks. While it uses a custom `.crar` extension, all archives created are standard ZIP files, ensuring full compatibility with any modern archiving tool.

### Features

*   **Multi-language Interface**: Choose between English and Russian at startup.
*   **Intuitive UI**: Simple buttons for packing and unpacking folders.
*   **Cross-Platform**: Built with Python and tkinter, it runs on Windows, macOS, and Linux.

### Getting Started

To get a local copy up and running, follow these simple steps.

1.  **Clone the repository**
    ```sh
    git clone https://github.com/intcatsite/chebrar.git
    cd chebrar
    ```
2.  **Run the script**
    You need Python 3.x installed on your system.
    ```sh
    python main.py
    ```
    *(Replace `main.py` with the actual name of your Python file)*

### Creating the Executable (`.exe`)

To package the application into a single executable file for Windows, use PyInstaller.

1.  **Install PyInstaller**
    ```sh
    pip install pyinstaller
    ```
2.  **Run the packaging command**
    ```sh
    # Using python -m is a reliable way to call pyinstaller
    python -m PyInstaller --onefile --windowed --name=chebrar main.py
    ```
    The final `chebrar.exe` will be located in the `dist` folder.

---

## <a name="русский"></a>Русский

### О проекте

chebRAR вырос из простого консольного скрипта в полноценное приложение с графическим интерфейсом. Цель проекта — предоставить понятный инструмент для базовых задач архивации. Несмотря на использование собственного расширения `.crar`, все создаваемые архивы являются стандартными ZIP-файлами, что обеспечивает полную совместимость с любыми современными архиваторами.

### Возможности

*   **Многоязычный интерфейс**: Выбор между русским и английским языком при запуске.
*   **Интуитивный дизайн**: Простые кнопки для упаковки и распаковки папок.
*   **Кросс-платформенность**: Программа написана на Python и tkinter, что позволяет ей работать на Windows, macOS и Linux.

### Начало работы

Чтобы запустить локальную копию, выполните следующие простые шаги.

1.  **Клонируйте репозиторий**
    ```sh
    git clone https://github.com/intcatsite/chebrar.git
    cd chebrar
    ```
2.  **Запустите скрипт**
    На вашем компьютере должен быть установлен Python 3.x.
    ```sh
    python main.py
    ```
    *(Замените `main.py` на фактическое имя вашего Python-файла)*

### Создание исполняемого файла (`.exe`)

Чтобы упаковать приложение в один исполняемый файл для Windows, используйте PyInstaller.

1.  **Установите PyInstaller**
    ```sh
    pip install pyinstaller
    ```
2.  **Выполните команду для упаковки**
    ```sh
    # Использование python -m — надежный способ вызова pyinstaller
    python -m PyInstaller --onefile --windowed --name=chebrar main.py
    ```
    Готовый `chebrar.exe` будет находиться в папке `dist`.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

**[github.com/intcatsite](https://github.com/intcatsite)**
