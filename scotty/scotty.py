def firstpart():
    searchType = input('Choose your seacrh condition "name" for name\n,"g" for gender\n ')
    lb = open('BoyNames.txt','r')
    lg = open('GirlNames.txt','r')
    braw=list(lb)
    graw=list(lg)
    Users=[]
    Boys=[]
    Girls=[]
    for boy in braw:
        if( boy==braw[-1]):
            boylast=boy 
            Boys.append(boylast)
            Users.append(boylast)
        else:
            boyl = boy[:-1]
            Boys.append(boyl)
            Users.append(boyl)
    for girl in graw:
        if( girl==graw[-1]):
            girllast=girl
            Girls.append(girllast)
            Users.append(girllast)
        else:
            girll = girl[:-1]
            Girls.append(girll)
            Users.append(girll)

    return Users,Boys,Girls,searchType
def minibot():
    Users,Boys,Girls,searchType=firstpart()
    count=1
    while (count):
         if searchType in('name','g'):
            if searchType=='name':
                name= input('Enter Name : ') 
                if name in Users:
                    print(name)
                else:
                    print("users does not exist")
                 
            elif searchType=='g':
                    print(Boys)
            else:
                    print("users does not exist")
                 
            
                

             
            




minibot()
firstpart()

