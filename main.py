import datetime
user={}
births=[]
while True:


    def MaxAge() :
        for x in user.values():
            return (x)
    def new():
        now=datetime.datetime.today()
        yearNow= int(now.year)
        mouthNow= int (now.month)
        dayNow=int (now.day)


        def year():
            y=int(input('Please tipe your birth year : '))
            if y>yearNow or y<1800:
                print('Invalid date')
                new()
            else:
                return y
        def mouth():
            m=int(input('Please tipe your birth month : '))
            if m<0 or m>12:
                print('Invalid date')
                new()
            else:
                return m
        def day():
            d=int(input('Please tipe your birth day : '))
            if d<0 or d>31:
                print('Invalid date')
                new()
            else:
                return d

        def age():
            age = yearNow - birth.year - ((mouthNow, dayNow) < (birth.month, birth.day))
            return age



        name = input("tipe your name : ")
        year = year()
        mouth= mouth()
        day= day()
        birth=datetime.date(year,mouth,day)
        births.append(birth)
        age=age()
        user.update({age:name})
    a=input ('-------------------------------------------------------------\n1: if you add a new user \n2: show users   \nType a number :')
    if a=="1":
        new()
    elif a=="2":
        b=0
        for usr in user :
            print (f'{user[usr]} is {usr} years old and she/he was born on {(births[b].strftime("%A") )} ')

            b=1+b
        if (len(user))==1 or (len(user))==0 :
            print ("There is no oldest or youngest person")
        else:
            minAge = (min(user.keys()))
            maxAge = max(user.keys())
            print(f'The oldest one is {user[maxAge]}')
            print(f'The youngest one is {user[minAge]}')
            print (f'Total People: {(len(user))}')


    else:
        print ("invali choit")





