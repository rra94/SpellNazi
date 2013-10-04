#!/usr/bin/env python
from ast import literal_eval
import re
import sys
import requests
from pandas import DataFrame # http://github.com/pydata/pandas
from requests.auth import HTTPProxyAuth

proxies = {"http":"bsnlproxy.iitk.ac.in"}
auth = HTTPProxyAuth("zaid", "colgate")

           

corpora = dict(eng_us_2012=17, eng_us_2009=5, eng_gb_2012=18, eng_gb_2009=6, eng_2012=15, eng_2009=0, eng_fiction_2012=16, eng_fiction_2009=4, eng_1m_2009=1)


def getNgrams(query, corpus, startYear, endYear, smoothing):
    params = dict(content=query, year_start=startYear, year_end=endYear,
                  corpus=corpora[corpus], smoothing=smoothing)
    req = requests.get('http://books.google.com/ngrams/graph', params=params)
    response = req.content
    #print response
    res = re.findall('data.addRows(.*?);', response.replace('\n',''))
    #print res
    data = literal_eval(res[0])
    return req.url, params['content'], data


def saveData(fname, query, data, url):
    df = DataFrame(data)
    df.columns = ['year'] + [q.strip() for q in query.split(',')]
    df.to_csv(fname, index=False, sep='\t')


def runQuery(argumentString,filename):
    arguments = argumentString.split()
    #print arguments
    query = ' '.join([arg for arg in arguments if not arg.startswith('-')])
    params = [arg for arg in arguments if arg.startswith('-')]
    corpus, startYear, endYear, smoothing = 'eng_2012', 2008, 2008, 50
    printHelp, toSave, toPrint = False, True, False
    
    # parsing the query parameters
    for param in params:
        if '-nosave' in param:
            toSave = False
        elif '-noprint' in param:
            toPrint = False
        elif '-corpus' in param:
            corpus = param.split('=')[1].strip()
        elif '-startYear' in param:
            startYear = int(param.split('=')[1])
        elif '-endYear' in param:
            endYear = int(param.split('=')[1])
        elif '-smoothing' in param:
            smoothing = int(param.split('=')[1])    
        elif '-help' in param:
            printHelp = True
        elif '-quit' in param:
            pass
        else:
            print 'Did not recognize the following argument:', param
    if printHelp:
        print 'See README file.'
    else:
        #print query
        url, urlquery, data = getNgrams(query, corpus, startYear, endYear, smoothing)
        if toPrint:
            print url
            for d in data:
                try:
                    print '%d,' % int(d[0]) + ','.join([str(s) for s in d[1:]])
                except:
                    print ','.join([str(s) for s in d])
        if toSave:
            queries = ''.join(urlquery.replace(',', '_').split())
            #filename = '1.tsv'
            saveData(filename, urlquery, data, url)

'''if __name__ == '__main__':
    argumentString = ' '.join(sys.argv[1:])
    if '-quit' in argumentString.split():
        runQuery(argumentString)    
    if argumentString == '':
        argumentString = raw_input('Enter query (or -help, or -quit):')
    while '-quit' not in argumentString.split():
        try:
            runQuery(argumentString)
        except:
            print 'An error occurred.'
        argumentString = raw_input('Enter query (or -help, or -quit):')'''
