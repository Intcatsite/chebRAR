import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
import webbrowser

TEXT_DATA = {
    'title': {'en': 'chebRAR Tool', 'ru': 'Утилита chebRAR'},
    'lang_title': {'en': 'Language', 'ru': 'Язык'},
    'pack': {'en': 'Pack folder', 'ru': 'Сжать папку'},
    'unpack': {'en': 'Unpack archive', 'ru': 'Извлечь архив'},
    'exit': {'en': 'Quit', 'ru': 'Выход'},
    'select_pack_dir': {'en': 'Select a folder to pack', 'ru': 'Выберите, какую папку сжать'},
    'save_as': {'en': 'Save archive as...', 'ru': 'Сохранить как...'},
    'select_unpack_file': {'en': 'Select an archive to unpack', 'ru': 'Выберите архив для извлечения'},
    'select_dest_dir': {'en': 'Select destination folder', 'ru': 'Выберите, куда извлечь'},
    'ok_title': {'en': 'Done', 'ru': 'Готово'},
    'fail_title': {'en': 'Failure', 'ru': 'Провал'},
    'pack_ok': {'en': 'Archive is ready:\n{}', 'ru': 'Архив готов:\n{}'},
    'unpack_ok': {'en': 'Files are extracted to:\n{}', 'ru': 'Файлы извлечены в:\n{}'},
    'generic_fail': {'en': 'Something went wrong:\n{}', 'ru': 'Что-то пошло не так:\n{}'}
}

class ChebApp:
    def __init__(self):
        self.lang = 'en'
        self.root = None
        self.github_url = "https://github.com/intcatsite"
        self.launch_lang_picker()

    def open_link(self, event):
        webbrowser.open_new_tab(self.github_url)

    def launch_lang_picker(self):
        picker = tk.Tk()
        picker.title(TEXT_DATA['lang_title']['ru'])
        picker.geometry('280x100')
        picker.resizable(False, False)
        
        def set_lang(lang_code):
            self.lang = lang_code
            picker.destroy()

        label = tk.Label(picker, text='Select Language / Выберите язык')
        label.pack(pady=10)
        
        frame = tk.Frame(picker)
        frame.pack(pady=5)
        
        tk.Button(frame, text='English', command=lambda: set_lang('en')).pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text='Русский', command=lambda: set_lang('ru')).pack(side=tk.LEFT, padx=10)
        
        picker.mainloop()

    def run_main_app(self):
        self.root = tk.Tk()
        self.root.title(TEXT_DATA['title'][self.lang])
        self.root.geometry('380x210')
        self.root.resizable(False, False)
        

        tk.Button(self.root, text=TEXT_DATA['pack'][self.lang], font=('Arial', 11), command=self.pack_action).pack(fill=tk.X, padx=20, pady=(20, 5))
        tk.Button(self.root, text=TEXT_DATA['unpack'][self.lang], font=('Arial', 11), command=self.unpack_action).pack(fill=tk.X, padx=20, pady=5)
        
        tk.Button(self.root, text=TEXT_DATA['exit'][self.lang], command=self.root.quit).pack(side=tk.BOTTOM, pady=5)

        link_label = tk.Label(self.root, text=self.github_url, fg="blue", cursor="hand2")
        link_label.pack(side=tk.BOTTOM)
        link_label.bind("<Button-1>", self.open_link)
        
        self.root.mainloop()

    def pack_action(self):
        try:
            src = filedialog.askdirectory(title=TEXT_DATA['select_pack_dir'][self.lang])
            if not src: return
            
            dest = filedialog.asksaveasfilename(
                title=TEXT_DATA['save_as'][self.lang],
                initialdir=os.path.dirname(src),
                initialfile=os.path.basename(src) + '.crar',
                defaultextension='.crar', filetypes=[('chebRAR', '*.crar')]
            )
            if not dest: return

            base = os.path.splitext(dest)[0]
            zip_file = shutil.make_archive(base_name=base, format='zip', root_dir=src)
            if os.path.exists(dest): os.remove(dest)
            os.rename(zip_file, dest)
            messagebox.showinfo(TEXT_DATA['ok_title'][self.lang], TEXT_DATA['pack_ok'][self.lang].format(dest))
        except Exception as e:
            messagebox.showerror(TEXT_DATA['fail_title'][self.lang], TEXT_DATA['generic_fail'][self.lang].format(e))

    def unpack_action(self):
        try:
            src = filedialog.askopenfilename(
                title=TEXT_DATA['select_unpack_file'][self.lang], filetypes=[('chebRAR', '*.crar')]
            )
            if not src: return
            
            dest = filedialog.askdirectory(title=TEXT_DATA['select_dest_dir'][self.lang])
            if not dest: return
            
            shutil.unpack_archive(src, dest, 'zip')
            messagebox.showinfo(TEXT_DATA['ok_title'][self.lang], TEXT_DATA['unpack_ok'][self.lang].format(dest))
        except Exception as e:
            messagebox.showerror(TEXT_DATA['fail_title'][self.lang], TEXT_DATA['generic_fail'][self.lang].format(e))

if __name__ == '__main__':
    app = ChebApp()
    app.run_main_app()
