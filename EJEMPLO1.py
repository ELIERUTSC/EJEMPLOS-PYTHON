class User:  
    def __init__(self, name=None, email=None):  
self.name = name  
self.email = email  
class Student(User):  
    def __init__(self, name=None, email=None, id=None, score=None):  
        super().__init__(name, email)  
self.id = id if id else uuid.uuid4()  
        self.score = score  
    def send_email(self):  
      
        # Aquí puedes implementar la lógica para enviar un correo electrónico.  
print(f"Correo electrónico enviado a {self.email}")  

# Crear una instancia de Student llamada Student1  
Student1 = Student("sem", "sem.hernandez@utsc.edu.mx")  
Student1.send_email()  

# Crear otra instancia de Student llamada Student2 con un correo electrónico  
Student2 = Student(email="otro.correo@utsc.edu.mx")  
Student2.send_email()  
