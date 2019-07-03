def curdatfun():
    from datetime import date
    today = date.today()
    print("Today's date:", str(today))
    li=str(today).split('-')#1.0.1907.0
    dyearcur=int(li[0][2:4])
    dmonthcur=int(li[1])
    return(dyearcur,3)

n=input('enter:')
try:
    li=n.split('.')
    yrget=int(li[2][0:2])
    mnthget=int(li[2][2:4])
    num=int(li[3])
    print(yrget,mnthget,num)
    d=curdatfun()
    d=list(d)
    if d[0]==yrget and d[1]==mnthget:
        num+=1
    # print(num)
    else:
        num=0
    d[0]=str(d[0])
    d[1]=str(d[1])
    num=str(num)
    if len(d[1])==1:
        d[1]='0'+d[1]
    print('1.0.'+d[0]+d[1]+'.'+num)
except ValueError:
    print('u r input is wrong')
except IndexError:
    print('what u have entered????')