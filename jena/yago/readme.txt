In this module I prepare the information in yago 3.1 for ingestion into jena. 


1. scripts - a directory that contains two scripts :
			1. A sed script sed.txt (Either download sed for windows or use ubuntu on windows). It comments out all of the lines that contain the // string. I ran this script first otherwise the whole process would take forever.
            2. A powershell script run.ps1 that uses a combination of the riot command line and sed. Using the riot command it finds all problematic lines and then using sed it comments each line inline. If I had to run it again i would not use sed -i for every line I had to comment, instead i would write all lines to a file and then comment all lines using COMMENT_LINE.py (https://github.com/ycallen/spot/blob/master/neo4j/yago/python/COMMENT_LINES.py).			
			

