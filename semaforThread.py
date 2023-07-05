from PySide6.QtCore import QThread, QTimer, QMutex

class SemaforThread(QThread):
    def __init__(self, mutex):
        super().__init__()
        self.mutex = mutex
        self.timer = QTimer()
        self.timer.timeout.connect(self.run)

    def run(self):
        self.mutex.lock()  # Zaključaj mutex

        # Ovdje se može implementirati logika semafora

        self.mutex.unlock()  # Otključaj mutex
