import sys
!{sys.executable} -m pip install rdflib
from rdflib import Graph, Literal, Namespace, RDF, URIRef, OWL
from rdflib.namespace import DC, FOAF
import os

from owlready2 import *

# Create the ontology, name can be changed.
onto = get_ontology("http://test.org/myonto.owl")

with onto:
    class Person(Thing):
        namespace = onto

    ### types of celebrities ###    
    class Celebrity(Person):
        pass

    class Actors(Celebrity):
        pass 

    class Athletes(Celebrity):
        pass

    class Royalty(Celebrity):
        pass

    class Dancers(Celebrity):
        pass

    class Singers(Celebrity):
        pass

    class Politicians(Celebrity):
        pass

    class Influencers(Celebrity):
        pass

    class Models(Celebrity):
        pass

    class Scientists(Celebrity):
        pass

    class Comedians(Celebrity):
        pass

    class Parent(Person):
        pass

    class Child(Person):
        pass
    
    class Occupation(Person):
        pass
    
    class Country(Person):
        pass
    
    class Partner(Person):
        pass
    
    class Relative(Person):
        pass

    ### properties ###

    class childOf(ObjectProperty):
        domain = [Child]
        range = [Parent]

    class parentOf(ObjectProperty):
        domain = [Parent]
        range = [Child]
        inverse_property = childOf
        
    
    class hasRelative(Person >> Relative, SymmetricProperty):
        pass
    
    class partnerOf(Person >> Partner, SymmetricProperty):
        pass

    class birthDate(DataProperty, FunctionalProperty):
        namespace = onto
        domain = [Person]
        range = [str] #this can also be a datetype, but lets use str for now

    class birthPlace(DataProperty, FunctionalProperty):
        namespace = onto
        domain = [Person]
        range = [str]

    class ofGender(DataProperty, FunctionalProperty):
        namespace = onto
        domain = [Person]
        range = [str]
            
    class lengthPage(DataProperty, FunctionalProperty):
        namespace = onto
        domain = [Person]
        range = [int]
        
    class amountWikiLinks(DataProperty, FunctionalProperty):
        namespace = onto
        domain = [Person]
        range = [int]

    class ofNationality(ObjectProperty):
        namespace = onto
        domain = [Person]
        range = [Country]

        # dbpedia: dbo:stateOfOrigin

    class hasOccupation(ObjectProperty):
        namespace = onto
        domain = [Person]
        range = [Occupation]
    
cwd = os.getcwd()
    
onto.save(cwd + "/OntologyFile", format = "rdfxml")
