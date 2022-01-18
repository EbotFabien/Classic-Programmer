from Film import db,Series,Film,Cartoon
import os


#db.create_all()
def Mov(File):
    if File=="cartoons.txt":
        cartoon=open(File,'r')
        Mid_Movie=list(cartoon)
        for film in Mid_Movie:
            if (film==Mid_Movie[-1]):
               first_cart=film.split('_')
               cart=Cartoon.query.filter_by(Cartoon_link=first_cart[1])
               if cart == None:
                 Fin_cart=Cartoon(first_cart[0],first_cart[1],first_cart[2])
                 db.session.add(Fin_cart)
                 db.session.commit()
               else:
                   print('already exists')
            else:
               mov=film[:-1]
               body_cart=mov.split('_')
               cart=Cartoon.query.filter_by(Cartoon_link=body_cart[1])
               if cart == None:
                 Fin=Cartoon(body_cart[0],body_cart[1],body_cart[2])
                 db.session.add(Fin)
                 db.session.commit()
               else:
                   print('already exists')
    elif File=="Films.txt":
        Film=open(File,'r')
        List_Film=list(Film)
        for film in List_Film:
            if(film==List_Film[-1]):
                first_film=film.split('_')
                Fil=Film.query.filter_by(Film_link=first_film[1])
                if Fil == None:
                 Fin_film=Film(first_film[0],first_film[1],first_film[2])
                 db.session.add(Fin_film)
                 db.session.commit()
                else:
                    print('already exists')
            else:
                fil=film[:-1]
                body_fil=fil.split('_')
                rest=Film.query.filter_by(Film_link=first_film[1])
                if rest == None:
                 Fin=Film(body_fil[0],body_fil[1],body_fil[2])
                 db.session.add(Fin)
                 db.session.commit()
                else:
                    print("data already exists")
    elif File=="Series.txt":
        Serie=open(File,'r')
        List_Series=list(Serie)
        for film in List_Series:
            if(film==List_Series[-1]):
                first_series=film.split('_')
                fin_series=Series(first_series[0],first_series[1],first_series[2])
                db.session.add(fin_series)
                db.session.commit()
            else:
                ser=film[:-1]
                body_ser=ser.split('_')
                Fin=Series(body_ser[0],body_ser[1],body_ser[2])
                db.session.add(Fin)
                db.session.commit()
       

    


Mov('cartoons.txt')









