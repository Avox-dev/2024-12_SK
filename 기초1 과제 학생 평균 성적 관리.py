class StudentScores:
    def __init__(self, file_name):
        self.scores = {}
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    name,score1=line.split(',')
                    self.scores[name]=score1
        except Exception as error:
            print(f'오류:{error}')
 
    def avg(self):
        sum=0
        for val in self.scores.values():
            sum+=int(val)
        return sum/len(self.scores.values())
    def avg_up(self):
        self.avg_up_namelist=[]
        for avg_up_name in self.scores:
            if int(self.scores[avg_up_name])>=self.avg():
                self.avg_up_namelist.append(avg_up_name)
        return self.avg_up_namelist
    def avg_down(self):
        self.avg_down_namelist=''
        for avg_down_name in self.scores:
            if int(self.scores[avg_down_name])<=self.avg():
                #self.avg_down_namelist[avg_down_name]=(self.scores[avg_down_name])
                self.avg_down_namelist+=f'{avg_down_name},{(self.scores[avg_down_name])}'
        with open('below_average_korean.txt','w',encoding='utf8') as file:
            file.write(self.avg_down_namelist)
        return 
    def print_student(self):
        print('----------------------------------------------------------------')
        print(f'평균점수:{self.avg()}')
        print(f'평균 이상을 받은 학생들:{self.avg_up()}')
        print('----------------------------------------------------------------')
 
print('파일명을 입력하세요 ex: scores_korean.txt')
try:
    st1=StudentScores(input())
    st1.print_student()
except:
    print('다시 시도해주세요')
