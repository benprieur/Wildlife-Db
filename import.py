from SPARQLWrapper import SPARQLWrapper, JSON
from wikidata import WIKIDATA_REQUEST1
from config import *
from urllib.error import HTTPError
from tables import *
from database import *

# Wikidata request
endpoint_url = "https://query.wikidata.org/sparql"
def get_results(endpoint_url, query):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    try:
        result = sparql.query().convert()
        print (result)
        return result
    except HTTPError as err:
        print(err.code)

wikidata_request_send = WIKIDATA_REQUEST1
results = get_results(endpoint_url, wikidata_request_send)

listIdsSPECIES = []
listResults = []
results = get_results(endpoint_url, wikidata_request_send)
results = results["results"]["bindings"]
for result in results:

    id = result["citesid"]["value"]
    print(id)
    if id not in listIdsSPECIES:
        listIdsSPECIES.append(id)
        listResults.append(result)

# MySQL
cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)
cursor = cnx.cursor()
db = Database(cursor)
db.remove_database(DATABASE)
db.create_database(DATABASE)
db.use_database(DATABASE)
db.create_tables(TABLES, cnx)

ligne = 0
for res in listResults:

    nom = ''
    wikidataid = ''
    image = ''
    nomscientifique = ''
    rangtaxinomique = ''
    taxonsuperieur = ''
    citesid = ''

    try:
        nom = res['itemLabel']['value']
        print (nom)
    except:
        nom = ''
        print("Erreur - nom")

    try:
        wikidataid = res['item']['value']
        print (wikidataid)
        wikidataid = wikidataid.replace('http://www.wikidata.org/entity/', '')
    except:
        wikidataid = ''
        print("Erreur - wikidataid")

    try:
        image = res['image']['value']
        print (image)
    except:
        image = ''
        print("Erreur - image")

    try:
        nomscientifique = res['nomscientifique']['value']
        print (nomscientifique)
    except:
        nomscientifique = ''
        print("Erreur - nomscientifique")

    try:
        rangtaxinomique = res['rangtaxinomiqueLabel']['value']
        print (rangtaxinomique)
    except:
        rangtaxinomique = ''
        print("Erreur - rangtaxinomique")

    try:
        rangtaxinomique = res['rangtaxinomiqueLabel']['value']
        print (rangtaxinomique)
    except:
        rangtaxinomique = ''
        print("Erreur - rangtaxinomique")

    try:
        citesid = res['citesid']['value']
        print (citesid)
    except:
        citesid = ''
        print("Erreur - citesid")

    try:
        cursor.execute("INSERT INTO MAINTABLE (nom, wikidataid, image, nomscientifique, rangtaxinomique, taxonsuperieur, citesid) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nom, wikidataid, image, nomscientifique, rangtaxinomique, taxonsuperieur, citesid))
        cnx.commit()
        ligne = ligne + 1
        print("Row " + str(ligne))
    except:

        print("Erreur - INSERT")