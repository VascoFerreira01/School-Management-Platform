class Grade:
    def __init__(self, student, subject, assessment, value: float ):

        if value < 0 or value >20:
            raise ValueError('Grade must be between 0 and 20')
        
        self.student = student
        self.subject = subject
        self.assessment = assessment
        self.value = value
     

    def __str__(self):
        return(f'{self.student.name} \n {self.subject.name}' '-' f'{self.assessment.name} - {self.assessment.assessment_type}: {self.value}')