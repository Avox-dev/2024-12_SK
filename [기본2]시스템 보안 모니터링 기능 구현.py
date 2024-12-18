import os
import time
import re

class directoryMonitoring:
    def __init__(self,dirpath):
        self.dirpath=dirpath
        self.o_filelist=os.listdir(path=dirpath)
        self.WarningExlist=['py','js','class']
    

    def getnewfile(self):
        n_filelist=os.listdir(path=self.dirpath)
        newfileset=set(n_filelist)-set(self.o_filelist)
        newfile=''
        if newfileset:
            newfile=newfileset.pop()
            self.o_filelist=n_filelist
        return newfile

        
    def Warningfile(self,newfilename):
        newfileEx=newfilename.split('.').pop()
        for WarningEx in self.WarningExlist:
            if newfileEx == WarningEx:
                return '주의파일'
        return ''
    
    def analyzefile(self, filepath):
        with open(self.dirpath+'\\'+filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        for line_num, line in enumerate(lines, start=1):
            if re.search(r'.*#.*', line): 
                print(f'          주석: 줄 {line_num}: {line.strip()}')

            if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', line):
                print(f'          이메일 주소: 줄 {line_num}: {line.strip()}')

            if any(sql_keyword in line.upper() for sql_keyword in ['SELECT', 'INSERT', 'UPDATE', 'DELETE']):
                print(f'          SQL 코드: 줄 {line_num}: {line.strip()}')
                
def start_monitoring():
    dirpath = input("모니터링할 디렉토리 경로를 입력하세요: ")
    try:
        dm=directoryMonitoring(dirpath)
    except FileNotFoundError:
        print('지정된 경로를 찾을 수 없습니다')
        start_monitoring()
    print(f'{dirpath} 모니터링 시작')
    while True:
        newfilename=dm.getnewfile()

        if newfilename:
            print(f'[+]   {newfilename} {dm.Warningfile(newfilename)}')
            dm.analyzefile(newfilename)
        time.sleep(1)

if __name__ == '__main__':
    start_monitoring()
    
