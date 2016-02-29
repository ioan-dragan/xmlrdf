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
from rdflib import Namespace
from rdflib import RDF
from rdflib.namespace import FOAF
from rdflib import Graph
import sys
from pprint import pprint


def readJson(filename):
    with open(filename) as data_file:
        data = json.loads(data_file.read())
    pprint(data)
    g = rdflib.Graph()

    dcterms = rdflib.Namespace("http://purl.org/dc/terms/")
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


    counter = 0
    for maps in data['maps']:
        #get in the maps and collect attributes
        for i in maps:
            g.add((rdflib.URIRef('maps.'+str(counter)), rdflib.RDFS.label, rdflib.Literal(i)))
            g.add((rdflib.URIRef('maps.'+str(counter)), rdflib.RDFS.label, rdflib.Literal(maps[i])))
        counter += 1
        print len(maps)

    #g.add((rdflib.URIRef('maps:id'), rdflib.RDFS.label, rdflib.Literal('id')))
    #g.add((rdflib.URIRef('maps:id'), FOAF.value, rdflib.Literal(12)))
    print g.serialize(format='xml')


def printBob():
    g = rdflib.Graph()
    g.add((rdflib.URIRef('urn:bob'), rdflib.RDFS.label, rdflib.Literal('bob')))
    print g.serialize(format='xml')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        readJson("example.json")
    else:
        print sys.argv[1]
        readJson(sys.argv[1])

