import json
import itertools
import datetime,xlrd
import xlwt

#wb = xlrd.open_workbook('C:/Users/user/Downloads/Telegram Desktop/TRUSTEXPERTISE_HISTO EDL 201801_202012 (4).xlsx')

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
a=[['REF BAILLEUR', 'SOCIETE BAILLEUR', 'TITRE BAILLEUR', 'NOM BAILLEUR', 'ADRESSE1 BAILLEUR', 'ADRESSE2 BAILLEUR', 'CP BAILLEUR', 'VILLE BAILLEUR', 'NRO FACTURE', 'ABONNEMENT', 'TITRE CONCESS', '23757.0', '2020-10-01 00:00:00', 'TVA EDL', 'PRIX TTC EDL', 'TITRE INTERV', 'NOM INTERV', 'REF LOCATAIRE', 'TITRE LOCATAIRE', 'NOM LOCATAIRE', 'ADRESSE1 BIEN', 'ADRESSE2 BIEN', 'CP BIEN', 'VILLE BIEN', 'CA HT AS', 'TVA AS', 'CA TTC AS', 'CA HT AC', 'CA TTC AC', 'CA HT TRUST', 'TVA TRUST', 'Date chiffrage regle', 'Prix ht chiffrage', '% suiveur chiffrage', '% AS chiffrage', '% manager chiffrage', 'Nom manager chiffrage', '% agent chiffrage', 'Nom agent chiffrage', 'TYPE EDL', 'DATE FACTURE', 'TITRE PROPRIO', 'NOMPROPRIO', 'DATE FACT REGLEE', 'DATE COM REGLEE AS', 'MONTANT COM REGLEE AS', 'DATE COM REGLEE AC', 'MONTANT COM REGLEE AC', 'TYPE LOGEMENT', 'NBRE EDL ABOONEMENT', 'MAIL'
    'CONTACT ENVOI FACT', 'DATE saisie enregistrement', 'CODE AMEXPERT', 'COMMENTAIRE FACTURE', 'TYPE PAIEMENT', 'N° REMISE DE CHEQUE', 'SAISIE TRAITE PAR', 'infos / TRAITEMENT', 'LOGEMENT MEUBLE', 'CODE FACTURATION', 'TYPE DE BIEN', 'surface logement1', 'ETAGE', 'POINTAGE', 'DATE POINTAGE', 'DEVEL', 'DATE EXTRACTION COMPTABLE', '% COM AS DU CLIENT', 'Nom Respon Cell Dev', '% Respon Cell Dev', 'Nom agent Cell Dev', '% Agent Cell Dev', 'Nom Agent CellTech', '% Agent Cell Tech', 'Nom Respon Cell Tech', '% Respon Cell Tech', 'Nom Suiveur Cell Tech', '% Suiveur Cell Tech', 'Nom Respon Cell Planif', '% Respon Cell Planif', 'Nom Suiveur Cell Planif', '% Suiveur Cell Planif', 'Nom Agent saisie Cell Planif', '% Agent saisie CEll planif'],['REF BAILLEUR', 'SOCIETE BAILLEUR', 'TITRE BAILLEUR', 'NOM BAILLEUR', 'ADRESSE1 BAILLEUR', 'ADRESSE2 BAILLEUR', 'CP BAILLEUR', 'VILLE BAILLEUR', 'NRO FACTURE', 'ABONNEMENT', 'TITRE CONCESS', 'NOM CONCESS', 'DATE REALISE EDL', 'TVA EDL', 'PRIX TTC EDL', 'TITRE INTERV', 'NOM INTERV', 'REF LOCATAIRE', 'TITRE LOCATAIRE', 'NOM LOCATAIRE', 'ADRESSE1 BIEN', 'ADRESSE2 BIEN', 'CP BIEN', 'VILLE BIEN', 'CA HT AS', 'TVA AS', 'CA TTC AS', 'CA HT AC', 'CA TTC AC', 'CA HT TRUST', 'TVA TRUST', 'Date chiffrage regle', 'Prix ht chiffrage', '% suiveur chiffrage', '% AS chiffrage', '% manager chiffrage', 'Nom manager chiffrage', '% agent chiffrage', 'Nom agent chiffrage', 'TYPE EDL', 'DATE FACTURE', 'TITRE PROPRIO', 'NOMPROPRIO', 'DATE FACT REGLEE', 'DATE COM REGLEE AS', 'MONTANT COM REGLEE AS', 'DATE COM REGLEE AC', 'MONTANT COM REGLEE AC', 'TYPE LOGEMENT', 'NBRE EDL ABOONEMENT', 'MAIL'
    'CONTACT ENVOI FACT', 'DATE saisie enregistrement', 'CODE AMEXPERT', 'COMMENTAIRE FACTURE', 'TYPE PAIEMENT', 'N° REMISE DE CHEQUE', 'SAISIE TRAITE PAR', 'infos / TRAITEMENT', 'LOGEMENT MEUBLE', 'CODE FACTURATION', 'TYPE DE BIEN', 'surface logement1', 'ETAGE', 'POINTAGE', 'DATE POINTAGE', 'DEVEL', 'DATE EXTRACTION COMPTABLE', '% COM AS DU CLIENT', 'Nom Respon Cell Dev', '% Respon Cell Dev', 'Nom agent Cell Dev', '% Agent Cell Dev', 'Nom Agent CellTech', '% Agent Cell Tech', 'Nom Respon Cell Tech', '% Respon Cell Tech', 'Nom Suiveur Cell Tech', '% Suiveur Cell Tech', 'Nom Respon Cell Planif', '% Respon Cell Planif', 'Nom Suiveur Cell Planif', '% Suiveur Cell Planif', 'Nom Agent saisie Cell Planif', '% Agent saisie CEll planif']]

v=1
ff=[0]


def fun(av):
    ba=[]
    v=0
    for oo in av:
        tr=len(oo)
    
    for i in range(0,tr):
        ba.append(i)
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    for oo in av:
            for q,i in zip(ba,oo) :
                try:
                    ws.write(v, q, i,style1)
                    print(1)
                except:
                    ws.write(v, q, i)
                    print(2)
            v=v+1
    wb.save('example1.xls')         


#print(a)
#for i in ff:
    #for v in i:
        #print(v)
fun(a)
    #fun(a,b,v)
    #v=v+1
    #fun(a,b,v)
    #v=v+1

#print(v)
#wb.save('example1.xls')


        


	    
