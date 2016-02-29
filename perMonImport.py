from rdflib import Graph
import json



def elasticJson(filePath):
    jsonData = open(filePath).read()
    data = json.loads(jsonData)
    #print data
    print data['hits']
    nestedData = data['hits']['hits']

    for n in nestedData:
        # print n
        # print n["_index"]
        print n['_type']
        print n['_source']
        print n['_source']['plugin']
        print n['_source']['@timestamp']
        # print n['_source']['value']
        print n['_source']['host']
        # print n['_source']['plugin_instance']
        # print n['_source']['type_instance']


def exampleRDF(filePath, format='xml'):
    g = Graph()
    g.parse(filePath, format=format)
    for smt in g:
        print smt


if __name__ == '__main__':
    elasticJson("systemmetrics.json")
    exampleRDF("20130128-PerfMonRec-001.rdf")