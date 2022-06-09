
import random as rd


dger=["anglais", "aurion", "connexion_ent", "edt", "google", "messagerieENT", "moodle", "office365"]
loisir=["fb", "mail", "leboncoin", "google1", "google2", "insta", "youtube"]
lsdi=["unreal", "google2", "google1"]
mili=["messagerieENT", "mail"]
eo=["ssp", "sdi", "meca", "elec", "info", "cyber", "simu", "ro"]


def Apres_midi (user, h, m):
    requete=""
    zero=""
    if m<=9:
        zero="0"
    if ((h==14)and(0<=m<=15)) or ((h==16)and(10<m<=25)):          # début cours
        if (user in eo) or (user=="prof"):
            n=rd.random()
            if user=="prof":
                n-=0.09
            if TTPP(user):
                n+=0.5
            if n<0.85:
                if user=="sdi":
                    requete=(lsdi[rd.randint(0, len(lsdi)-1)])
                    return(str(h)+":"+zero+str(m)+" connexion: "+ requete)
                else:
                    requete=dger[rd.randint(0, len(dger)-1)]
                    return(str(h)+":"+zero+str(m)+" connexion: "+ requete)
            else:
                requete=(loisir[rd.randint(0, len(loisir)-1)])
                return(str(h)+":"+zero+str(m)+" connexion: "+ requete)
   
    if ((h==14)and(15<m<=59)) or ((h==15)and(10<m<=50)) or ((h==16)and(25<m<=59)) or ((h==17)and(10<m<=59)):          #cours
        if (user in eo) or (user=="prof"):
            n=rd.random()
            if user=="prof":
                n-=0.15
            if n<0.75:
                if user=="sdi":
                    requete=(lsdi[rd.randint(0, len(lsdi)-1)])
                    return(str(h)+":"+zero+str(m)+" connexion: "+ requete)
                else:
                    requete=(dger[rd.randint(0, len(dger)-1)])
                    return(str(h)+":"+zero+str(m)+" connexion: "+ requete)
            else:
                requete=(loisir[rd.randint(0, len(loisir)-1)])
                return(str(h)+":"+zero+str(m)+" connexion: "+ requete)
            
    if ((h==15)and(0<=m<=10)) or ((h==15)and(50<m<=59)) or ((h==16)and(0<=m<=10)) or ((h==17)and(0<=m<=10)):  #pause
        if (user in eo) or (user=="prof"): 
            n=rd.random()
            if user=="prof":
                n-=0.05
            if n<0.1:
                if user=="sdi":
                    requete=(lsdi[rd.randint(0, len(lsdi)-1)])
                    return(str(h)+":"+zero+str(m)+" connexion: "+ requete)
                else:
                    requete=(dger[rd.randint(0, len(dger)-1)])
                    return(str(h)+":"+zero+str(m)+" connexion: "+ requete)
            else:
                requete=(loisir[rd.randint(0, len(loisir)-1)])
                return(str(h)+":"+zero+str(m)+" connexion: "+ requete)
            
    if (14<=h<18)and user=="vorace":    # Vorace
        n=rd.random()
        if 0<=n<0.65:
            requete=(mili[rd.randint(0, len(mili)-1)])
            return(str(h)+":"+zero+str(m)+" connexion: "+ requete)
        else:
            requete=(loisir[rd.randint(0, len(loisir)-1)])
            return(str(h)+":"+zero+str(m)+" connexion: "+ requete)
     
        
def Perturbation():
    n=rd.random()
    if n<=0.55:
        return("RSO")
    elif 0.55<n<=0.75:
        return("RDV")
    elif 0.75<n<=0.87:
        return("malade")
    else:
        return("absence prof")

def TTPP(user):
    if user=="sdi":
        n=rd.random()
        if n<0.1:
            return(True)
    if user=="ssp":
        n=rd.random()
        if n<0.25:
            return(True)
    return(False)


def Trafic_AM(nbSDI, nbSSP, nbP, nbV):
    ni=nbSDI
    ns=nbSSP
    trafic=[]
    h=14
    m=0
    while h<18:
        
        if h==14 or h==16:  # cas du sport
            n=rd.random()
            if n<0.25:
                h+=2
                m=10
            if h==18:
                break
            

        
        while m<60:
            
            p=0
            n=rd.random()
            if n<0.1:
                p=Perturbation()
            mm=0   
            if p=="RDV" or p=="malade":
                mm=rd.randint(0, 3)
            pp=0
            if p=="absence prof":
                pp=nbSDI//10
                
            tpi=0
            if TTPP("sdi"):
                tpi=nbSDI//20
            tpp=0
            if TTPP("ssp"):
                tpp=nbSSP//20
            
            n=rd.random()
            if n>0.75:
                for i in range(int((nbSDI-pp-mm-tpi))):           # SDI
                    trafic.append(Apres_midi("sdi", h, m))
            n=rd.random()
            if n>0.65:
                for i in range(int(n*(nbSSP-pp-mm-tpp))):            # SSP
                    trafic.append(Apres_midi("ssp", h, m))
            n=rd.random()
            if n>0.75:
                for i in range(int(n*nbP)):             # Prof
                    trafic.append(Apres_midi("prof", h, m))
            n=rd.random()
            if n>0.7:
                for i in range(int(n*(nbV-mm))):                  # Vorace
                    trafic.append(Apres_midi("vorace", h, m))
            m+=1
            
            
            if p=="RSO":
                zero=""
                if m<=9:
                    zero="0"
                trafic.append(str(h)+":"+zero+str(m)+" ===========PB RSO===========")
                n=rd.random()
                if n<0.7:
                    m+=rd.randint(0, 10)
                elif n<0.9:
                    m+=rd.randint(10, 30)
                else:
                    m+=rd.randint(30, 60)

        h+=1
        m=0
        nbSDI=ni
        nbSSP=ns
        
        
    f=open("apres-midi.txt", "w")
    for i in range(len(trafic)):
        f.write(trafic[i])
        f.write("\n")
    f.close()
    
    return(trafic)

   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        


