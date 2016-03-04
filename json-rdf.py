#!/usr/bin/env python
"""
Copyright 2015, Institute e-Austria, Timisoara, Romania
    http://www.ieat.ro/
Developers:
 * Ioan Dragan, idragan@ieat.ro
 * Gabriel Iuhasz, iuhasz.gabriel@info.uvt.ro

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
from rdflib import RDFS
from rdflib.namespace import FOAF
from rdflib import Graph
import sys
from pprint import pprint


def readJson(filename):
    with open(filename) as data_file:
            data = json.loads(data_file.read())

    dcterms = rdflib.Namespace("http://purl.org/dc/terms/")
    namespace_manager = NamespaceManager(Graph())

    rdf = rdflib.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    ems = rdflib.Namespace("http://open-services.net/ns/ems#")
    ex = rdflib.Namespace("http://example.org#")
    xsd = rdflib.Namespace("http://www.w3.org/2001/XMLSchema#")
    qudt = rdflib.Namespace("http://qudt.org/vocab/unit#")

    rdfs = rdflib.Namespace("http://www.w3.org/2000/01/rdf-schema#")
    crtv = rdflib.Namespace("http://open-services.net/ns/crtv#")
    pm = rdflib.Namespace("http://open-services.net/ns/perfmon#")
    oslc = rdflib.Namespace("http://open-services.net/ns/core#")
    bp = rdflib.Namespace("http://open-services.net/ns/basicProfile#")
    dbp = rdflib.Namespace("http://dbpedia.org/resource/")

    jsonUsefulData = data['hits']['hits']
    g = Graph()

    for d in jsonUsefulData:
        if d['_source']['plugin'] == 'load':
            print d['_source']['shortterm']
            print d['_source']['longterm']
            print d['_source']['midterm']
        elif d['_source']['plugin'] == 'interface':
            print d['_source']['rx']
            print d['_source']['tx']
        elif d['_source']['plugin'] == 'cpu':
            print "CPU DATA"
            cpu = BNode()
            g.add( (rdflib.URIRef('cpu'), RDFS.label, rdflib.Literal('cpu')) )
            g.add( (cpu, RDFS.label, rdflib.Literal('cpu metric')) )
            g.add( (cpu, pm.CpuUsed, rdflib.Literal(d['_source']['value'])) )

            print d['_source']['value']
            print d['_source']['plugin_instance']
            print d['_source']['type_instance']
            print "end CPU data"
        else:
            print d['_source']['value']
            print d['source']
            print d['_source']['type_instance']


        print g.serialize(format = 'xml')


if __name__ == '__main__':
    print sys.argv[1]
    readJson(sys.argv[1])

