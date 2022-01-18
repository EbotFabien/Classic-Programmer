import json
import itertools
import pandas as pd

df = pd.read_excel('C:/Users/user/Downloads/Telegram Desktop/Cpte%20agent%20db.xlsx')

for (ca,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x,y,z,aa,bb,cc) in zip(df['ID'],df['identité agent'],df['Téléphone'],df['AS AC AP'],
                                                                        df['email groupe'],df['email perso'],df['Code Tva'],
                                                                        df['Taux Tva'],df['SIRET'],df['date entrée'],df['Trigramme'],
                                                                        df['secteur activité'],df['Adresse 1'],df['Adresse 2'],df['CP'],
                                                                        df['Ville'],df['Login backof'],df['PWD backof.1'],df['Login extranet']
                                                                        ,df['Pwd extranet'],df['Login tablette'],df['PWD backof'],df['Observations de suivi']
                                                                        df['Actif  Parti'],df['Type certification'],df['Date certification initiale']
                                                                        ,df['date renouv certification'],df['Pwd Gsuite']):
         cli=Expert.query.filter_by(nom=str(a.lower())).first()

         if cli is None:
            expert=Expert(old=nom=a.lower(),numero=b,TYPE=c,email=d,email_perso=e,code_tva=f,taux_tva=g,siret=h,date_entree=i,
            trigramme=j)    
            db.session.add(expert)
            db.session.commit()
            history=Expert_History(expert_id=expert.id,secteur=k,adresse1=l,adresse2=m,cp=n,ville=o,login_backof=p,pwd_backof=q
            ,login_extranet=r,pwd_extranet=s,login_google=t,pwd_google=u,observations_de_suivi=v,actif_parti=y,type_certification=z;
             date_certification_initiale=aa,date_renouv_certification=bb,pwd_gsuite=cc)
            db.session.add(history)
            db.session.commit()
        else:
            print('already exist')



        


	    
