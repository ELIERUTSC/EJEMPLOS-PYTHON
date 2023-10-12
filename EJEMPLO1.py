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
