
import random as rd

dger=["anglais", "aurion", "connexion_ent", "edt", "google", "messagerieENT", "moodle", "office365"]
loisir=["fb", "mail", "leboncoin", "google1", "google2", "insta", "youtube"]
lsdi=["unreal", "google2", "google1"]
mili=["messagerieENT", "mail"]
eo=["ssp", "sdi", "meca", "elec", "info", "cyber", "simu", "ro"]

def midi(user, h, m):
    requete=""
    zero=""
    if m<=9:
        zero="0"
    if h==12:
        if (user in eo) or user=="prof":
            n=rd.random()
            if n<0.1:
                if user=="sdi":
                    requete=(lsdi[rd.randint(0, len(lsdi)-1)])
                    return(str(h)+":"+zero+str(m)+" connexion: "+ requete)
                else:
                    requete=(dger[rd.randint(0, len(dger)-1)])
                    return(str(h)+":"+zero+str(m)+" connexion: "+ requete)
            else:
                requete=(loisir[rd.randint(0, len(loisir)-1)])
                return(str(h)+":"+zero+str(m)+ " connexion: "+ requete)
        if user=="vorace":
            n=rd.random()
            if n<0.65:
                requete=(mili[rd.randint(0, len(mili)-1)])
                return(str(h)+":"+zero+str(m)+" connexion: "+requete)
            else:
                requete=(mili[rd.randint(0, len(mili)-1)])
                return(str(h)+":"+zero+str(m)+" connexion: "+requete)
    elif h==13:
        if (user in eo) or user=="prof":
            n=rd.random()
            if n<0.2:
                if user=="sdi":
                    requete=(lsdi[rd.randint(0, len(lsdi)-1)])
                    return(str(h)+":"+zero+str(m)+" connexion: "+ requete)
                else:
                    requete=(dger[rd.randint(0, len(dger)-1)])
                    return(str(h)+":"+zero+str(m)+" connexion: "+ requete)
            else:
                requete=(loisir[rd.randint(0, len(loisir)-1)])
                return(str(h)+":"+zero+str(m)+ " connexion: "+ requete)
        if user=="vorace":
            n=rd.random()
            if n<0.7:
                requete=(mili[rd.randint(0, len(mili)-1)])
                return(str(h)+":"+zero+str(m)+" connexion: "+requete)
            else:
                requete=(loisir[rd.randint(0, len(loisir)-1)])
                return(str(h)+":"+zero+str(m)+" connexion: "+requete)
            
            

def RSO():
    n=rd.random()
    if n<0.01:
        return(True)
    return(False)


def trafic_midi(nbsdi, nbssp, nbv, nbp):
    h=12
    m=0
    trafic=[]
    while h<14:
        print(h)
        while m<60:
            if h==12:
                for i in range(nbsdi):
                    n=rd.random()
                    if n<0.1:
                        trafic.append(midi("sdi", h, m))
                for i in range(nbssp):
                    n=rd.random()
                    if n<0.1:
                        trafic.append(midi("ssp", h, m))
                for i in range(nbp):
                    n=rd.random()
                    if n<0.1:
                        trafic.append(midi("prof", h, m))
                for i in range(nbv):
                    n=rd.random()
                    if n<0.15:
                        trafic.append(midi("vorace", h, m))
            elif h==13:
                for i in range(nbsdi):
                    n=rd.random()
                    if n<0.3:
                        trafic.append(midi("sdi", h, m))
                for i in range(nbssp):
                    n=rd.random()
                    if n<0.3:
                        trafic.append(midi("ssp", h, m))
                for i in range(nbp):
                    n=rd.random()
                    if n<0.2:
                        trafic.append(midi("prof", h, m))
                for i in range(nbv):
                    n=rd.random()
                    if n<0.5:
                        trafic.append(midi("vorace", h, m))
            m+=1
            
            rso=RSO()
            if rso:
                trafic.append("PB RSO")
                n=rd.random()
                if n<0.5:
                    m+=rd.randint(0, 5)
                elif n<0.75:
                    m+=rd.randint(5, 20)
                else:
                    m+=rd.randint(20, 60)
                    
            
        h+=1
        m=0
            
    f=open("midi.txt", "w")
    for i in range(len(trafic)):
        if trafic[i]!=None:
            f.write(trafic[i])
            f.write("\n")
    f.close()
    
    return(trafic)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    