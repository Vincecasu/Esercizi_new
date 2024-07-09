import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        print(f"time elapsed: {self.elapsed_time:.5f} seconds")
        # Returning False re-raises the exception, True suppresses it
        return False

# Esempio di funzionamento
with Timer():
    time.sleep(1)
