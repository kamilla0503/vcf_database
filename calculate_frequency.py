from Models import * 
from Functions import * 
import argparse
from pathlib import Path



database.connect()

parser = argparse.ArgumentParser(description='Calculate_frequency of variant') 

parser.add_argument('--chrom', type=str, help='Chromosome. Values could be from 1 to 22 or X/Y')

parser.add_argument('--pos', type=str, help='Position')

parser.add_argument('--name', type=str, help='Mutation Id')

args = parser.parse_args() 

cursor = database.cursor()

if args.chrom!=None and args.pos!=None:

    cursor.execute("SELECT GT, 1.0 * COUNT(*) / ( SELECT COUNT(*) FROM sample ) as rate FROM ( SELECT * FROM variants WHERE CHROM = %s AND POS = %s  ) as variants_filtered GROUP BY GT"%(args.chrom, args.pos) )

    print(cursor.fetchall()) 


if args.name!=None:
    query = 'SELECT GT, 1.0 * COUNT(*) / ( SELECT COUNT(*) FROM sample ) as rate FROM ( SELECT * FROM variants WHERE ID_VARIANT = ' + r'"%s"'%(args.name) + ') as variants_filtered GROUP BY GT' 
    print(query)
    cursor.execute(query )

    print(cursor.fetchall()) 
    
database.close()