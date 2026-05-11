import sys
import os
import subprocess
import re
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit,
                             QSplitter, QVBoxLayout, QWidget, QPushButton,
                             QLabel, QGraphicsView, QGraphicsScene)
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtCore import Qt


def usun_kody_ansi(tekst):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', tekst)


class AutoScalingSvgView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setScene(QGraphicsScene())
        self.svg_item = None

    def load_svg(self, filepath):
        self.scene().clear()
        self.svg_item = QGraphicsSvgItem(filepath)
        self.scene().addItem(self.svg_item)
        self.scene().setSceneRect(self.svg_item.boundingRect())
        self.fitInView(self.svg_item, Qt.KeepAspectRatio)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.svg_item:
            self.fitInView(self.svg_item, Qt.KeepAspectRatio)


class SigmaScriptIDE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SigmaScript IDE")
        self.resize(1200, 800)

        # ==========================================
        # USTAWIENIA STYLU
        # ==========================================
        RODZAJ_CZCIONKI = "Consolas, monospace"

        STYLE = {
            "przycisk": (
                "font-size: 24pt; "
                "padding: 15px; "
                "font-weight: bold; "
                "background-color: #4CAF50; "
                "color: white;"
            ),
            "edytor_kodu": (
                f"font-family: {RODZAJ_CZCIONKI}; "
                "font-size: 20pt; "
                "background-color: #ffffff; "
                "color: #000000;"
            ),
            "konsola_bledow": (
                f"font-family: {RODZAJ_CZCIONKI}; "
                "font-size: 18pt; "
                "color: #D32F2F; "
                "background-color: #ffebee;"
            ),
            "konsola_wyjscia": (
                f"font-family: {RODZAJ_CZCIONKI}; "
                "font-size: 18pt; "
                "color: #e0e0e0; "
                "background-color: #2b2b2b;"
            ),
            "etykieta": (
                "font-size: 22pt; "
                "font-weight: bold; "
                "padding: 4px;"
            ),
            "widok_svg": (
                "background-color: white; "
                "border: 1px solid #ccc;"
            )
        }
        # ==========================================

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        self.run_btn = QPushButton("Uruchom SigmaScript")
        self.run_btn.setStyleSheet(STYLE["przycisk"])
        self.run_btn.clicked.connect(self.uruchom_kod)
        layout.addWidget(self.run_btn)

        self.editor = QTextEdit()
        self.editor.setStyleSheet(STYLE["edytor_kodu"])

        if os.path.exists("temp.ss"):
            with open("temp.ss", "r", encoding="utf-8") as f:
                self.editor.setPlainText(f.read())
        else:
            self.editor.setPlainText("naprzod 400\nobroc 120\npowtorz 6 {\n\tnaprzod 400\n\tobroc 60\n}")

        self.editor.textChanged.connect(self.autozapis)

        self.errors_console = QTextEdit()
        self.errors_console.setReadOnly(True)
        self.errors_console.setStyleSheet(STYLE["konsola_bledow"])

        self.svg_viewer = AutoScalingSvgView()
        self.svg_viewer.setStyleSheet(STYLE["widok_svg"])

        self.output_console = QTextEdit()
        self.output_console.setReadOnly(True)
        self.output_console.setStyleSheet(STYLE["konsola_wyjscia"])

        def utworz_panel(tytul, widzet):
            kontener = QWidget()
            uklad = QVBoxLayout(kontener)
            uklad.setContentsMargins(0, 0, 0, 0)
            etykieta = QLabel(tytul)
            etykieta.setStyleSheet(STYLE["etykieta"])
            uklad.addWidget(etykieta)
            uklad.addWidget(widzet)
            return kontener

        left_splitter = QSplitter(Qt.Vertical)
        left_splitter.addWidget(utworz_panel("Kod SigmaScript:", self.editor))
        left_splitter.addWidget(utworz_panel("Bledy kompilacji:", self.errors_console))
        left_splitter.setSizes([500, 200])

        right_splitter = QSplitter(Qt.Vertical)
        right_splitter.addWidget(utworz_panel("Wygenerowany Obraz SVG:", self.svg_viewer))
        right_splitter.addWidget(utworz_panel("Wyjscie konsoli:", self.output_console))
        right_splitter.setSizes([500, 200])

        main_splitter = QSplitter(Qt.Horizontal)
        main_splitter.addWidget(left_splitter)
        main_splitter.addWidget(right_splitter)
        main_splitter.setSizes([600, 600])

        layout.addWidget(main_splitter)

    def autozapis(self):
        kod = self.editor.toPlainText()
        with open("temp.ss", "w", encoding="utf-8") as f:
            f.write(kod)

    def uruchom_kod(self):
        self.errors_console.clear()
        self.output_console.clear()
        self.svg_viewer.scene().clear()

        kod = self.editor.toPlainText()
        if not kod.strip():
            self.errors_console.append("Edytor jest pusty! Wpisz jakis kod przed uruchomieniem.")
            return

        self.autozapis()

        self.output_console.append("[1/3] Uruchamianie kompilatora SigmaScript...\n")
        QApplication.processEvents()

        process_ss = subprocess.run([sys.executable, "main.py", "temp.ss"], capture_output=True, text=True,
                                    encoding="utf-8")

        czysty_stdout = usun_kody_ansi(process_ss.stdout) if process_ss.stdout else ""
        czysty_stderr = usun_kody_ansi(process_ss.stderr) if process_ss.stderr else ""

        if "[!]" in czysty_stdout or czysty_stderr:
            self.errors_console.append("BLAD SIGMASCRIPT:\n" + czysty_stdout.strip() + "\n" + czysty_stderr.strip())
            self.output_console.append("Przerwano z powodu bledow w kodzie.")
            return
        else:
            self.output_console.append(czysty_stdout.strip() + "\n")

        self.output_console.append("[2/3] Kompilacja kodu C (GCC)...\n")
        QApplication.processEvents()

        exe_name = "wynik.exe" if sys.platform == "win32" else "./wynik"

        process_gcc = subprocess.run(["gcc", "wynik.c", "-o", exe_name.replace("./", ""), "-lm"], capture_output=True,
                                     text=True, encoding="utf-8")

        if process_gcc.returncode != 0:
            self.errors_console.append("BLAD GCC (C):\n" + process_gcc.stderr)
            self.output_console.append("Przerwano z powodu bledow na poziomie GCC.")
            return

        self.output_console.append("[3/3] Uruchamianie skompilowanego programu...\n")
        QApplication.processEvents()

        process_exe = subprocess.run([exe_name], capture_output=True, text=True, encoding="utf-8")

        if process_exe.stderr:
            self.errors_console.append("BLAD WYKONANIA (RUNTIME):\n" + process_exe.stderr)

        if process_exe.stdout:
            self.output_console.append("WYJSCIE PROGRAMU:\n" + process_exe.stdout.strip())

        if os.path.exists("wynik.svg"):
            self.svg_viewer.load_svg("wynik.svg")
            self.output_console.append("\n[+] Pomyslnie wygenerowano obraz na ekranie!")
        else:
            self.errors_console.append("\nPlik wynik.svg nie zostal wygenerowany przez kod C!")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    font = app.font()
    font.setPointSize(12)
    app.setFont(font)

    window = SigmaScriptIDE()
    window.show()
    sys.exit(app.exec_())