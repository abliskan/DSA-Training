if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    def calculate(student_marks):
        for y,z in student_marks.items():
            if y == query_name:
                avg = sum(z)/len(z)
                # we can get mark upto 2 digit of decimels
                print(f"{avg:.2f}")                
    calculate(student_marks)