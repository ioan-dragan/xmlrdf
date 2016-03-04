#!/usr/bin/env python 
"""
Copyright 2015, Institute e-Austria, Timisoara, Romania
    http://www.ieat.ro/
Developers:
 * Ioan Dragan, idragan@ieat.ro

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import json
import rdflib
from rdflib import URIRef, BNode, Literal
from rdflib.namespace import Namespace, NamespaceManager
from rdflib import RDFS, XSD
from rdflib import Graph
import sys




def readJson(filename):
    with open(filename) as data_file:
        data = json.loads(data_file.read())



    dcterms = rdflib.Namespace("http://purl.org/dc/terms/")
    #namespace_manager = NamespaceManager(Graph())
    rdf = rdflib.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    ems = rdflib.Namespace("http://open-services.net/ns/ems#")
    ex = rdflib.Namespace("http://example.org#")
    xsd = rdflib.Namespace("http://www.w3.org/2001/XMLSchema#")
    qudt = rdflib.Namespace("http://qudt.org/vocab/unit#")
    dcterms = rdflib.Namespace("http://purl.org/dc/terms/")

    rdfs = rdflib.Namespace("http://www.w3.org/2000/01/rdf-schema#")
    crtv = rdflib.Namespace("http://open-services.net/ns/crtv#")
    pm = rdflib.Namespace("http://open-services.net/ns/perfmon#")
    oslc = rdflib.Namespace("http://open-services.net/ns/core#")
    bp = rdflib.Namespace("http://open-services.net/ns/basicProfile#")
    dbp = rdflib.Namespace("http://dbpedia.org/resource/")

    nestedData = data['hits']['hits']
    g = Graph()
    g.bind('ems', ems)
    g.bind('dcterms', dcterms)
    counter = 0
    for d in nestedData:
        if d['_source']['plugin'] == 'load':
            print d['_source']['shortterm']
            print d['_source']['longterm']
            print d['_source']['midterm']
        elif d['_source']['plugin'] == 'interface':
            print d['_source']['rx']
            print d['_source']['tx']
        elif d['_source']['plugin'] == 'cpu':
            print 'CPU Data'
            cpu = URIRef('http://perfmon-provider.example.org/rec001#cpuutil' + str(d['_source']['value']))
            g.add((rdflib.URIRef('http://perfmon-provider.example.org/rec001#cpuutil10'), RDFS.label, rdflib.Literal('CPU Utilization')))
            g.add((cpu, ems.numericValue, rdflib.Literal(d['_source']['value'])))
            g.add((cpu, ems.unitOfMeasure, rdflib.URIRef('http://dbpedia.org/resource/Percentage')))
            g.add((cpu, ems.metric, rdflib.URIRef('http://open-services.net/ns/perfmon#CpuUsed')))
            g.add((cpu, dcterms.title, rdflib.Literal('CPU Utilization')))
            g.add((cpu, rdf.type, rdflib.URIRef('http://open-services.net/ns/ems#Measure')))
            #g.add((cpu, rdf.type, rdflib.Literal(d['_source']['@timestamp'], datatype=XSD.data)))
            print d['_source']['value']
            print d['_source']['plugin_instance']
            print d['_source']['type_instance']
            print ' End CPU Data'
        else:
            print d['_source']['value']
            print d['_source']['type_instance']
        counter += 1

    print g.serialize(format='xml')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        readJson("systemmetrics.json")
    else:
        print sys.argv[1]
        readJson(sys.argv[1])

