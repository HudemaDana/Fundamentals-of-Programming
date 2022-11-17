#problem 6

#check if it is a leap year
def leap(year:int):
    if (int(year % 4) == 0) and (int(year % 100) != 0):
        return True
    elif int(year % 400) == 0:
        return True
    else:
        return False

#declare 2 lists for the mouth/ days in a month
month=["January","February","March","April","May","June","July","August","September","Octomber","November","December"]
days=[31,28,31,30,31,30,31,31,30,31,30,31]

def printr(day:int, sm:int ,mth:int):
    if (day-sm) == 1:
        print(month[mth]," ",day-sm,"st")
    elif (day-sm) == 2:
        print(month[mth]," ",day-sm,"nd")
    elif (day-sm) == 3:
        print(month[mth]," ",day-sm,"rd")
    else:
        print(month[mth]," ",day-sm)



def main():
    #read ayear and bday which represent the year, respective the day

    ayear=int(input())
    bday=int(input())

    s=0
    s=int(s)

    #check if we have a leap year and change the value of february if is necessary
    if leap(ayear):
        days[1]=29

    #we're going through the days of the year and add them to the sum until we find the month in are in
    for i in range(11):
        if (s+days[i])< bday:
            s=s+days[i]
        else:
            break

    printr(bday,s,i)

main()

