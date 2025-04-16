import enum

class Difficulty(enum.Enum):
    Easy = 1
    Medium = 2
    Hard = 3

class Task:
    def __init__(self, Title, Description, Date, Time, Difficulty):
        self.Title = Title
        self.Description = Description
        self.Date = Date
        self.Time = Time
        self.Difficulty = Difficulty
    
    def __str__(self):
        return f"Task(Title={self.Title}, Description={self.Description}, Date={self.Date}, Time={self.Time}, Difficulty={self.Difficulty})"
    

