import json
import itertools
import pandas as pd

df = pd.read_excel('C:/Users/user/Downloads/Telegram Desktop/SUIVI%20CLIENTS%20%26%20PROSPECTS%20%C3%A0%20importer%20en%20Base.xlsx')

print(df['Commentaires  suivi client et action à prévoir'])
for (ca,a,b,c,d,e,f,g,h,i,j,k,l,m,v) in zip(df['Ref proposition commerciale'],df['Etat du client']
                                                                           ,df['Référence de la société'],df['Titre'],
                                                                           df['Nom du ou des responsables'],df['Date création du client']
                                                                           ,df['Adresse 1'],df['Complément adresse'],df['CODE POSTAL'],
                                                                        df['Ville'],df['Extranet ID Login'],df['Extranet MDP'],df['Numéro de siret']
                                                                        ,df['Nom du ou des responsables'],df['Commentaires  suivi client et action à prévoir']):
                if str(a) != 'PROSPECT':d
                    cli=Client.query.filter(and_(Client.reference==ca,Client.societe==b,Client.nom==d)).first() #check by reference number,societe, and nom
                    r_C=Expert.query.filter_by(nom=str(m.lower())).first()
                    if cli is None:
                        client=Client(reference=ca,TYPE=a,societe=b,titre=c,nom=d.lower(),date_creation=e,siret=l)
                        db.session.add(client)
                        db.session.commit()   
                        history=Client_History(client_id=client.id,adresse1=f,adresse2=g,cp=h,ville=i,
                        login_extranet=j,mpd_extranet=k,pays="FRANCE")
                        r_C=Expert.query.filter_by(nom=str(m.lower())).first()
                        if r_C is not None:#check keys
                            rC= r_C.id
                        if r_C is None  :
                            rC= 0
                        if v !='NaN':#check
                            suivi =suivi_client(client=client.id,responsable=rC,commentaire=v)
                            db.session.add(suivi)
                        db.session.add(history)
                        db.session.commit()

                    else:
                        return 'This data already exist'
                    
                        
                if str(a) == 'PROSPECT' :
                    
                    cli=prospect.query.filter(and_(prospect.reference==ca,prospect.societe==b,prospect.nom==d)).first() #check by reference number,societe, and nom
                    if cli is None:
                        client=prospect(reference=ca,TYPE=a,societe=b,titre=c,nom=d.lower(),date_creation=e,siret=l)
                        db.session.add(client)
                        db.session.commit()   
                        history=prospect_History(prospect=client.id,adresse1=f,adresse2=g,cp=h,ville=i)
                        db.session.add(history)
                        db.session.commit()
 
                    else:
                        return 'This data already exist'


