In this module I prepare the information in yago 3.1 for ingestion into neo4j. 
I use the NSMNTX plugin written by Jesús Barrasa (https://github.com/neo4j-labs/neosemantics)
I am currently using Neosemantics Release 3.5.0.4 for Neo4j 3.5.x

1. python - A pycharm project that includes 2 files :
	
	1. BOM.py - finds all the lines in a ttl file that are not valid for neo4j and writes them to a file.
	2. COMMENT_LINES.py - comments out all the lines in the file genrated by BOM.py.
