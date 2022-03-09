# This script check the repository integrity
# to made reproducible this work on different machine
# 
SWAP_PATH ="./swap"
TRAINING_DESCRIPTORS_PATH="./descriptors"

TARGET_SEQUENCE_LEN = 6

DESCRIPTORS_TOUSE = ["QSOrder","SOCNumber","APAAC","PAAC","CKSAAGP","CKSAAP","NMBroto","Geary","Moran","BINARY","EAAC","AAINDEX","ZSCALE","BLOSUM62","EGAAC","AAC","DPC","DDE","TPC","GAAC","GDPC","GTPC","CTDC","CTDT","CTDD","CTriad","KSCTriad"]
#DESCRIPTORS_TOUSE = ["QSOrder","SOCNumber","APAAC","PAAC","NMBroto","Geary","Moran","AAINDEX","ZSCALE","EGAAC","DDE","GAAC","GDPC","CTDC","CTDD"]


print("SNARER2: Un bel nome qua?")
