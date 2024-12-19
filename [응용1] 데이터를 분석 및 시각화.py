import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

class SalesAnalysis:
    def __init__(self):
        dates=pd.date_range('2024-01-01','2024-12-31',freq='D')
        Sales = np.random.randint(1000,10000,len(dates))
        data = {
            'date':dates,
            'Sale':Sales
        }
        
        self.df = pd.DataFrame(data)

        self.df['month'] = self.df['date'].dt.strftime('%m')
        self.monthly_sales = self.df.groupby('month')['Sale'].sum().reset_index()

    def view(self):
        
        plt.plot(self.monthly_sales['month'], self.monthly_sales['Sale'], marker='o', linestyle='-', color='b')
        
        # 그래프 설정

        plt.title('월별 매출 총합')
        plt.xlabel('월')
        plt.ylabel('매출')
        plt.xticks(ticks=[m for m in range(1,12,2)])

        plt.show()


if __name__ == '__main__':
    Sa=SalesAnalysis()
    Sa.view()