'''
Progettare un semplice sistema di gestione di studenti e corsi con i seguenti 
requisiti:
 
1. Classe Student:
Attributi:

    student_id: str - identificatore univoco per lo studente.
    courses: list[str] - la lista dei corsi ai quali lo studente è iscritto.

Metodi:

    enroll(course: str) - aggiunge il corso specificato alla lista dei corsi 
    dello studente oppure stampa il messaggio "Lo studente è già iscritto al 
    corso {course}."

    get_courses(): restituisce la lista dei corsi ai quali lo studente è 
    iscritto.

    
Classe School:
Attributi:

    students: dict[str, Student] - un dizionario per memorizzare gli studenti, 
    in cui la chiave è una stringa ID mentre il valore è un oggetto di tipo 
    Studente.

Metodi:

    create_student(student_id: str): crea un nuovo studente con l'ID specificato 
    e una lista di corsi vuota oppure stampa il messaggio 
    "Lo studente con ID {student_id} esiste già."

    enroll_student(student_id: str, course: str): se lo studente esiste viene 
    iscritto al corso specificato, altrimenti  stampa il messaggio 
    "Studente non trovato."

    get_student_courses(student_id: str): se lo studente esiste restituisce 
    la lista dei corsi dello studente con l'ID specificato, altrimenti 
    ritorna il messaggio "Studente non trovato."

    get_stundent_list(): Ritorna una lista di tutte le chiavi all'interno 
    del dizionario students.

    search_by_course(self, course: str): Trova e restituisce tutti gli ID degli 
    studenti iscritti ad un determinato corso. Restituisce una lista di tutte 
    le chiavi all'interno del dizionario students che hanno il corso specificato
    tra i valori oppure il messaggio di errore "Nessuno studente è iscritto al 
    corso {course}." se non ci sono studenti che frequentano il corso 
    specificato.
'''

class Student:
    def __init__(self, student_id: str, courses: list[str]):
        self.student_id = student_id
        self.courses = courses
    
    def enroll(self, course: str):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"Lo studente è già iscritto al corso {course}.")
    
    def get_courses(self):
        return self.courses

class School:
    def __init__(self, students: dict[str, Student]):
        self.students = {}
    
    def create_student(self, student_id: str):
        if student_id not in self.students:
            self.students[student_id] = []
        else:
            print(f"Lo studente con ID {student_id} esiste già.")
    
    def enroll_student(self, student_id: str, course: str):
        if student_id in self.students:
            self.students.update[course]
    

  

        


