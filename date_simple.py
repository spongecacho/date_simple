"""
Created on Mon Apr  9 13:57:49 2018

@author: pnix
"""
import datetime

KNOWN_FORMATS = {'DD - Mon - YY' : '',
                 'YYYY/DD/MM' : ''}                                             #I plan to create a list of known date formats, possibly using regular expressions, to use in
                                                                                #get_date_string instead of repeated '.replace', however I haven't gotten to this step yet

def get_date_object(date = None):
    if date == None:
        date = datetime.datetime.today()
    else:
        date = datetime.datetime.strptime(date,'%Y-%m-%d')
    return date

def get_date_string(date_object = None, d_format = '%Y-%m-%d'):
    if date_object == None:
        date_object = datetime.datetime.today()
    if d_format != None:
        d_format = d_format.replace('YYYY', '%Y').replace('YY','%y').replace('DD','%d').replace('MM','%m').replace('Mon','%b')
    return date_object.strftime(d_format)

def main():
    print(get_date_object())
    print(get_date_string())
    print(get_date_object(date = '2018-02-26'))
    dateobj = get_date_object(date = '2018-02-22')
    print(get_date_string(date_object = dateobj, d_format = 'Mon-DD-YYYY'))
    

if __name__ == '__main__':
    main()