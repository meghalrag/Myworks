import os
import re
def splitFunc(data):
    dsplit=data.split('.')
    # print(dsplit)
    dyear=int(dsplit[2][0:2])
    dmonth=int(dsplit[2][2:4])
    dnum=int(dsplit[3])
    return(dyear,dmonth,dnum)
def nextFunc(li,data):
    pass
def Scenario00Func(li,dat):
    while(1):
        count=0
        yr=dat[0]
        mnth=dat[1]-1
        for i in li:
            mydata=splitFunc(i)
            if mydata[0]==yr and mydata[1]==mnth:
                count+=1
        # print(count)
        if count==0:
            dat[1]-=1
            continue
        return (mnth,count)
def mainFuncForPrevious(str):
    flag=0
    mnthprev=0
    previousnum=0
    s=os.getcwd()
    if os.path.exists('data.txt'):
        with open('data.txt','r',1) as f:
            li=f.readlines()
            print(li)
            data=input('enter:')
            for i in li:
                if data==str(i).strip():
                    flag=1
                    break
            if flag==0:
                print('item not detected')
                exit()
            else:
                print('item detected')
            try:
                dat=splitFunc(data)
                print(dat[0],dat[1],dat[2])
                if int(dat[2]) != 0:
                    yr=str(data[0])
                    previousnum=str((dat[2]-1))
                    mnthprev=str(dat[1])
                elif int(dat[2])==0:
                    if int(dat[1])==0:
                        yr = int(dat[0]) - 1
                        mnth = 12
                        num = 0
                        dat = (yr, mnth, num)
                        print('year at the start is detected')
                    previous=Scenario00Func(li,list(dat))
                    # print(previous)
                    mnthprev=int(previous[0])
                    previousnum=previous[1]-1
                if len(str(mnthprev))!=2:
                    mnthprev='0'+str(mnthprev)
                if len(str(previousnum))!=2:
                    previousnum='0'+str(previousnum)
                finalprev = '1.0.' + str(int(dat[0])) + (mnthprev)+ '.' + str(previousnum)
                print('previous data=',finalprev)
            except ValueError:
                print('u r input is wrong')
            except IndexError:
                print('what u have entered????')


    else:
        with open('data.txt','w',1) as f:
            str='1.0.1901.00\n1.0.1901.01\n1.0.1901.02\n1.0.1901.03\n1.0.1902.00\n1.0.1902.01\n1.0.1904.00\n1.0.2001.00\n1.0.2001.01'
            f.write(str)

def mainFuncForNext(str):
    pass
if __name__ == '__main__':
    mainFuncForPrevious(str)
    mainFuncForNext(str)

