# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 10:56:47 2015

@author: ahmedov
"""

import csv
import sys
import json

fieldnames = ["COMPANY","COUNTRY","INDUSTRY"]

def convert(filename):
    csv_filename=filename[0]
    print "Opening CSV file: ",csv_filename
    f=open(csv_filename, 'rU')
    csv_reader = csv.DictReader(f,fieldnames, delimiter=';')
    #for row in csv_reader:
    #   yield [unicode(cell, 'utf-8') for cell in row]
    json_filename = csv_filename.split(".")[0]+"_1line.json"
    print "Saving JSON to file: ", json_filename
    jsonf = open (json_filename,'w')
    print "Opened JSON file to write"
   # for row in csv_reader:
    #    print row
     #   data = json.dumps(row,ensure_ascii=False)
      #  jsonf.write(data);
       # jsonf.write("\n");
    data = json.dumps([r for r in csv_reader], ensure_ascii=False).decode('latin-1').encode('utf8')
    jsonf.write(data.decode("latin-1").encode("UTF-8"))
    print "writing to file complete"
    f.close()
    jsonf.close()
if __name__=="__main__":
    convert(sys.argv[1:])
    
