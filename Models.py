from peewee import *
import sqlite3

database = SqliteDatabase('Variants.db')

class BaseModel(Model):
    class Meta:
        database = database
        
class Sample(BaseModel):
    Sample_name = IntegerField(primary_key=True, unique=True)
    Type = CharField(constraints = [Check('Type == "Exome" OR Type=="Panel"')], max_length=5)        
    
class Variants(BaseModel):
    sample = ForeignKeyField(Sample, backref='Sample')
    CHROM = CharField(max_length =  2)
    POS =  CharField()
    ID_VARIANT = CharField()
    DP = IntegerField()
    GT = CharField()    

    