#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Models import * 
from Functions import * 

database.bind([Sample, Variants], bind_refs=False, bind_backrefs=False)
database.connect()

database.create_tables([Sample, Variants])

database.close()

