import time
import random as rd
from creation_pop import *
import sys
import os
import threading
interface = sys.argv[1]

requete_travail={"voraces_Bureau":{1:"mail_peigne",2:"ENT_peigne",3:"Google_peigne"},
                    "sdi_DGER_cyber":{1:"mail",2:"moodle",3:"cyberrange",4:"cyberrange",5:"cyberrange"},
                    "sdi_peigne_cyber":{1:"mail_peigne",2:"moodle_peigne",3:"ENT_peigne"},
                    "sdi_DGER_simu":{1:"mail",2:"moodle",3:"unreal",4:"unreal",5:"youtube",6:"youtube"},
                    "sdi_peigne_simu":{1:"mail_peigne",2:"moodle_peigne",3:"ENT_peigne"},
                    "sdi_DGER_RO":{1:"mail",2:"moodle",3:"visualstudio",4:"visualstudio",5:"visualstudio"},
                    "sdi_peigne_RO":{1:"mail_peigne",2:"moodle_peigne",3:"ENT_peigne"},
                    "sdi_DGER_meca":{1:"mail",2:"moodle",3:"matlab",4:"matlab",5:"matlab"},
                    "sdi_peigne_meca":{1:"mail_peigne",2:"moodle_peigne",3:"ENT_peigne"},
                    "sdi_DGER_elec":{1:"mail",2:"moodle",3:"msatlab",4:"matlab",5:"matlab"},
                    "sdi_peigne_elec":{1:"mail_peigne",2:"moodle_peigne",3:"ENT_peigne"},
                    "ssp_DGER":{1:"mail",2:"moodle",3:"office365"},
                    "ssp_peigne":{1:"mail_peigne",2:"moodle_peigne",3:"ENT_peigne"}}
requete_loisir={"voraces_Bureau":{1:"fb_peigne",2:"wa_peigne",3:"insta_peigne"},
                    "sdi_DGER_cyber":{1:"fb",2:"wa",3:"insta"},
                    "sdi_peigne_cyber":{1:"fb_peigne",2:"wa_peigne",3:"insta_peigne",4:"netflix_peigne",5:"streaming_peigne",6:"google_peigne"},
                    "sdi_DGER_simu":{1:"fb",2:"wa",3:"insta"},
                    "sdi_peigne_simu":{1:"fb_peigne",2:"wa_peigne",3:"insta_peigne",4:"netflix_peigne",5:"streaming_peigne",6:"google_peigne"},
                    "sdi_DGER_RO":{1:"fb",2:"wa",3:"insta"},
                    "sdi_peigne_RO":{1:"fb_peigne",2:"wa_peigne",3:"insta_peigne",4:"netflix_peigne",5:"streaming_peigne",6:"google_peigne"},
                    "sdi_DGER_meca":{1:"fb",2:"wa",3:"insta"},
                    "sdi_peigne_meca":{1:"fb_peigne",2:"wa_peigne",3:"insta_peigne",4:"netflix_peigne",5:"streaming_peigne",6:"google_peigne"},
                    "sdi_DGER_elec":{1:"fb",2:"wa",3:"insta"},
                    "sdi_peigne_elec":{1:"fb_peigne",2:"wa_peigne",3:"insta_peigne",4:"netflix_peigne",5:"streaming_peigne",6:"google_peigne"},
                    "ssp_DGER":{1:"fb",2:"wa",3:"insta"},
                    "ssp_peigne":{1:"fb_peigne",2:"wa_peigne",3:"insta_peigne"}}

def reveil_class(start_h,start_min,population):
    f=open("reveil.txt",'w')
    while (start_h!=7) or (start_min!=25):
        for nom,personne in population.items():
            if personne.reveille and personne.lieu!="absent":
                if nom[0:1]=='v':
                    requete=requete_loisir["voraces"+"_"+str(personne.lieu)][rd.randint(1,len(requete_loisir["voraces"+"_"+str(personne.lieu)]))]
                elif nom[0:3]=='sdi':
                    requete=requete_loisir["sdi"+"_"+str(personne.lieu)+"_"+str(personne.specialite)][rd.randint(1,len(requete_loisir["sdi"+"_"+str(personne.lieu)+"_"+str(personne.specialite)]))]
                elif nom[0:3]=="ssp":
                    alea=rd.randint(1,len(requete_loisir["ssp"+"_"+str(personne.lieu)]))
                    requete=requete_loisir["ssp"+"_"+str(personne.lieu)][alea]
                if len(requete.split('_'))>1:
                    pass
                else:
                    f.write(f"{str(start_h)}:{str(start_min)} : requête {requete} effectuée par {nom} {personne.specialite}\n".format(start_h,start_min,requete,nom,personne.specialite))
            if not personne.reveille:
                #f.write(f"{str(start_h)}:{str(start_min)} : oups je suis {nom} {personne.specialite} et je dors \n".format(start_h,start_min,nom,personne.specialite))
                pass
            personne.update_reveil(start_h,start_min)
            if personne.lieu=="absent":    
                personne.update_arrivee(start_h,start_min)
        start_min+=1
        if start_min==60:
            start_h+=1
            start_min=0
    f.write("\n \n RASSO \n \n \n")
    f.close()
    return(start_h,start_min)





