import random as rd


dger=["anglais", "aurion", "connexion_ent", "edt", "google", "messagerieENT", "moodle", "office365"]
loisir=["fb", "mail", "leboncoin", "google1", "google2", "insta", "youtube"]
lsdi=["unreal", "google2", "google1"]
mili=["messagerieENT", "mail"]
eo=["ssp", "sdi", "meca", "elec", "info", "cyber", "simu", "ro"]

def soir(user, h, m):
    requete=""
    zero=""
    if m<=9 :
        zero="0"
    H=""
    if h<=9:
        H="0"
    if (18<=h<20):
        if (user in eo) or user=="prof":
            n=rd.random()
            if n<0.5:
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
            if n<0.75:
                requete=(mili[rd.randint(0, len(mili)-1)])
                return(str(h)+":"+zero+str(m)+" connexion: "+requete)
            else:
                requete=(loisir[rd.randint(0, len(loisir)-1)])
                return(str(h)+":"+zero+str(m)+" connexion: "+requete)
    if (20<=h<22):
        if (user in eo) or user=="prof":
            n=rd.random()
            if n<0.65:
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
            if n<0.1:
                requete=(mili[rd.randint(0, len(mili)-1)])
                return(str(h)+":"+zero+str(m)+" connexion: "+requete)
            else:
                requete=(loisir[rd.randint(0, len(loisir)-1)])
                return(str(h)+":"+zero+str(m)+" connexion: "+requete)
    if (22<=h<=23):
        if (user in eo) or user=="prof":
            n=rd.random()
            if n<0.15:
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
            if n<0.95:
                requete=(mili[rd.randint(0, len(mili)-1)])
                return(H+str(h)+":"+zero+str(m)+" connexion: "+requete)
            else:
                requete=(loisir[rd.randint(0, len(loisir)-1)])
                return(H+str(h)+":"+zero+str(m)+" connexion: "+requete)
    if (0<=h<6) or (h==6 and 0<=m<30):
        if (user in eo) or user=="prof":
            n=rd.random()
            if n<0.2:
                if user=="sdi":
                    requete=(lsdi[rd.randint(0, len(lsdi)-1)])
                    return(H+str(h)+":"+zero+str(m)+" connexion: "+ requete)
                else:
                    requete=(dger[rd.randint(0, len(dger)-1)])
                    return(H+str(h)+":"+zero+str(m)+" connexion: "+ requete)
            else:
                requete=(loisir[rd.randint(0, len(loisir)-1)])
                return(H+str(h)+":"+zero+str(m)+ " connexion: "+ requete)
        if user=="vorace":
            n=rd.random()
            if n<0.7:
                requete=(mili[rd.randint(0, len(mili)-1)])
                return(H+str(h)+":"+zero+str(m)+" connexion: "+requete)
            else:
                requete=(loisir[rd.randint(0, len(loisir)-1)])
                return(H+str(h)+":"+zero+str(m)+" connexion: "+requete)           
            
         
def RSO():
    n=rd.random()
    if n<0.01:
        return(True)
    return(False)
         
            
def trafic_soir (nbsdi, nbssp, nbp, nbv):
    trafic=[]
    h=18
    m=0
    while 1:
        while m<60:
            if 18<=h<20:
                for i in range(nbsdi):
                    n=rd.random()
                    if n<0.1:
                        trafic.append(soir("sdi", h, m))
                for i in range(nbssp):
                    n=rd.random()
                    if n<0.1:
                        trafic.append(soir("ssp", h, m))
                for i in range(nbp):
                    n=rd.random()
                    if n<0.2:
                        trafic.append(soir("prof", h, m))
                for i in range(nbv):
                    n=rd.random()
                    if n<0.7:
                        trafic.append(soir("vorace", h, m))
            elif 20<=h<22:
                for i in range(nbsdi):
                    n=rd.random()
                    if n<0.3:
                        trafic.append(soir("sdi", h, m))
                for i in range(nbssp):
                    n=rd.random()
                    if n<0.3:
                        trafic.append(soir("ssp", h, m))
                for i in range(nbp):
                    n=rd.random()
                    if n<0.5:
                        trafic.append(soir("prof", h, m))
                for i in range(nbv):
                    n=rd.random()
                    if n<0.4:
                        trafic.append(soir("vorace", h, m))
            elif 22<=h<=23:
                for i in range(nbsdi):
                    n=rd.random()
                    if n<0.2:
                        trafic.append(soir("sdi", h, m))
                for i in range(nbssp):
                    n=rd.random()
                    if n<0.2:
                        trafic.append(soir("ssp", h, m))
                for i in range(nbp):
                    n=rd.random()
                    if n<0.2:
                        trafic.append(soir("prof", h, m))
                for i in range(nbv):
                    n=rd.random()
                    if n<0.1:
                        trafic.append(soir("vorace", h, m))
            elif 0<=h<=6:
                for i in range(nbsdi):
                    n=rd.random()
                    if n<0.01:
                        trafic.append(soir("sdi", h, m))
                for i in range(nbssp):
                    n=rd.random()
                    if n<0.01:
                        trafic.append(soir("ssp", h, m))
                for i in range(nbp):
                    n=rd.random()
                    if n<0.005:
                        trafic.append(soir("prof", h, m))
                for i in range(nbv):
                    n=rd.random()
                    if n<0.001:
                        trafic.append(soir("vorace", h, m))
                        
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
                    
            m+=1
            if h==6 and m==30:
                break     
            
        if h==6 and m==30:
            break  
        m=0
        if h==23:
            h=0
        else:
            h+=1
        
    f=open("soiree.txt", "w")
    for i in range(len(trafic)):
        if trafic[i]!=None:
            f.write(trafic[i])
            f.write("\n")
    f.close()
    return(trafic)
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            