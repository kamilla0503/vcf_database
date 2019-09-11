import pandas as pd
import io
import os

def read_vcf(path):
    with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('##')]
    return pd.read_csv(
        io.StringIO(''.join(lines)),
        dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
               'QUAL': str, 'FILTER': str, 'INFO': str},
        sep='\t'
    ).rename(columns={'#CHROM': 'CHROM', 'ID' : 'ID_VARIANT'})

standart_columns = {'CHROM', 'POS','ID_VARIANT','REF', 'ALT', 'QUAL','FILTER', 'INFO', 'FORMAT'}

def get_DP(format_, sample):
    info_DP = list(filter(lambda x: x[0]=="DP", zip(format_.split(":"), sample.split(":"))))
    return info_DP[0][1]

def get_GT(format_, sample, ref, alt):
    info_GT = list(filter(lambda x: x[0]=="GT", zip(format_.split(":"), sample.split(":"))))[0][1].split("/") 
    info_GT  = list(map( lambda x: int(x), info_GT  ))
    nucleotides =  [ref] + alt.split(",")
    genotype = nucleotides[info_GT[0]] + "/" + nucleotides[info_GT[1]]
    return genotype