def apres_rasso_class(start_h,start_min,population):
    f=open("apres_rasso.txt",'w')
    while (start_h!=7) or (start_min!=50):
        for nom,personne in population.items():
            if personne.reveille and personne.lieu!="absent":
                if nom[0:1]=='v':
                    requete=requete_travail["voraces"+"_"+str(personne.lieu)][rd.randint(1,len(requete_travail["voraces"+"_"+str(personne.lieu)]))]
                elif nom[0:3]=='sdi':
                    choix = rd.randint(1,2)
                    if choix ==1 : 
                        requete=requete_loisir["sdi"+"_"+str(personne.lieu)+"_"+str(personne.specialite)][rd.randint(1,len(requete_loisir["sdi"+"_"+str(personne.lieu)+"_"+str(personne.specialite)]))]
                    else:
                        requete=requete_travail["sdi"+"_"+str(personne.lieu)+"_"+str(personne.specialite)][rd.randint(1,len(requete_travail["sdi"+"_"+str(personne.lieu)+"_"+str(personne.specialite)]))]
                elif nom[0:3]=="ssp":
                    choix = rd.randint(1,2)
                    if choix ==1 : 
                        requete=requete_loisir["ssp"+"_"+str(personne.lieu)][rd.randint(1,len(requete_loisir["ssp"+"_"+str(personne.lieu)]))]
                    else:
                        requete=requete_travail["ssp"+"_"+str(personne.lieu)][rd.randint(1,len(requete_travail["ssp"+"_"+str(personne.lieu)]))]
                if len(requete.split('_'))>1:
                    pass
                else:
                    f.write(f"{str(start_h)}:{str(start_min)} : requête {requete} effectuée par {nom} {personne.specialite}\n".format(start_h,start_min,requete,nom,personne.specialite))

            personne.update_reveil(start_h,start_min)
        start_min+=1
        if start_min==60:
            start_h+=1
            start_min=0
    f.write("\n \n DEPART DGER \n \n \n")
    f.close()
    return(start_h,start_min)


def cours_matin(start_h,start_min,nom,personne):
    #f=open("matin.txt",'w')
    while (start_h!=11) or (start_min!=50):
        if (start_h==8 and start_min==1) or (start_h==9 and start_min==50):
            personne.update_TTPP()
        if personne.reveille:
            if personne.lieu!="absent":
                if personne.motivation:
                    if rd.randint(1,3)>=2:
                        if nom[0:1]=='v':
                            requete=requete_travail["voraces"+"_"+str(personne.lieu)][rd.randint(1,len(requete_travail["voraces"+"_"+str(personne.lieu)]))]
                        elif nom[0:3]=='sdi':
                            requete=requete_travail["sdi"+"_"+str(personne.lieu)+"_"+str(personne.specialite)][rd.randint(1,len(requete_travail["sdi"+"_"+str(personne.lieu)+"_"+str(personne.specialite)]))]
                        elif nom[0:3]=="ssp":
                            requete=requete_travail["ssp"+"_"+str(personne.lieu)][rd.randint(1,len(requete_travail["ssp"+"_"+str(personne.lieu)]))]
                        if len(requete.split('_'))>1:
                            pass
                        else:
                            #f.write(f"{str(start_h)}:{str(start_min)}:{requete}:{personne.ip}\n".format(start_h,start_min,requete,personne.ip))
                            print(f"{nom}:{requete}:{personne.ip}\n".format(nom,requete,personne.ip))
                            try:
                                os.system("tcpreplay-edit"+" --mtu-trunc "+ " -i " + interface +" " +" --srcipmap=0.0.0.0/0:"+personne.ip + "/32 "+ " requetes/"+requete+".pcap"+" 2>/dev/null" )
                            except: 
                                os.system("tcpreplay-edit"+" --mtu-trunc "+ " -i " + interface +" " +" --srcipmap=0.0.0.0/0:"+personne.ip + "/32 "+ " requetes/google.pcap"+" 2>/dev/null" )
                            #time.sleep(5)
                else:
                    if rd.randint(1,3)>=2:
                        if nom[0:1]=='v':
                            requete=requete_loisir["voraces"+"_"+str(personne.lieu)][rd.randint(1,len(requete_loisir["voraces"+"_"+str(personne.lieu)]))]
                        elif nom[0:3]=='sdi':
                            requete=requete_loisir["sdi"+"_"+str(personne.lieu)+"_"+str(personne.specialite)][rd.randint(1,len(requete_loisir["sdi"+"_"+str(personne.lieu)+"_"+str(personne.specialite)]))]
                        elif nom[0:3]=="ssp":
                            requete=requete_loisir["ssp"+"_"+str(personne.lieu)][rd.randint(1,len(requete_loisir["ssp"+"_"+str(personne.lieu)]))]
                        if len(requete.split('_'))>1:
                            pass
                        else:
                            #f.write(f"{str(start_h)}:{str(start_min)}:{requete}:{personne.ip}\n".format(start_h,start_min,requete,personne.ip))
                            print(f"{nom}:{requete}:{personne.ip}\n".format(nom,requete,personne.ip))
                            try:
                                os.system("tcpreplay-edit"+" --mtu-trunc "+ " -i " + interface +" " +" --srcipmap=0.0.0.0/0:"+personne.ip + "/32 "+ " requetes/"+requete+".pcap"+" 2>/dev/null" )
                            except:
                                os.system("tcpreplay-edit"+" --mtu-trunc "+ " -i " + interface +" " +" --srcipmap=0.0.0.0/0:"+personne.ip + "/32 "+ " requetes/google.pcap"+" 2>/dev/null" )
                            

                        #time.sleep(5)
        personne.update_lieu()
        personne.update_motivation()
        #print(start_h,start_min)
        start_min+=1
        if start_min==60:
            start_h+=1
            start_min=0
    #f.close()
    return(start_h,start_min)
#h2,m2=cours_matin(8,0,pop)


if __name__=='__main__':
    h,m=reveil_class(6,30,pop)
    h1,m1=apres_rasso_class(h,30,pop)
    nombre=len(pop)
    threads=dict()
    for a,b in pop.items():
        threads[a] = threading.Thread(target=cours_matin,args=(8,0,a,b,))
    for a,b in pop.items():
        threads[a].start()
    for a,b in pop.items():
        threads[a].join()