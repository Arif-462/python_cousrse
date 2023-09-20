class Exam:
    def __init__(self, total_marks):
        self.total_marks = total_marks
        self.min_marks = 33
        self.max_marks = 80

    def get_marks(self):
        self.marks

    def marks(self, marks):
        if marks > 33:
            self.get_marks += marks

    def earened_marks(self, marks):
        if marks < self.min_marks:
            return f'apni fail korecen, try next best you marks is below {self.min_marks}'
        elif marks > self.max_marks:
            return f'wounderfull you got star marks your marks is above {self.max_marks}'
        
        else:
            self.marks = self.get_marks
            return f'your marks is {marks}'


rakib = Exam(100)
ans = rakib.earened_marks(45)
print(ans)
ans = rakib.earened_marks(85)
print(ans)
ans = rakib.earened_marks(25)
print(ans)