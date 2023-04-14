from neo4j import GraphDatabase
from my_project.neo4j_config import NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD

class Neo4jHelper:
    def __init__(self):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

    def close(self):
        self.driver.close()

    def run_query(self, query, parameters=None):
        with self.driver.session() as session:
            return session.run(query, parameters)
