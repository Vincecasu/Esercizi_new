class FileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            # Gestione degli errori (facoltativo)
            print(f"An exception occurred: {exc_val}")
        # Returning False re-raises the exception, True suppresses it
        return False  # Cambia a True se vuoi sopprimere l'eccezione

# Esempio di funzionamento
with FileManager('esempio.txt', 'w') as f:
    f.write('Hello, world!')
