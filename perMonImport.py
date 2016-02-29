from rdflib import Graph
import json
import sys



def elasticJson(filePath):
    jsonData = open(filePath).read()
    data = json.loads(jsonData)
    #print data
    print data['hits']
    nestedData = data['hits']['hits']

    for n in nestedData:
        #print n
        # print n["_index"]
        print n['_type']
        print n['_source']
        print n['_source']['plugin']
        print n['_source']['@timestamp']

        if n['_source']['plugin'] == 'load':
            print n['_source']['shortterm']
            print n['_source']['longterm']
            print n['_source']['midterm']
        elif n['_source']['plugin'] == 'interface':
            print n['_source']['rx']
            print n['_source']['tx']
        elif n['_source']['plugin'] == 'cpu':
            print n['_source']['value']
            print n['_source']['plugin_instance']
            print n['_source']['type_instance']
        else:
            print n['_source']['value']
            print n['_source']['type_instance']

        print n['_source']['host']




def exampleRDF(filePath, format='xml'):
    g = Graph()
    g.parse(filePath, format=format)
    for smt in g:
        print smt


if __name__ == '__main__':
    elasticJson("systemmetrics.json")

    # exampleRDF("20130128-PerfMonRec-001.rdf")