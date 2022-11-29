import os
import sys
from tqdm import tqdm
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein

dir = os.environ["DIR"]
name = os.environ["NAME"]

info_file =  dir + '/STEP4_1_out/vep_' + name + '_4_1.csv'
print(info_file)
ensembl_dir="/sc/arion/projects/Itan_lab/minju/annotations/sources/vep_input/" #path to Homo_sapiens.GRCh38.pep.all.fa and Homo_sapiens.GRCh38.pep.abinitio.fa files downloaded from Ensembl.
fasta_dir=dir + '/STEP5_out/' #directory to save protein fasta seq files (seperate fasta files are needed to run netsurfp)
out_dir=dir + '/STEP5_out/' #directory to save netsurfp output

## Read multiple fasta sequences using Biopython into a dictionary
pep_sequences = SeqIO.to_dict(SeqIO.parse(open(ensembl_dir+"Homo_sapiens.GRCh38.pep.all.fa"),'fasta', alphabet=generic_protein))
abinitio_sequences = SeqIO.to_dict(SeqIO.parse(open(ensembl_dir+"Homo_sapiens.GRCh38.pep.abinitio.fa"),'fasta', alphabet=generic_protein))

prot_info=pd.read_csv(info_file, usecols=["ID","Protein_position","Amino_acids","Ref_aa","Alt_aa","ENSP_v","AA_pos"])
##running netsurfp for all proteins in the goflof dataset (later run for all?)
for myid in tqdm(prot_info.ENSP_v.unique()):
    myid = str(myid)
    #check if the fasta file exists
    if not os.path.exists(fasta_dir+myid+".fasta"):
        if myid in pep_sequences.keys():
            SeqIO.write(pep_sequences[myid], "%s/%s.fasta"%(fasta_dir,str(myid)), "fasta")
            ##run netsurfp using the fasta file
            os.system("netsurfp -i %s/%s.fasta -a > %s/%s.out"%(fasta_dir,str(myid),out_dir,myid))
        elif myid in abinitio_sequences.keys():
            SeqIO.write(abinitio_sequences[myid], "%s/%s.fasta"%(fasta_dir,str(myid)), "fasta")
            ##run netsurfp using the fasta file
            os.system("netsurfp -i %s/%s.fasta -a > %s/%s.out"%(fasta_dir,str(myid),out_dir,myid))

