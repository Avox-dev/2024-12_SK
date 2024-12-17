import re
from collections import Counter
import pandas as pd
class logfileanalyze:
    def __init__(self,path):
        self.logpath=path
        self.ip_pattern = r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

    def ip_extraction(self):
        ips=[]
        try:
            with open(self.logpath,encoding='utf8') as logfile:
                for line in logfile:
                    ip_list=re.findall(self.ip_pattern, line)
                    for ip in ip_list:
                            ips.append(ip)
        except FileNotFoundError:
            print(f"파일 '{self.logpath}'이 없습니다.")
        return ips
    
    def ip_frequency(self,ip_data):
        item_counts = Counter(ip_data)

        return {'ip' :list(item_counts.keys()),'frequency': list(item_counts.values())}
print('파일경로를 입력하세요 ex: C:/Users/user/Desktop/python_project/iplog.log')
logfa=logfileanalyze(input())

ip_data=logfa.ip_extraction()
ip_frqdata=logfa.ip_frequency(ip_data)

df=pd.DataFrame(ip_frqdata)
df_top3=df.nlargest(3, 'frequency')
print(df_top3)
df_top3.to_csv('iplog_top3.csv',index=False,mode='w')
