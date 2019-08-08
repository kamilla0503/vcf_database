import sqlite3
from peewee import *

database = SqliteDatabase('Mutations.db')

class BaseModel(Model):
    class Meta:
        database = database
        
class Sample(BaseModel):
    Sample_name = IntegerField(primary_key=True, unique=True)
    Type = CharField(constraints = [Check('Type == "Exome" OR Type=="Panel"')], max_length=5)        
    
class Mutations(BaseModel):
    sample = ForeignKeyField(Sample, backref='Sample')
    chromosome = CharField(max_length =  2)
    position =  CharField()
    mutation_name = CharField()
    read_depth = IntegerField()
    genotype = CharField()    