for (m,n,o,p,q,r,s,t,u,v,x,y,z,aa,bb,cc,dd,ee,ff,ab,ac,ad,ae,af,ag,ah,ai,aj,ak,al,am,an,ao,ap,aq,ar,As,at,au,av,aw,ax,ay,az,ba,bc,bd,be,ca,km,ck) in zip(df['AS du Client'],df['% Com AS du client'],df['Nom Respon Cell Dev'],
                                                      df['% Respon Cell Dev'],df['Nom agent Cell Dev'],df['% Agent Cell Dev']
                                                      ,df['Nom Agent TECH EDELE'],df['% Agent TECH EDELE'],df['Nom Respon Cell Tech']
                                                      ,df['% Respon Cell Tech'],df['Nom Suiveur Cell Tech'],df['% Suiveur Cell Tech'],
                                                      df['Nom Respon Cell Planif'],df['% Respon Cell Planif'],df['Nom Suiveur Cell Planif'],
                                                      df['% Suiveur Cell Planif'],df['Nom Agent saisie Cell Planif'],df['% Agent saisie CEll planif'],
                                                      df['TAUX DE MAJORATION MEUBLE'],df['EDL_PRIX STD'],df['EDL_APPT / PRIX T1'],df['EDL_APPT / PRIX T2'],
                                                      df['EDL_APPT / PRIX T3'],df['EDL_APPT / PRIX T4'],df['EDL_APPT / PRIX T5'],df['EDL_APPT / PRIX T6'],
                                                      df['EDL_PAV VILLA / PRIX T1'],df['EDL_PAV VILLA / PRIX T2'],df['EDL_PAV VILLA / PRIX T3'],
                                                      df['EDL_PAV VILLA / PRIX T4'],df['EDL_PAV VILLA / PRIX T5'],df['EDL_PAV VILLA / PRIX T6'],
                                                      df['EDL_PAV VILLA / PRIX T7'],df['EDL_PAV VILLA / PRIX T8'],df['CHIF_APPT / PRIX STU'],
                                                      df['CHIF_APPT / PRIX T1'],df['CHIF_APPT / PRIX T2'],df['CHIF_APPT / PRIX T3'],
                                                      df['CHIF_APPT / PRIX T4'],df['CHIF_APPT / PRIX T5'],df['CHIF_PAV VILLA / PRIX T1'],
                                                      df['CHIF_PAV VILLA / PRIX T2'],df['CHIF_PAV VILLA / PRIX T3'],df['CHIF_PAV VILLA / PRIX T4'],
                                                      df['CHIF_PAV VILLA / PRIX T5'],df['CHIF_PAV VILLA / PRIX T6'],df['CHIF_PAV VILLA / PRIX T7'],
                                                      df['CHIF_PAV VILLA / PRIX T8'],df['PRIX AUTRE'],df['Ref proposition commerciale']
                                                      ,df['Référence de la société'],df['Nom du ou des responsables']):
    
                    cli=Client.query.filter(and_(Client.reference=ca,Client.societe=km,Client.nom=ck)).first() #check by reference number,societekm, and nomck
                    tarif =Tarifs.query.filter_by(reference_client=int(cli.id)).first()
                    r_C=Expert.query.filter_by(nom=str(m.lower())).first()
                    if r_C is not None:#check keys
                        rC= r_C.id
                    if r_C is None  :
                        rC= 0
                    r_r=Expert.query.filter_by(nom=str(o.lower())).first()
                    if r_r is not None:
                        rr= r_r.id
                    if r_r is None  :
                        rr= 0
                    dr_a=Expert.query.filter_by(nom=str(q.lower())).first()
                    if dr_a is not None:
                        dra= dr_a.id
                    if dr_a is None  :
                        dra= 0
                    tr_a=Expert.query.filter_by(nom=str(s.lower())).first()
                    if tr_a is not None:
                        tra= tr_a.id
                    if tr_a is None  :
                        tra= 0
                    tr_r=Expert.query.filter_by(nom=str(u.lower())).first()
                    if tr_r is not None:
                        trr= tr_r.id
                    if tr_r is None  :
                        trr= 0
                    tr_s=Expert.query.filter_by(nom=str(x.lower())).first()
                    if tr_s is not None:
                        trs= tr_s.id
                    if tr_s is None  :
                        trs= 0
                    pr_s=Expert.query.filter_by(nom=str(z.lower())).first()
                    if pr_s is not None:
                        prs= pr_s.id
                    if pr_s is None  :
                        prs= 0
                    pr_si=Expert.query.filter_by(nom=str(bb.lower())).first()
                    if pr_si is not None:
                        prsi= pr_si.id
                    if pr_si is None  :
                        prsi= 0
                    ra_s=Expert.query.filter_by(nom=str(dd.lower())).first()
                    if ra_s is not None:
                        ras= ra_s.id
                    if ra_s is None  :
                        ras= 0      
                    if tarif is None:
                        taf_base =Tarifs(reference_client=cli.id,code_tva=int(name[2]),
                        referent_as_client=rC,com_as_sur_ca_client=n,cell_dev_ref_responsable=rr,
                        com_cell_dev_ref_responsable=p,cell_dev_ref_agent=dra,com_cell_dev_ref_agent=r,
                        cell_tech_ref_agent=tra,com_cell_tech_Ref_agent=t,cell_tech_ref_responsable=trr,
                        com_cell_tech_ref_responsable=v,cell_tech_ref_suiveur=trs,
                        com_cell_tech_ref_suiveur=y,cell_planif_ref_responsable=prs,
                        com_cell_planif_ref_responsable=aa,cell_planif_ref_suiveur=prsi,
                        com_cell_planif_ref_suiveur=cc,cell_planif_ref_agent_saisie=ras,
                        com_cell_planif_ref_agent_saisie=ee,taux_meuble=ff,edl_prix_std=float(ab),
                        edl_appt_prix_f1=float(ac),edl_appt_prix_f2=float(ad),edl_appt_prix_f3=float(ae),edl_appt_prix_f4=float(af),
                        edl_appt_prix_f5=float(ag),edl_appt_prix_f6=float(ah),edl_pav_villa_prix_t1=float(ai), edl_pav_villa_prix_t2=float(aj),
                        edl_pav_villa_prix_t3=float(ak),edl_pav_villa_prix_t4=float(al),edl_pav_villa_prix_t5=float(am),edl_pav_villa_prix_t6=float(an),
                        edl_pav_villa_prix_t7=float(ao),edl_pav_villa_prix_t8=float(ap),chif_appt_prix_stu=float(aq),
                        chif_appt_prix_f1=float(ar),chif_appt_prix_f2=float(As),chif_appt_prix_f3=float(at),
                        chif_appt_prix_f4=float(au),chif_appt_prix_f5=float(av),chif_pav_villa_prix_t1=float(aw),
                        chif_pav_villa_prix_t2=float(ax),chif_pav_villa_prix_t3=float(ay),chif_pav_villa_prix_t4=float(az),
                        chif_pav_villa_prix_t5=float(ba),chif_pav_villa_prix_t6=float(bc),chif_pav_villa_prix_t7=float(bd),
                        chif_pav_villa_prix_t8=int(be),prix_autre=bf)
                        
                        db.session.add(tai_base)
                        db.session.commit()
                    else:
                        print('exist2')



                    
