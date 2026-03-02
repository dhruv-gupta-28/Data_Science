class Teacher:
    def __init__(self, subject="Math"):
        self.subject = subject

if __name__ == "__main__":
    t1 = Teacher() # Uses default "Math"
    t2 = Teacher("Science") # Overrides default
    
    print(f"Teacher 1 Subject: {t1.subject}")
    print(f"Teacher 2 Subject: {t2.subject}")
