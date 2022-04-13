'''
Query 1 shows a query which mapped all data dbpedia to the ontology and from that point
was transformed to a csv format

'''


query_1 = """PREFIX onto: <http://test.org/myonto.owl>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbp: <http://dbpedia.org/property/>

SELECT * 
     WHERE { GRAPH <http://test.org/myonto.owl4> { 
        SERVICE <https://dbpedia.org/sparql/> {
            ?name dbo:wikiPageWikiLink ?mypeople;
        	rdf:type foaf:Person;
         	rdf:type dbo:Person;
			dbo:birthPlace ?place;
			dbo:birthDate ?date;
   			dbp:occupation ?occupation;
         	dbo:wikiPageLength ?lengthPage.
        OPTIONAL{?name dbp:partner ?partner}.
        OPTIONAL{?name dbp:spouse ?partner}.
        OPTIONAL{?name dbp:relatives ?relative}.
        VALUES (?mypeople) {(foaf:Person)(dbr:Forbes_Celebrity_100)}
            { SELECT ?name (COUNT(?r) as ?wikiLinks)
                WHERE {
                    ?name dbo:wikiPageWikiLink ?r.
                }
             GROUP BY?name
    }
}   
}
} 
"""

'''
Query 2 shows the query that does not make use of the owl:sameAs property and it maps every element from the dbpedia 
to the self-made ontology 


'''

query_2 = """ PREFIX onto: <http://test.org/myonto.owl>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbp: <http://dbpedia.org/property/>

CONSTRUCT { 
        foaf:Person owl:equivalentClass onto:Person.
        dbp:occupation owl:equivalentClass onto:Occupation.
    	dbp:partner owl:equivalentClass onto:Partner.
        dbp:relatives owl:equivalentClass onto:Relative.
        ?name rdf:type onto:Person.  
        ?place rdf:type onto:birthPlace.
        ?date rdf:type onto:birthDate.
        ?occupation rdf:type onto:Occupation.
        ?partner rdf:type onto:Partner.
        ?relative rdf:type onto:Relative.
        ?name onto:birthPlace ?place.
        ?name onto:birthDate ?date.
        ?name onto:hasOccupation ?occupation.
        ?name onto:hasPartner ?partner.
        ?name onto:hasRelative ?relative.
        ?name onto:lengthPage ?lengthPage.
    	?name onto:amountWikiLinks ?wikiLinks.
    	?name onto:ofNationality ?country.
    } 

#SELECT * 
     WHERE { GRAPH <http://test.org/myonto.owl4> { 
        SERVICE <https://dbpedia.org/sparql/> {
            ?name dbo:wikiPageWikiLink ?mypeople;
        	rdf:type foaf:Person;
         	rdf:type dbo:Person;
			dbo:birthPlace ?place;
			dbo:birthDate ?date;
   		#	dbo:gender	?gender;
   			dbp:occupation ?occupation;
         	dbo:wikiPageLength ?lengthPage;
        OPTIONAL{?name dbp:partner ?partner}.
        OPTIONAL{?name dbp:spouse ?partner}.
        OPTIONAL{?name dbp:relatives ?relative}.
        VALUES (?mypeople) {(foaf:Person)(dbr:Forbes_Celebrity_100)}
            { SELECT ?name (COUNT(?r) as ?wikiLinks)
                WHERE {
                    ?name dbo:wikiPageWikiLink ?r.
                }
             GROUP BY?name
    }
}   
}
} """




'''
Query 3 shows the query that makes use of the owl:sameAs property and maps every element from the dbpedia 
to the self-made ontology 


'''
query_3 = """ PREFIX onto: <http://test.org/myonto.owl>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbp: <http://dbpedia.org/property/>

CONSTRUCT { 
        foaf:Person owl:equivalentClass onto:Person.
        dbp:occupation owl:equivalentClass onto:Occupation.
    	dbp:partner owl:equivalentClass onto:Partner.
        dbp:relatives owl:equivalentClass onto:Relative.
        ?name rdf:type onto:Person.  
        ?place rdf:type onto:birthPlace.
        ?date rdf:type onto:birthDate.
        ?occupation rdf:type onto:Occupation.
        ?partner rdf:type onto:Partner.
        ?relative rdf:type onto:Relative.
        ?name onto:birthPlace ?place.
        ?name onto:birthDate ?date.
        ?name onto:hasOccupation ?occupation.
        ?name onto:hasPartner ?partner.
        ?name onto:hasRelative ?relative.
        ?name onto:lengthPage ?lengthPage.
    	?name onto:amountWikiLinks ?wikiLinks.
    	?name onto:ofNationality ?country.
    	?name owl:sameAs ?x
    } 

#SELECT * 
     WHERE { GRAPH <http://test.org/myonto.owl4> { 
        SERVICE <https://dbpedia.org/sparql/> {
            ?name dbo:wikiPageWikiLink ?mypeople;
        	rdf:type foaf:Person;
         	rdf:type dbo:Person;
			dbo:birthPlace ?place;
			dbo:birthDate ?date;
   		#	dbo:gender	?gender;
   			dbp:occupation ?occupation;
         	dbo:wikiPageLength ?lengthPage;
          	owl:sameAs ?x.
        OPTIONAL{?name dbp:partner ?partner}.
        OPTIONAL{?name dbp:spouse ?partner}.
        OPTIONAL{?name dbp:relatives ?relative}.
        VALUES (?mypeople) {(foaf:Person)(dbr:Forbes_Celebrity_100)}
            { SELECT ?name (COUNT(?r) as ?wikiLinks)
                WHERE {
                    ?name dbo:wikiPageWikiLink ?r.
                }
             GROUP BY?name
    }
}   
}
} """
