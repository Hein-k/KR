# KR
A repository for our knowledge-base-to-text generation project for the course Knowledge Representation on the Web.

In this repository every step that we took in the creation part of the generated stories can be found. During the whole process we made use of the programming language python in combination with the query language SPARQL, which can be used to express queries across diverse data sources. The steps to repeat the experiment are written down below:

1. The Ontology folder shows the ontology we have written with the help of owlready2. Owlready2 can help manipulating ontologies in python. The owl_ontology.py file have to be runned in order to get the ontolgy in RDF format. This RDF file need to be loaded in GraphDB.
2. After the RDF file is loaded as a graph in GraphDB, the SPARQL queries can be given as input to GraphDB to get instances for out ontology. With the usage of the dbpedia web source these instances where created. The SPARQL queries can be found in the sparql_visual folder in the file sparql_queries.py.
3. In the link_prediction folder the Python notebook in which the link prediction were calculated for the ontology can be found. These predictions among celebrities were stores in the MatchesLink.tsv file and later distributed to generate the stories with the use of the T5 model.
4. In the sparql_visual folder the SPARQL notebook can be found in which visualities with the help of the SPARQL queries where build.
5. The T5 model .... 
