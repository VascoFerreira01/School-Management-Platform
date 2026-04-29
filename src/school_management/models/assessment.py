class Assessment:
    def __init__ (self, name: str, assessment_type: str, weight: float):

        if not name:
            raise ValueError("Assessment name can't be empty")
        
        if not assessment_type:
            raise ValueError("Assessment type can't be empty")
        
        if not weight:
            raise ValueError("Assessment wight must be between 0 and 100")
        
        self.name= name
        self.assessment_type = assessment_type
        self.weight = weight

    def __str__(self):
        return f'{self.name}; {self.assessment_type}; {self.weight}'