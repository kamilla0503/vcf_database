#!/usr/bin/env python
# coding: utf-8

from Models import * 
from Functions import * 
import argparse
from pathlib import Path


database.connect()


parser = argparse.ArgumentParser(description='Add new information from files in the folder') 
parser.add_argument('indir', type=str, help='A folder path')
args = parser.parse_args() 



for fn in Path(args.indir).glob("*.vcf"):
     
    sample_type = str(fn).split(".")[1]
 
    data = read_vcf(fn)
    sample_names = list( filter(lambda x: x not in standart_columns, list(data)))
    for s in sample_names:
        data["DP"] = data.apply(lambda x: get_DP(x["FORMAT"], x[s]), axis=1)
        data["GT"] = data.apply(lambda x: get_GT(x["FORMAT"], x[s], x["REF"], x["ALT"]), axis=1)
        sample_citonumber = int(s.split("_")[1])
        try:
            sample_to_base = Sample.create(Sample_name = sample_citonumber, Type = sample_type)
            with database.atomic():
                data_source = data[["CHROM", "POS", "ID_VARIANT", "DP", "GT"]].to_dict(orient='records')
                for data_dict in data_source:
                    Variants.create(sample= sample_to_base,**data_dict)
        except IntegrityError:
            continue
    


database.close()
 




