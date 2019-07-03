import os
import re
def splitFunc(input_data):
    dsplit=input_data.split('.')
    # print(dsplit)
    dyear=int(dsplit[2][0:2])
    dmonth=int(dsplit[2][2:4])
    dversionnum=int(dsplit[3])
    return(dyear,dmonth,dversionnum)
def Scenario00Func(li,dat):
    while(1):
        count=0
        yr=str(dat[0])
        mnth=str(dat[1]-1)
        if len(mnth)==1:
            mnth='0'+mnth
        listring=str(li)
        x=re.search((yr+mnth),listring)
        if x:
            newdata='1.0.'+yr+mnth+'.'
            for i in li:
                # print(i)
                if yr+mnth in str(i):
                    newitem=i
            print('previous data=',str(newitem))
            break
        else:
            dat[1]-=1
def mainFuncForPrevious(str):
    flag=0
    s=os.getcwd()
    if os.path.exists('data.txt'):
        with open('data.txt','r',1) as f:
            li=f.readlines()
            # print(li)
            input_data=input('enter version:')
            for i in li:
                if input_data==str(i).strip():
                    flag=1
                    break
            if flag==0:
                print('item not detected')
                exit()
            else:
                print('item detected')
            try:
                dat=splitFunc(input_data)
                print('yy=',dat[0],',mm=',dat[1],',version no:=',dat[2])
                if int(dat[2]) != 0:
                    yr=str(input_data[0])
                    previousnum=str((dat[2]-1))
                    mnthprev=str(dat[1])
                    if len(str(mnthprev))!=2:
                        mnthprev='0'+str(mnthprev)
                    finalprev = '1.0.' + str(int(dat[0])) + (mnthprev)+ '.' + str(previousnum) 
                    print('previous data=',finalprev)
                elif int(dat[2])==0:
                    if int(dat[1])==1:
                        yr = int(dat[0]) - 1
                        mnth = 12
                        num = 0
                        dat = (yr, mnth, num)
                        print('year at the start is detected')
                    previous=Scenario00Func(li,list(dat))
                    # print(previous)
                #     mnthprev=int(previous[0])
                #     previousnum=previous[1]-1
                # if len(str(mnthprev))!=2:
                #     mnthprev='0'+str(mnthprev)
                
            except ValueError:
                print('u r input is wrong')
            except IndexError:
                print('what u have entered????')


    else:
        with open('data.txt','w',1) as f:
            str='1.0.1901.00\n1.0.1901.01\n1.0.1901.02\n1.0.1901.03\n1.0.1902.00\n1.0.1902.01\n1.0.1904.00\n1.0.2001.00\n1.0.2001.01'
            f.write(str)
if __name__ == '__main__':
    mainFuncForPrevious(str)