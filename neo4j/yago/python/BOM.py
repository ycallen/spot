from neo4j import GraphDatabase
import sys
import os
import time
from datetime import datetime

# input arguments to program
# 1. path to the ttl file : e.g. C:\yago\manipulation\neo4j\yagoTypes.ttl
# 2. path to output directory to generate file with all non valid lines : e.g. C:\yago\manipulation\neo4j\
# 3. url of bolt service externalized by neo4j : e.g. bolt://localhost:11017


cypher_neosemantics = 'UNWIND  $payload as rdf_fragment  \
      CALL semantics.importRDFSnippet(rdf_fragment,"Turtle")  \
      YIELD terminationStatus, triplesLoaded, triplesParsed, extraInfo \
      RETURN terminationStatus, triplesLoaded as totalLoaded, triplesParsed as totalParsed '

batch_size = 50000

uri = sys.argv[3]

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
ttl_file_name = os.path.basename(sys.argv[1])
base = os.path.splitext(ttl_file_name)[0]
output_file_name = sys.argv[2] + base + current_time.replace(":", "_") + ".txt"

print(sys.argv)
print(current_time + " : started program")
open(output_file_name, "w")
def load_batch(tx, batch, cnt):
    not_ok = []
    for cnt2, record in enumerate(tx.run(cypher_neosemantics, payload=batch)):
        if record["terminationStatus"]=="KO":
                not_ok.append(str(cnt - batch_size + cnt2 + 2))
    if len(not_ok):
        with open(output_file_name, "a") as file:
            file.write('\n')
            file.write('\n'.join(not_ok))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time + " : batch " + str(cnt))

driver = GraphDatabase.driver(uri, auth=("neo4j", "123456"))
with driver.session() as session:
    batch = []
    success = 0
    failure = 0
    with open(sys.argv[1],encoding='utf-8') as file:
        for cnt, line in enumerate(file):
            #if cnt > 43699999:
                batch.append(line)
                if len(batch) == batch_size:
                    try:
                        session.write_transaction(load_batch, batch, cnt)
                    except:
                        print("Unexpected error:", sys.exc_info()[0])
                    batch = []
    session.read_transaction(load_batch, batch, cnt)
driver.close()
