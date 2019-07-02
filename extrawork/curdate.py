def curdatfun():
    from datetime import date
    today = date.today()
    print("Today's date:", str(today))
    li=str(today).split('-')
    dyearcur=int(li[0][2:4])
    dmonthcur=int(li[1])
    return(dyear,dmonth)

n=input('enter:')
li=n.split('.')
yrget=int(li[2][0:2])
mnthget=int(li[2][2:4])
num=int(li[3])
print(yrget,mnthget,num)
d=curdatfun()
d=