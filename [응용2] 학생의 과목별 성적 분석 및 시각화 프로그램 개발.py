import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

class StudentScoreAnalysis:
    def __init__(self):
        
        names=[f'학생{name}' for name in range(1,21)]
        mat, sci, eng = [np.random.randint(50, 101, 20) for i in range(3)]

        data = {
            '이름':names,
            '수학':mat,
            '영어':eng,
            '과학':sci
        }
        
        self.df = pd.DataFrame(data)
        self.subjectname=[col for col in self.df.columns if col != '이름']
        #print(self.df)
    def plot_average_scores(self):
        
        subject_avg = self.df[self.subjectname].mean()
        
        plt.bar(self.subjectname,subject_avg,color='orange')
        plt.title('과목별 평균 성적')
        plt.ylabel('평균 점수')
        plt.show()
        
        
    def avg_top5view(self):
        
        self.df['평균'] = self.df[self.subjectname].mean(axis=1)
        top5_avg=self.df.sort_values(by='평균',ascending=False).head(5)

        plt.bar(top5_avg['이름'],top5_avg['평균'],color='green')
        plt.title('상위 5명의 평균 성적')
        plt.ylabel('평균 점수')
        plt.show()

if __name__ == '__main__':
    Ssa=StudentScoreAnalysis()
    Ssa.plot_average_scores()
    Ssa.avg_top5view()
