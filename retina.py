# -*- coding: utf-8 -*-
import numpy as np

n=10     # мест
Lot=1     # школьники

while True:
    try:
        n = int(input("Please enter lot of Place"))
        Lot = int(input("Please enter num a Visitor"))
        break
    except ValueError:
        print("Invalid input.  Please try again")
        
def finddeep(Place):
    chunks=[Place[s] for s in np.ma.clump_unmasked(np.ma.masked_invalid(Place))]
    chunksbysort=np.array(sorted(chunks
                       , key=len
                       , reverse=True)
                        )
    bedeep=round(np.array([chunksbysort[0]]).mean(axis=1))
    return int(bedeep)

def FreePlace(Place):
    fp=[Place[s] for s in np.ma.clump_unmasked(np.ma.masked_invalid(Place))]
    return len(fp[0]),len(fp[-1])
    
Place = np.zeros(n)
Place =Place[1:-1]
for v in range(len(Place)): Place[v]=v+1    

if __name__ == '__main__':
    for l in range(Lot):
        bevact=finddeep(Place)
        Place[bevact-1]=np.nan
        
    result=FreePlace(Place)
    print '---free place by extreme:',result
