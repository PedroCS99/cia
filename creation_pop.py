from population import *

nombre_voraces=4
nombre_sdi=8
nombre_ssp=8

pop=dict()

for k in range(1,nombre_voraces+1):
    pop["v"+str(k)]=Vorace(6,30)
    pop["v"+str(k)].update_ip(k)
for k in range(1,nombre_sdi+1):
    pop["sdi"+str(k)]=SDI(6,30)
    pop["sdi"+str(k)].update_ip(k)
for k in range(1,nombre_ssp+1):
    pop["ssp"+str(k)]=SSP(6,30)
    pop["ssp"+str(k)].update_ip(k)
