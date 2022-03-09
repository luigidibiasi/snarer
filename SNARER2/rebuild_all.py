# This script check the repository integrity
# to made reproducible this work on different machine

import os
import shutil
from src.common import *

print("Checking integrity...")



#Check NON SNARE
if (not os.path.isfile("./dataset/no_snare.fasta")):
    print("\tNOTSNARE [Not Found]")
    exit()
else:
    print("\tNOTSNARE [OK]")

#Check SNARE
if (not os.path.isfile("./dataset/snare.fasta")):
    print("\tSNARE[Not Found].")
else:
    print("\tSNARE [OK]")



descr = DESCRIPTORS_TOUSE
for d in descr:    
    b=0
    if (b<=30):
        print("\tComputing " + d);
        if (d=="Moran" or d=="Geary" or d=="NMBroto"):
            os.system('python C:/Users/luigi/Desktop/ENTAIL/fibrille/iFeature/codes/'+d+'.py --file ./dataset/no_snare.fasta --nlag 5 --out '+TRAINING_DESCRIPTORS_PATH+'/NOTSNARE_'+str(d)+'.txt')
            os.system('python C:/Users/luigi/Desktop/ENTAIL/fibrille/iFeature/codes/'+d+'.py --file ./dataset/snare.fasta --nlag 5 --out '+TRAINING_DESCRIPTORS_PATH+'/SNARE_'+str(d)+'.txt')            
        else:
            if(d=="CKSAAP" or d=="CKSAAGP"):
                os.system('python C:/Users/luigi/Desktop/ENTAIL/fibrille/iFeature/codes/'+d+'.py ./dataset/no_snare.fasta 4 '+TRAINING_DESCRIPTORS_PATH+'/NOTSNARE_'+str(d)+'.txt')
                os.system('python C:/Users/luigi/Desktop/ENTAIL/fibrille/iFeature/codes/'+d+'.py ./dataset/snare.fasta 4 '+TRAINING_DESCRIPTORS_PATH+'/SNARE_'+str(d)+'.txt')                
            else:
                if(d=="PAAC" or d=="APAAC" or d=="SOCNumber" or d=="QSOrder"):
                    os.system('python C:/Users/luigi/Desktop/ENTAIL/fibrille/iFeature/codes/'+d+'.py ./dataset/no_snare.fasta 5  '+TRAINING_DESCRIPTORS_PATH+'/NOTSNARE_'+str(d)+'.txt')
                    os.system('python C:/Users/luigi/Desktop/ENTAIL/fibrille/iFeature/codes/'+d+'.py ./dataset/snare.fasta 5  '+TRAINING_DESCRIPTORS_PATH+'/SNARE_'+str(d)+'.txt')                    
                else:
                    os.system('python C:/Users/luigi/Desktop/ENTAIL/fibrille/iFeature/iFeature.py --file ./dataset/no_snare.fasta --type '+str(d)+' --out '+TRAINING_DESCRIPTORS_PATH+'/NOTSNARE_'+str(d)+'.txt')
                    os.system('python C:/Users/luigi/Desktop/ENTAIL/fibrille/iFeature/iFeature.py --file ./dataset/snare.fasta --type '+str(d)+' --out '+TRAINING_DESCRIPTORS_PATH+'/SNARE_'+str(d)+'.txt')                    
                    

print("\n\nAll Done!")
print("The training and test sets are available into classificator_inputs directory.")
