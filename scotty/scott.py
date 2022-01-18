def process():
    fb = open('BoyNames.txt')
    fg = open('GirlNames.txt')
    fbl=fb.readlines()
    fgl=fg.readlines()
    user_name=[]
    name=""
    count=0
            
    while 1:
        search_type =input("press \n 'n' to search by name\n 'g' to search by gender \n 'b' to search using both\n 's' Begin with \n")
        if search_type.lower() in ('n','g','b','s'):
            if search_type.lower() == 'n':
                for b in fbl:
                    if(b == fbl[-1]):
                        user_name.append(b.lower())
                    else:
                        user_name.append(b[:-1].lower())
                for g in fgl:
                    if(g == fgl[-1]):
                        user_name.append(g.lower())
                    else:
                        user_name.append(g[:-1].lower())
                name =input('please input name:')
                if name.lower() not in user_name:
                    print("NO Name Match")
                else:
                    print(name)
            elif search_type =='g':
                gender=input("please enter 'm' for male or 'f' for female:")
                if gender in('m'):
                    for b in fbl:
                        if(b == fbl[-1]):
                            user_name.append(b.lower())
                        else:
                            user_name.append(b[:-1].lower())
                    print(user_name)
                elif gender in('f'):
                    for g in fgl:
                        if(g == fgl[-1]):
                            user_name.append(g.lower())
                        else:
                            user_name.append(g[:-1].lower())
                    print(user_name)
                else:
                    print("sorry you typed your gender  wrongly")
            elif search_type == 'b':
                name = input('please input name:')
                gender=input("please enter 'm' for male or 'f' for female:")
                if gender in('m'):
                    for b in fbl:
                        if(b == fbl[-1]):
                            user_name.append(b.lower())
                        else:
                            user_name.append(b[:-1].lower())
                    if name.lower() not in user_name:
                        print('No name match\n')
                    else:
                        print(name)            
                if gender in('f'):
                    for g in fgl:
                        if(g == fgl[-1]):
                            user_name.append(g.lower())
                        else:
                            user_name.append(g[:-1].lower())
                    if name.lower() not in user_name:
                        print('No name match\n')
                    else:
                        print(name)
            elif search_type =='s':
                for b in fbl:
                        if(b == fbl[-1]):
                            user_name.append(b.lower())
                        else:
                            user_name.append(b[:-1].lower())
                for g in fgl:
                        if(g == fgl[-1]):
                            user_name.append(g.lower())
                        else:
                            user_name.append(g[:-1].lower())
                name =input('please input name:')
                for user in user_name:
                    if user.startswith(name.lower()):
                        print(user)
                    else:
                        print('wrong input')


process()
                
                
                    

                    
                          
                        
                            
                        
