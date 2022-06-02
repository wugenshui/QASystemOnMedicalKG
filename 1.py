from py2neo import Graph

entities = ['发烧', '流鼻涕']

query = ["MATCH (m:Disease)-[r:has_symptom]->(n:Symptom) where" + "or".join(" n.name = '{0}' ".format(i) for i in entities) + " WITH m,COLLECT(DISTINCT n) AS ns WHERE SIZE(ns) = "+ str(len(entities)) +" return m"]
print(query)

g = Graph('http://192.168.0.222:7474/', auth=("neo4j", "1q2w3e4r"))
data = g.run(query[0]).data()
print(data[0]['m'])
print(data[0]['m']['name'])
print(data[0]['m']['cause'])

print([i['m']['name'] for i in data])

# MATCH (m:Disease)-[r:has_symptom]->(n:Symptom) 
# where n.name = '流鼻涕' or n.name = '发热伴寒战' or n.name='浑身忽冷忽热'
# WITH m,COLLECT(DISTINCT n) AS ns
# WHERE SIZE(ns) = 3
# return m