from bs4 import BeautifulSoup
import urllib2
import re

from click import *
from _mysql import *
from openpyxl import *
import os

import uuid
import hashlib
from random import randint

userinterests= ['Projects', 'Startups', 'Travel', 'Food', 'Music', 'Pets', 'Relationships']

def getLinks():
    page=urllib2.urlopen("https://raw.githubusercontent.com/kusaraju-padala/GMRIT_InternRecruitTest/master/Buckton_Castle")
    soup = BeautifulSoup(page)
    f=open("links.txt","w+")
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        f.write(link.get('href'))
        f.write("\n") 
    f.close()



@group()
@pass_context
def mysql(context):
    con=connect('localhost','root','')
    context.obj['conn']=con

@mysql.command()
@argument('dbname',required=True,default="db_sample",nargs=1)
@argument('tablename',required=True,default="Students",nargs=1)
@pass_context
def createdb(context,dbname,tablename):
    '''Create database along with the table'''
    con=context.obj['conn']
    query='CREATE DATABASE '+dbname+';'
    con.query(query)
    echo('Database "' + dbname + '" created successfully!')
    query = 'USE ' + dbname + ';'
    con.query(query)
    query='CREATE TABLE '+tablename+'(interestid varchar(100),interestname varchar(20),userid varchar(100));'
    con.query(query)
    echo(tablename+'Table'+ created successfully!')
         
@mysql.command()
@argument('dbname',required=True,default="db_sample",nargs=1)
@pass_context
def populatedb(context,dbname):
    con=context.obj['conn']
    query='USE '+dbname+';'
    con.query(query)
    for i in range(100000):
        id = str(uuid.uuid4())
        interestid=hashlib.md5(id).hexdigest()
        interestname=userinterests[randint(0, 5)]
        query='INSERT INTO user VALUES('"'+interestid+'", "'+interestname+'","'+id+'");'
        con.query(query)
         
if __name__=="__main__":
    getlinks()
    mysql(obj={})


