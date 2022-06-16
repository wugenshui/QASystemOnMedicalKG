# 知识图谱
## 一、人工智能的三个阶段
### 机器智能

- 机器的运算能力
- 大规模集群的处理能力
- GPU的处理能力
### 感知智能

- 深度学习是一种感知智能
- 语音识别，识别一段语音
- 图像识别，识别图像中的动物
- 动物也会有这样的一些感知智能
### 认知智能

- 认知是建立在思考的基础之上，而思考是建立在知识的基础之上
- 必须有知识的基础、有一些常识，才能建立思考，形成一个推理机制
- 不断地积累知识，并进行总结思考改进是人类特有的
## 二、何为知识图谱

- 知识图谱本质上是一种语义网络，将客观的经验沉淀在巨大的知识网络中。
- 以实体或概念为节点，以关系为边，提供了一种从关系的视角来看整个知识网络。
- 直观展示

![Knowledge Mapping.png](https://cdn.nlark.com/yuque/0/2022/png/822031/1654852772581-d6523838-6911-454a-b8c8-74e9f0cbc1f3.png#clientId=u20760895-5347-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=547&id=ucd035d83&margin=%5Bobject%20Object%5D&name=Knowledge%20Mapping.png&originHeight=547&originWidth=880&originalType=binary&ratio=1&rotation=0&showTitle=false&size=295138&status=done&style=none&taskId=ud8f73b1c-1cf8-49e5-999e-b4d1b683ad9&title=&width=880)

   - C罗是足球运动员，足球运动员是运动员的子类 -> C罗是运动员
   - 六度空间理论：最多通过六个人你就能够认识任何一个陌生人
- 参考资料
> [知识图谱关键技术与应用案例](https://blog.csdn.net/valada/article/details/83784719)

## 三、知识图谱的典型应用

- 金融行业应用：风控反欺诈

![image.png](https://cdn.nlark.com/yuque/0/2022/png/822031/1655082869893-f6843342-4639-4474-8f15-472f62704073.png#clientId=ua9b7a73b-222e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=868&id=uc2bbdafb&margin=%5Bobject%20Object%5D&name=image.png&originHeight=868&originWidth=1698&originalType=binary&ratio=1&rotation=0&showTitle=false&size=524190&status=done&style=none&taskId=u802f9dff-fc6f-456b-a552-0b3fe4afd8e&title=&width=1698)

- 个性化推荐

![image.png](https://cdn.nlark.com/yuque/0/2022/png/822031/1655083574570-3fe5e5b5-ec57-4a4b-9fff-11ced271ae3a.png#clientId=ua9b7a73b-222e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=808&id=uc4652ae7&margin=%5Bobject%20Object%5D&name=image.png&originHeight=808&originWidth=1632&originalType=binary&ratio=1&rotation=0&showTitle=false&size=906392&status=done&style=none&taskId=u55661845-f6dd-4fdf-974d-274ad60b509&title=&width=1632)
## 四、如何建立一个知识图谱应用
### Schema定义

- 对知识图谱来进行模式或者 Schema 的定义
- demo 选择的领域为医学领域，因此定义了疾病（Disease）、症状(Symptom)、检查(Check)、食物(Food)、药物(Drug)、生产商(Producer)等节点

![model.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/822031/1654857042228-879842d3-3d2b-49f3-be27-0e4588c0ef5a.jpeg#clientId=u5a1d24af-0568-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=682&id=v2lXp&margin=%5Bobject%20Object%5D&name=model.jpg&originHeight=682&originWidth=907&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52819&status=done&style=none&taskId=uef8c08f8-63bd-4f3e-b7fe-62e45a04851&title=&width=907)
### 知识抽取

- 人工抽取
   - 人工标注、分类
   - 能够抽取并有效利用特征，准确率较高
   - 特点：数据量较多时成本相对较高
- 自动抽取
   - 机器学习，聚类
   - 自然语言处理框架
   - 特点：往往会产生一些脏数据，需要进行多轮清洗
### 知识融合

- 这一步骤最主要的是进行实体对齐，也叫实体归一化
- 比如中华人民共和国、中国和 China，这个三个指的是同一实体，就把它归一化为具有全局唯一标识的实例对象。
### 知识存储

- 知识图谱的关系结构非常的复杂、关系非常的多，这时候比较推荐使用图数据库
   - TiTan 是 Apache 旗下的，支持Linux，提供 Java API，数据量级能达到千亿
   - Graph Engine 是 MIT协议，支持 Windows，提供 C# API，数据量级达到百亿
   - Neo4j 是 GPL协议，支持多个平台，提供多语言API，数据量级达到百亿

![image.png](https://cdn.nlark.com/yuque/0/2022/png/822031/1655091343385-61eb44f2-7f69-4935-9fff-f2ade1982ba0.png#clientId=ua9b7a73b-222e-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=404&id=u213967eb&margin=%5Bobject%20Object%5D&name=image.png&originHeight=404&originWidth=1447&originalType=binary&ratio=1&rotation=0&showTitle=false&size=356816&status=done&style=none&taskId=u1fce2593-becf-47ca-97ad-b3610f7f7bd&title=&width=1447)
### 知识推理/应用
## 五、Neo4j
### 部署
```cypher
# 7474=web浏览器 7687=neo4j数据库
docker run -d --name neo4j --restart=always \
-p 7474:7474 -p 7687:7687 \
-v /usr/local/neo4j/data:/data -v /usr/local/neo4j/logs:/logs \
-v /usr/local/neo4j/conf:/var/lib/neo4j/conf -v /usr/local/neo4j/import:/var/lib/neo4j/import \
-e NEO4J_AUTH=neo4j/1q2w3e4r neo4j

# 启动完成后可以通过7474端口暴露出的neo4j-browser访问数据库
```
### 新增数据
```cypher
// 新增 node
CREATE (student1:Person {sid:'1001', name:'Steven', gender:'M', age:'18'})
CREATE (student2:Person {sid:'1002', name:'Mary', gender:'M', age:'19'})
// 新增 relationship
CREATE (student1)-[:classmate]->(student2)

// 创建唯一约束
CREATE CONSTRAINT ON (n:Movie) ASSERT (n.title) IS UNIQUE

// 创建索引，用于提升插叙性能
CREATE INDEX FOR (m:Movie) ON (m.released)
  
// Cypher load csv：使用csv导入数据
// 将数据改为指定格式后，复制到安装目录下的import文件夹下，使用该语句直接导入即可
LOAD CSV FROM "file:///user.csv" AS line
create (a:person{id:line[0],gender:line[1],age:line[2]})
```
### 查询数据
```cypher
// 查询所有数据
MATCH (n) RETURN n
// 清理所有数据
MATCH (n) detach delete n

// 获得节点对象关系
CALL db.schema.visualization

// 查询单个节点，双击可以查看单层关系
MATCH (tom:Person {name: "Tom Hanks"}) RETURN tom
MATCH(tom:Person) WHERE tom.name = 'Tom Hanks' RETURN tom

// 范围查询
MATCH (nineties:Movie) WHERE nineties.released >= 1990 AND nineties.released < 2000 RETURN nineties.title

// 查询单个属性值
MATCH (people:Person) RETURN people.name LIMIT 10

// 查询节点与关联节点
MATCH (tom:Person {name: "Tom Hanks"})-[:ACTED_IN]->(tomHanksMovies) RETURN tom,tomHanksMovies

// 查询合作过电影的演员
MATCH (tom:Person {name:"Tom Hanks"})-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors) RETURN DISTINCT coActors.name

// 电影有关的所有人与关系
MATCH (people:Person)-[relatedTo]-(:Movie {title: "Cloud Atlas"}) RETURN people.name, Type(relatedTo), relatedTo.roles

// 查询node相关节点与关系
MATCH(n)-[r]->(nn:Disease) where nn.name = '白血病' RETURN n,r
                                                           
// 模糊匹配
MATCH(d:Disease) where d.name =~'.*感冒.*' return d

// 查询与node节点有关联的对象
MATCH (people:Person)-[relatedTo]-(:Movie {title: "Cloud Atlas"}) RETURN people.name, Type(relatedTo), relatedTo.roles

// 多个关联属性查询方式一
MATCH (m:Disease)-[r:has_symptom]->(n:Symptom) where
n.name = '流鼻涕' or n.name = '发烧'
WITH m,COLLECT(DISTINCT n) AS ns WHERE SIZE(ns) = 2
return m

// 多个关联属性查询方式二（最优）
MATCH (d1:Disease)-[:has_symptom]->(:Symptom {name:'流鼻涕'}) WITH d1
MATCH (d2:Disease)-[:has_symptom]->(:Symptom {name:'发烧'}) WHERE d2=d1
RETURN d2

// 多个关联属性查询方式三
WITH ['肌肉酸痛','流鼻涕'] AS sym
MATCH (d:Disease)-[:has_symptom]->(s:Symptom)
where s.name IN sym
with sym, d, count(s) AS matches
where matches = size(sym)
RETURN d

// 最短路径
MATCH p=shortestPath(
(bacon:Person {name:"Kevin Bacon"})-[*]-(meg:Person {name:"Meg Ryan"})
)
RETURN p
```
### 初始化数据
```cypher
CREATE (TheMatrix:Movie {title:'The Matrix', released:1999, tagline:'Welcome to the Real World'})
    CREATE (Keanu:Person {name:'Keanu Reeves', born:1964})
    CREATE (Carrie:Person {name:'Carrie-Anne Moss', born:1967})
    CREATE (Laurence:Person {name:'Laurence Fishburne', born:1961})
    CREATE (Hugo:Person {name:'Hugo Weaving', born:1960})
    CREATE (LillyW:Person {name:'Lilly Wachowski', born:1967})
    CREATE (LanaW:Person {name:'Lana Wachowski', born:1965})
    CREATE (JoelS:Person {name:'Joel Silver', born:1952})
    CREATE
    (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrix),
(Carrie)-[:ACTED_IN {roles:['Trinity']}]->(TheMatrix),
(Laurence)-[:ACTED_IN {roles:['Morpheus']}]->(TheMatrix),
(Hugo)-[:ACTED_IN {roles:['Agent Smith']}]->(TheMatrix),
(LillyW)-[:DIRECTED]->(TheMatrix),
(LanaW)-[:DIRECTED]->(TheMatrix),
(JoelS)-[:PRODUCED]->(TheMatrix)
    
    CREATE (Emil:Person {name:"Emil Eifrem", born:1978})
    CREATE (Emil)-[:ACTED_IN {roles:["Emil"]}]->(TheMatrix)
    
    CREATE (TheMatrixReloaded:Movie {title:'The Matrix Reloaded', released:2003, tagline:'Free your mind'})
    CREATE
    (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrixReloaded),
(Carrie)-[:ACTED_IN {roles:['Trinity']}]->(TheMatrixReloaded),
(Laurence)-[:ACTED_IN {roles:['Morpheus']}]->(TheMatrixReloaded),
(Hugo)-[:ACTED_IN {roles:['Agent Smith']}]->(TheMatrixReloaded),
(LillyW)-[:DIRECTED]->(TheMatrixReloaded),
(LanaW)-[:DIRECTED]->(TheMatrixReloaded),
(JoelS)-[:PRODUCED]->(TheMatrixReloaded)
    
    CREATE (TheMatrixRevolutions:Movie {title:'The Matrix Revolutions', released:2003, tagline:'Everything that has a beginning has an end'})
    CREATE
    (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrixRevolutions),
(Carrie)-[:ACTED_IN {roles:['Trinity']}]->(TheMatrixRevolutions),
(Laurence)-[:ACTED_IN {roles:['Morpheus']}]->(TheMatrixRevolutions),
(Hugo)-[:ACTED_IN {roles:['Agent Smith']}]->(TheMatrixRevolutions),
(LillyW)-[:DIRECTED]->(TheMatrixRevolutions),
(LanaW)-[:DIRECTED]->(TheMatrixRevolutions),
(JoelS)-[:PRODUCED]->(TheMatrixRevolutions)
    
    CREATE (TheDevilsAdvocate:Movie {title:"The Devil's Advocate", released:1997, tagline:'Evil has its winning ways'})
    CREATE (Charlize:Person {name:'Charlize Theron', born:1975})
    CREATE (Al:Person {name:'Al Pacino', born:1940})
    CREATE (Taylor:Person {name:'Taylor Hackford', born:1944})
    CREATE
    (Keanu)-[:ACTED_IN {roles:['Kevin Lomax']}]->(TheDevilsAdvocate),
(Charlize)-[:ACTED_IN {roles:['Mary Ann Lomax']}]->(TheDevilsAdvocate),
(Al)-[:ACTED_IN {roles:['John Milton']}]->(TheDevilsAdvocate),
(Taylor)-[:DIRECTED]->(TheDevilsAdvocate)
    
    CREATE (AFewGoodMen:Movie {title:"A Few Good Men", released:1992, tagline:"In the heart of the nation's capital, in a courthouse of the U.S. government, one man will stop at nothing to keep his honor, and one will stop at nothing to find the truth."})
    CREATE (TomC:Person {name:'Tom Cruise', born:1962})
    CREATE (JackN:Person {name:'Jack Nicholson', born:1937})
    CREATE (DemiM:Person {name:'Demi Moore', born:1962})
    CREATE (KevinB:Person {name:'Kevin Bacon', born:1958})
    CREATE (KieferS:Person {name:'Kiefer Sutherland', born:1966})
    CREATE (NoahW:Person {name:'Noah Wyle', born:1971})
    CREATE (CubaG:Person {name:'Cuba Gooding Jr.', born:1968})
    CREATE (KevinP:Person {name:'Kevin Pollak', born:1957})
    CREATE (JTW:Person {name:'J.T. Walsh', born:1943})
    CREATE (JamesM:Person {name:'James Marshall', born:1967})
    CREATE (ChristopherG:Person {name:'Christopher Guest', born:1948})
    CREATE (RobR:Person {name:'Rob Reiner', born:1947})
    CREATE (AaronS:Person {name:'Aaron Sorkin', born:1961})
    CREATE
    (TomC)-[:ACTED_IN {roles:['Lt. Daniel Kaffee']}]->(AFewGoodMen),
(JackN)-[:ACTED_IN {roles:['Col. Nathan R. Jessup']}]->(AFewGoodMen),
(DemiM)-[:ACTED_IN {roles:['Lt. Cdr. JoAnne Galloway']}]->(AFewGoodMen),
(KevinB)-[:ACTED_IN {roles:['Capt. Jack Ross']}]->(AFewGoodMen),
(KieferS)-[:ACTED_IN {roles:['Lt. Jonathan Kendrick']}]->(AFewGoodMen),
(NoahW)-[:ACTED_IN {roles:['Cpl. Jeffrey Barnes']}]->(AFewGoodMen),
(CubaG)-[:ACTED_IN {roles:['Cpl. Carl Hammaker']}]->(AFewGoodMen),
(KevinP)-[:ACTED_IN {roles:['Lt. Sam Weinberg']}]->(AFewGoodMen),
(JTW)-[:ACTED_IN {roles:['Lt. Col. Matthew Andrew Markinson']}]->(AFewGoodMen),
(JamesM)-[:ACTED_IN {roles:['Pfc. Louden Downey']}]->(AFewGoodMen),
(ChristopherG)-[:ACTED_IN {roles:['Dr. Stone']}]->(AFewGoodMen),
(AaronS)-[:ACTED_IN {roles:['Man in Bar']}]->(AFewGoodMen),
(RobR)-[:DIRECTED]->(AFewGoodMen),
(AaronS)-[:WROTE]->(AFewGoodMen)
    
    CREATE (TopGun:Movie {title:"Top Gun", released:1986, tagline:'I feel the need, the need for speed.'})
    CREATE (KellyM:Person {name:'Kelly McGillis', born:1957})
    CREATE (ValK:Person {name:'Val Kilmer', born:1959})
    CREATE (AnthonyE:Person {name:'Anthony Edwards', born:1962})
    CREATE (TomS:Person {name:'Tom Skerritt', born:1933})
    CREATE (MegR:Person {name:'Meg Ryan', born:1961})
    CREATE (TonyS:Person {name:'Tony Scott', born:1944})
    CREATE (JimC:Person {name:'Jim Cash', born:1941})
    CREATE
    (TomC)-[:ACTED_IN {roles:['Maverick']}]->(TopGun),
(KellyM)-[:ACTED_IN {roles:['Charlie']}]->(TopGun),
(ValK)-[:ACTED_IN {roles:['Iceman']}]->(TopGun),
(AnthonyE)-[:ACTED_IN {roles:['Goose']}]->(TopGun),
(TomS)-[:ACTED_IN {roles:['Viper']}]->(TopGun),
(MegR)-[:ACTED_IN {roles:['Carole']}]->(TopGun),
(TonyS)-[:DIRECTED]->(TopGun),
(JimC)-[:WROTE]->(TopGun)
    
    CREATE (JerryMaguire:Movie {title:'Jerry Maguire', released:2000, tagline:'The rest of his life begins now.'})
    CREATE (ReneeZ:Person {name:'Renee Zellweger', born:1969})
    CREATE (KellyP:Person {name:'Kelly Preston', born:1962})
    CREATE (JerryO:Person {name:"Jerry O'Connell", born:1974})
    CREATE (JayM:Person {name:'Jay Mohr', born:1970})
    CREATE (BonnieH:Person {name:'Bonnie Hunt', born:1961})
    CREATE (ReginaK:Person {name:'Regina King', born:1971})
    CREATE (JonathanL:Person {name:'Jonathan Lipnicki', born:1996})
    CREATE (CameronC:Person {name:'Cameron Crowe', born:1957})
    CREATE
    (TomC)-[:ACTED_IN {roles:['Jerry Maguire']}]->(JerryMaguire),
(CubaG)-[:ACTED_IN {roles:['Rod Tidwell']}]->(JerryMaguire),
(ReneeZ)-[:ACTED_IN {roles:['Dorothy Boyd']}]->(JerryMaguire),
(KellyP)-[:ACTED_IN {roles:['Avery Bishop']}]->(JerryMaguire),
(JerryO)-[:ACTED_IN {roles:['Frank Cushman']}]->(JerryMaguire),
(JayM)-[:ACTED_IN {roles:['Bob Sugar']}]->(JerryMaguire),
(BonnieH)-[:ACTED_IN {roles:['Laurel Boyd']}]->(JerryMaguire),
(ReginaK)-[:ACTED_IN {roles:['Marcee Tidwell']}]->(JerryMaguire),
(JonathanL)-[:ACTED_IN {roles:['Ray Boyd']}]->(JerryMaguire),
(CameronC)-[:DIRECTED]->(JerryMaguire),
(CameronC)-[:PRODUCED]->(JerryMaguire),
(CameronC)-[:WROTE]->(JerryMaguire)
    
    CREATE (StandByMe:Movie {title:"Stand By Me", released:1986, tagline:"For some, it's the last real taste of innocence, and the first real taste of life. But for everyone, it's the time that memories are made of."})
    CREATE (RiverP:Person {name:'River Phoenix', born:1970})
    CREATE (CoreyF:Person {name:'Corey Feldman', born:1971})
    CREATE (WilW:Person {name:'Wil Wheaton', born:1972})
    CREATE (JohnC:Person {name:'John Cusack', born:1966})
    CREATE (MarshallB:Person {name:'Marshall Bell', born:1942})
    CREATE
    (WilW)-[:ACTED_IN {roles:['Gordie Lachance']}]->(StandByMe),
(RiverP)-[:ACTED_IN {roles:['Chris Chambers']}]->(StandByMe),
(JerryO)-[:ACTED_IN {roles:['Vern Tessio']}]->(StandByMe),
(CoreyF)-[:ACTED_IN {roles:['Teddy Duchamp']}]->(StandByMe),
(JohnC)-[:ACTED_IN {roles:['Denny Lachance']}]->(StandByMe),
(KieferS)-[:ACTED_IN {roles:['Ace Merrill']}]->(StandByMe),
(MarshallB)-[:ACTED_IN {roles:['Mr. Lachance']}]->(StandByMe),
(RobR)-[:DIRECTED]->(StandByMe)
    
    CREATE (AsGoodAsItGets:Movie {title:'As Good as It Gets', released:1997, tagline:'A comedy from the heart that goes for the throat.'})
    CREATE (HelenH:Person {name:'Helen Hunt', born:1963})
    CREATE (GregK:Person {name:'Greg Kinnear', born:1963})
    CREATE (JamesB:Person {name:'James L. Brooks', born:1940})
    CREATE
    (JackN)-[:ACTED_IN {roles:['Melvin Udall']}]->(AsGoodAsItGets),
(HelenH)-[:ACTED_IN {roles:['Carol Connelly']}]->(AsGoodAsItGets),
(GregK)-[:ACTED_IN {roles:['Simon Bishop']}]->(AsGoodAsItGets),
(CubaG)-[:ACTED_IN {roles:['Frank Sachs']}]->(AsGoodAsItGets),
(JamesB)-[:DIRECTED]->(AsGoodAsItGets)
    
    CREATE (WhatDreamsMayCome:Movie {title:'What Dreams May Come', released:1998, tagline:'After life there is more. The end is just the beginning.'})
    CREATE (AnnabellaS:Person {name:'Annabella Sciorra', born:1960})
    CREATE (MaxS:Person {name:'Max von Sydow', born:1929})
    CREATE (WernerH:Person {name:'Werner Herzog', born:1942})
    CREATE (Robin:Person {name:'Robin Williams', born:1951})
    CREATE (VincentW:Person {name:'Vincent Ward', born:1956})
    CREATE
    (Robin)-[:ACTED_IN {roles:['Chris Nielsen']}]->(WhatDreamsMayCome),
(CubaG)-[:ACTED_IN {roles:['Albert Lewis']}]->(WhatDreamsMayCome),
(AnnabellaS)-[:ACTED_IN {roles:['Annie Collins-Nielsen']}]->(WhatDreamsMayCome),
(MaxS)-[:ACTED_IN {roles:['The Tracker']}]->(WhatDreamsMayCome),
(WernerH)-[:ACTED_IN {roles:['The Face']}]->(WhatDreamsMayCome),
(VincentW)-[:DIRECTED]->(WhatDreamsMayCome)
    
    CREATE (SnowFallingonCedars:Movie {title:'Snow Falling on Cedars', released:1999, tagline:'First loves last. Forever.'})
    CREATE (EthanH:Person {name:'Ethan Hawke', born:1970})
    CREATE (RickY:Person {name:'Rick Yune', born:1971})
    CREATE (JamesC:Person {name:'James Cromwell', born:1940})
    CREATE (ScottH:Person {name:'Scott Hicks', born:1953})
    CREATE
    (EthanH)-[:ACTED_IN {roles:['Ishmael Chambers']}]->(SnowFallingonCedars),
(RickY)-[:ACTED_IN {roles:['Kazuo Miyamoto']}]->(SnowFallingonCedars),
(MaxS)-[:ACTED_IN {roles:['Nels Gudmundsson']}]->(SnowFallingonCedars),
(JamesC)-[:ACTED_IN {roles:['Judge Fielding']}]->(SnowFallingonCedars),
(ScottH)-[:DIRECTED]->(SnowFallingonCedars)
    
    CREATE (YouveGotMail:Movie {title:"You've Got Mail", released:1998, tagline:'At odds in life... in love on-line.'})
    CREATE (ParkerP:Person {name:'Parker Posey', born:1968})
    CREATE (DaveC:Person {name:'Dave Chappelle', born:1973})
    CREATE (SteveZ:Person {name:'Steve Zahn', born:1967})
    CREATE (TomH:Person {name:'Tom Hanks', born:1956})
    CREATE (NoraE:Person {name:'Nora Ephron', born:1941})
    CREATE
    (TomH)-[:ACTED_IN {roles:['Joe Fox']}]->(YouveGotMail),
(MegR)-[:ACTED_IN {roles:['Kathleen Kelly']}]->(YouveGotMail),
(GregK)-[:ACTED_IN {roles:['Frank Navasky']}]->(YouveGotMail),
(ParkerP)-[:ACTED_IN {roles:['Patricia Eden']}]->(YouveGotMail),
(DaveC)-[:ACTED_IN {roles:['Kevin Jackson']}]->(YouveGotMail),
(SteveZ)-[:ACTED_IN {roles:['George Pappas']}]->(YouveGotMail),
(NoraE)-[:DIRECTED]->(YouveGotMail)
    
    CREATE (SleeplessInSeattle:Movie {title:'Sleepless in Seattle', released:1993, tagline:'What if someone you never met, someone you never saw, someone you never knew was the only someone for you?'})
    CREATE (RitaW:Person {name:'Rita Wilson', born:1956})
    CREATE (BillPull:Person {name:'Bill Pullman', born:1953})
    CREATE (VictorG:Person {name:'Victor Garber', born:1949})
    CREATE (RosieO:Person {name:"Rosie O'Donnell", born:1962})
    CREATE
    (TomH)-[:ACTED_IN {roles:['Sam Baldwin']}]->(SleeplessInSeattle),
(MegR)-[:ACTED_IN {roles:['Annie Reed']}]->(SleeplessInSeattle),
(RitaW)-[:ACTED_IN {roles:['Suzy']}]->(SleeplessInSeattle),
(BillPull)-[:ACTED_IN {roles:['Walter']}]->(SleeplessInSeattle),
(VictorG)-[:ACTED_IN {roles:['Greg']}]->(SleeplessInSeattle),
(RosieO)-[:ACTED_IN {roles:['Becky']}]->(SleeplessInSeattle),
(NoraE)-[:DIRECTED]->(SleeplessInSeattle)
    
    CREATE (JoeVersustheVolcano:Movie {title:'Joe Versus the Volcano', released:1990, tagline:'A story of love, lava and burning desire.'})
    CREATE (JohnS:Person {name:'John Patrick Stanley', born:1950})
    CREATE (Nathan:Person {name:'Nathan Lane', born:1956})
    CREATE
    (TomH)-[:ACTED_IN {roles:['Joe Banks']}]->(JoeVersustheVolcano),
(MegR)-[:ACTED_IN {roles:['DeDe', 'Angelica Graynamore', 'Patricia Graynamore']}]->(JoeVersustheVolcano),
(Nathan)-[:ACTED_IN {roles:['Baw']}]->(JoeVersustheVolcano),
(JohnS)-[:DIRECTED]->(JoeVersustheVolcano)
    
    CREATE (WhenHarryMetSally:Movie {title:'When Harry Met Sally', released:1998, tagline:'Can two friends sleep together and still love each other in the morning?'})
    CREATE (BillyC:Person {name:'Billy Crystal', born:1948})
    CREATE (CarrieF:Person {name:'Carrie Fisher', born:1956})
    CREATE (BrunoK:Person {name:'Bruno Kirby', born:1949})
    CREATE
    (BillyC)-[:ACTED_IN {roles:['Harry Burns']}]->(WhenHarryMetSally),
(MegR)-[:ACTED_IN {roles:['Sally Albright']}]->(WhenHarryMetSally),
(CarrieF)-[:ACTED_IN {roles:['Marie']}]->(WhenHarryMetSally),
(BrunoK)-[:ACTED_IN {roles:['Jess']}]->(WhenHarryMetSally),
(RobR)-[:DIRECTED]->(WhenHarryMetSally),
(RobR)-[:PRODUCED]->(WhenHarryMetSally),
(NoraE)-[:PRODUCED]->(WhenHarryMetSally),
(NoraE)-[:WROTE]->(WhenHarryMetSally)
    
    CREATE (ThatThingYouDo:Movie {title:'That Thing You Do', released:1996, tagline:'In every life there comes a time when that thing you dream becomes that thing you do'})
    CREATE (LivT:Person {name:'Liv Tyler', born:1977})
    CREATE
    (TomH)-[:ACTED_IN {roles:['Mr. White']}]->(ThatThingYouDo),
(LivT)-[:ACTED_IN {roles:['Faye Dolan']}]->(ThatThingYouDo),
(Charlize)-[:ACTED_IN {roles:['Tina']}]->(ThatThingYouDo),
(TomH)-[:DIRECTED]->(ThatThingYouDo)
    
    CREATE (TheReplacements:Movie {title:'The Replacements', released:2000, tagline:'Pain heals, Chicks dig scars... Glory lasts forever'})
    CREATE (Brooke:Person {name:'Brooke Langton', born:1970})
    CREATE (Gene:Person {name:'Gene Hackman', born:1930})
    CREATE (Orlando:Person {name:'Orlando Jones', born:1968})
    CREATE (Howard:Person {name:'Howard Deutch', born:1950})
    CREATE
    (Keanu)-[:ACTED_IN {roles:['Shane Falco']}]->(TheReplacements),
(Brooke)-[:ACTED_IN {roles:['Annabelle Farrell']}]->(TheReplacements),
(Gene)-[:ACTED_IN {roles:['Jimmy McGinty']}]->(TheReplacements),
(Orlando)-[:ACTED_IN {roles:['Clifford Franklin']}]->(TheReplacements),
(Howard)-[:DIRECTED]->(TheReplacements)
    
    CREATE (RescueDawn:Movie {title:'RescueDawn', released:2006, tagline:"Based on the extraordinary true story of one man's fight for freedom"})
    CREATE (ChristianB:Person {name:'Christian Bale', born:1974})
    CREATE (ZachG:Person {name:'Zach Grenier', born:1954})
    CREATE
    (MarshallB)-[:ACTED_IN {roles:['Admiral']}]->(RescueDawn),
(ChristianB)-[:ACTED_IN {roles:['Dieter Dengler']}]->(RescueDawn),
(ZachG)-[:ACTED_IN {roles:['Squad Leader']}]->(RescueDawn),
(SteveZ)-[:ACTED_IN {roles:['Duane']}]->(RescueDawn),
(WernerH)-[:DIRECTED]->(RescueDawn)
    
    CREATE (TheBirdcage:Movie {title:'The Birdcage', released:1996, tagline:'Come as you are'})
    CREATE (MikeN:Person {name:'Mike Nichols', born:1931})
    CREATE
    (Robin)-[:ACTED_IN {roles:['Armand Goldman']}]->(TheBirdcage),
(Nathan)-[:ACTED_IN {roles:['Albert Goldman']}]->(TheBirdcage),
(Gene)-[:ACTED_IN {roles:['Sen. Kevin Keeley']}]->(TheBirdcage),
(MikeN)-[:DIRECTED]->(TheBirdcage)
    
    CREATE (Unforgiven:Movie {title:'Unforgiven', released:1992, tagline:"It's a hell of a thing, killing a man"})
    CREATE (RichardH:Person {name:'Richard Harris', born:1930})
    CREATE (ClintE:Person {name:'Clint Eastwood', born:1930})
    CREATE
    (RichardH)-[:ACTED_IN {roles:['English Bob']}]->(Unforgiven),
(ClintE)-[:ACTED_IN {roles:['Bill Munny']}]->(Unforgiven),
(Gene)-[:ACTED_IN {roles:['Little Bill Daggett']}]->(Unforgiven),
(ClintE)-[:DIRECTED]->(Unforgiven)
    
    CREATE (JohnnyMnemonic:Movie {title:'Johnny Mnemonic', released:1995, tagline:'The hottest data on earth. In the coolest head in town'})
    CREATE (Takeshi:Person {name:'Takeshi Kitano', born:1947})
    CREATE (Dina:Person {name:'Dina Meyer', born:1968})
    CREATE (IceT:Person {name:'Ice-T', born:1958})
    CREATE (RobertL:Person {name:'Robert Longo', born:1953})
    CREATE
    (Keanu)-[:ACTED_IN {roles:['Johnny Mnemonic']}]->(JohnnyMnemonic),
(Takeshi)-[:ACTED_IN {roles:['Takahashi']}]->(JohnnyMnemonic),
(Dina)-[:ACTED_IN {roles:['Jane']}]->(JohnnyMnemonic),
(IceT)-[:ACTED_IN {roles:['J-Bone']}]->(JohnnyMnemonic),
(RobertL)-[:DIRECTED]->(JohnnyMnemonic)
    
    CREATE (CloudAtlas:Movie {title:'Cloud Atlas', released:2012, tagline:'Everything is connected'})
    CREATE (HalleB:Person {name:'Halle Berry', born:1966})
    CREATE (JimB:Person {name:'Jim Broadbent', born:1949})
    CREATE (TomT:Person {name:'Tom Tykwer', born:1965})
    CREATE (DavidMitchell:Person {name:'David Mitchell', born:1969})
    CREATE (StefanArndt:Person {name:'Stefan Arndt', born:1961})
    CREATE
    (TomH)-[:ACTED_IN {roles:['Zachry', 'Dr. Henry Goose', 'Isaac Sachs', 'Dermot Hoggins']}]->(CloudAtlas),
(Hugo)-[:ACTED_IN {roles:['Bill Smoke', 'Haskell Moore', 'Tadeusz Kesselring', 'Nurse Noakes', 'Boardman Mephi', 'Old Georgie']}]->(CloudAtlas),
(HalleB)-[:ACTED_IN {roles:['Luisa Rey', 'Jocasta Ayrs', 'Ovid', 'Meronym']}]->(CloudAtlas),
(JimB)-[:ACTED_IN {roles:['Vyvyan Ayrs', 'Captain Molyneux', 'Timothy Cavendish']}]->(CloudAtlas),
(TomT)-[:DIRECTED]->(CloudAtlas),
(LillyW)-[:DIRECTED]->(CloudAtlas),
(LanaW)-[:DIRECTED]->(CloudAtlas),
(DavidMitchell)-[:WROTE]->(CloudAtlas),
(StefanArndt)-[:PRODUCED]->(CloudAtlas)
    
    CREATE (TheDaVinciCode:Movie {title:'The Da Vinci Code', released:2006, tagline:'Break The Codes'})
    CREATE (IanM:Person {name:'Ian McKellen', born:1939})
    CREATE (AudreyT:Person {name:'Audrey Tautou', born:1976})
    CREATE (PaulB:Person {name:'Paul Bettany', born:1971})
    CREATE (RonH:Person {name:'Ron Howard', born:1954})
    CREATE
    (TomH)-[:ACTED_IN {roles:['Dr. Robert Langdon']}]->(TheDaVinciCode),
(IanM)-[:ACTED_IN {roles:['Sir Leight Teabing']}]->(TheDaVinciCode),
(AudreyT)-[:ACTED_IN {roles:['Sophie Neveu']}]->(TheDaVinciCode),
(PaulB)-[:ACTED_IN {roles:['Silas']}]->(TheDaVinciCode),
(RonH)-[:DIRECTED]->(TheDaVinciCode)
    
    CREATE (VforVendetta:Movie {title:'V for Vendetta', released:2006, tagline:'Freedom! Forever!'})
    CREATE (NatalieP:Person {name:'Natalie Portman', born:1981})
    CREATE (StephenR:Person {name:'Stephen Rea', born:1946})
    CREATE (JohnH:Person {name:'John Hurt', born:1940})
    CREATE (BenM:Person {name: 'Ben Miles', born:1967})
    CREATE
    (Hugo)-[:ACTED_IN {roles:['V']}]->(VforVendetta),
(NatalieP)-[:ACTED_IN {roles:['Evey Hammond']}]->(VforVendetta),
(StephenR)-[:ACTED_IN {roles:['Eric Finch']}]->(VforVendetta),
(JohnH)-[:ACTED_IN {roles:['High Chancellor Adam Sutler']}]->(VforVendetta),
(BenM)-[:ACTED_IN {roles:['Dascomb']}]->(VforVendetta),
(JamesM)-[:DIRECTED]->(VforVendetta),
(LillyW)-[:PRODUCED]->(VforVendetta),
(LanaW)-[:PRODUCED]->(VforVendetta),
(JoelS)-[:PRODUCED]->(VforVendetta),
(LillyW)-[:WROTE]->(VforVendetta),
(LanaW)-[:WROTE]->(VforVendetta)
    
    CREATE (SpeedRacer:Movie {title:'Speed Racer', released:2008, tagline:'Speed has no limits'})
    CREATE (EmileH:Person {name:'Emile Hirsch', born:1985})
    CREATE (JohnG:Person {name:'John Goodman', born:1960})
    CREATE (SusanS:Person {name:'Susan Sarandon', born:1946})
    CREATE (MatthewF:Person {name:'Matthew Fox', born:1966})
    CREATE (ChristinaR:Person {name:'Christina Ricci', born:1980})
    CREATE (Rain:Person {name:'Rain', born:1982})
    CREATE
    (EmileH)-[:ACTED_IN {roles:['Speed Racer']}]->(SpeedRacer),
(JohnG)-[:ACTED_IN {roles:['Pops']}]->(SpeedRacer),
(SusanS)-[:ACTED_IN {roles:['Mom']}]->(SpeedRacer),
(MatthewF)-[:ACTED_IN {roles:['Racer X']}]->(SpeedRacer),
(ChristinaR)-[:ACTED_IN {roles:['Trixie']}]->(SpeedRacer),
(Rain)-[:ACTED_IN {roles:['Taejo Togokahn']}]->(SpeedRacer),
(BenM)-[:ACTED_IN {roles:['Cass Jones']}]->(SpeedRacer),
(LillyW)-[:DIRECTED]->(SpeedRacer),
(LanaW)-[:DIRECTED]->(SpeedRacer),
(LillyW)-[:WROTE]->(SpeedRacer),
(LanaW)-[:WROTE]->(SpeedRacer),
(JoelS)-[:PRODUCED]->(SpeedRacer)
    
    CREATE (NinjaAssassin:Movie {title:'Ninja Assassin', released:2009, tagline:'Prepare to enter a secret world of assassins'})
    CREATE (NaomieH:Person {name:'Naomie Harris'})
    CREATE
    (Rain)-[:ACTED_IN {roles:['Raizo']}]->(NinjaAssassin),
(NaomieH)-[:ACTED_IN {roles:['Mika Coretti']}]->(NinjaAssassin),
(RickY)-[:ACTED_IN {roles:['Takeshi']}]->(NinjaAssassin),
(BenM)-[:ACTED_IN {roles:['Ryan Maslow']}]->(NinjaAssassin),
(JamesM)-[:DIRECTED]->(NinjaAssassin),
(LillyW)-[:PRODUCED]->(NinjaAssassin),
(LanaW)-[:PRODUCED]->(NinjaAssassin),
(JoelS)-[:PRODUCED]->(NinjaAssassin)
    
    CREATE (TheGreenMile:Movie {title:'The Green Mile', released:1999, tagline:"Walk a mile you'll never forget."})
    CREATE (MichaelD:Person {name:'Michael Clarke Duncan', born:1957})
    CREATE (DavidM:Person {name:'David Morse', born:1953})
    CREATE (SamR:Person {name:'Sam Rockwell', born:1968})
    CREATE (GaryS:Person {name:'Gary Sinise', born:1955})
    CREATE (PatriciaC:Person {name:'Patricia Clarkson', born:1959})
    CREATE (FrankD:Person {name:'Frank Darabont', born:1959})
    CREATE
    (TomH)-[:ACTED_IN {roles:['Paul Edgecomb']}]->(TheGreenMile),
(MichaelD)-[:ACTED_IN {roles:['John Coffey']}]->(TheGreenMile),
(DavidM)-[:ACTED_IN {roles:['Brutus "Brutal" Howell']}]->(TheGreenMile),
(BonnieH)-[:ACTED_IN {roles:['Jan Edgecomb']}]->(TheGreenMile),
(JamesC)-[:ACTED_IN {roles:['Warden Hal Moores']}]->(TheGreenMile),
(SamR)-[:ACTED_IN {roles:['"Wild Bill" Wharton']}]->(TheGreenMile),
(GaryS)-[:ACTED_IN {roles:['Burt Hammersmith']}]->(TheGreenMile),
(PatriciaC)-[:ACTED_IN {roles:['Melinda Moores']}]->(TheGreenMile),
(FrankD)-[:DIRECTED]->(TheGreenMile)
    
    CREATE (FrostNixon:Movie {title:'Frost/Nixon', released:2008, tagline:'400 million people were waiting for the truth.'})
    CREATE (FrankL:Person {name:'Frank Langella', born:1938})
    CREATE (MichaelS:Person {name:'Michael Sheen', born:1969})
    CREATE (OliverP:Person {name:'Oliver Platt', born:1960})
    CREATE
    (FrankL)-[:ACTED_IN {roles:['Richard Nixon']}]->(FrostNixon),
(MichaelS)-[:ACTED_IN {roles:['David Frost']}]->(FrostNixon),
(KevinB)-[:ACTED_IN {roles:['Jack Brennan']}]->(FrostNixon),
(OliverP)-[:ACTED_IN {roles:['Bob Zelnick']}]->(FrostNixon),
(SamR)-[:ACTED_IN {roles:['James Reston, Jr.']}]->(FrostNixon),
(RonH)-[:DIRECTED]->(FrostNixon)
    
    CREATE (Hoffa:Movie {title:'Hoffa', released:1992, tagline:"He didn't want law. He wanted justice."})
    CREATE (DannyD:Person {name:'Danny DeVito', born:1944})
    CREATE (JohnR:Person {name:'John C. Reilly', born:1965})
    CREATE
    (JackN)-[:ACTED_IN {roles:['Hoffa']}]->(Hoffa),
(DannyD)-[:ACTED_IN {roles:['Robert "Bobby" Ciaro']}]->(Hoffa),
(JTW)-[:ACTED_IN {roles:['Frank Fitzsimmons']}]->(Hoffa),
(JohnR)-[:ACTED_IN {roles:['Peter "Pete" Connelly']}]->(Hoffa),
(DannyD)-[:DIRECTED]->(Hoffa)
    
    CREATE (Apollo13:Movie {title:'Apollo 13', released:1995, tagline:'Houston, we have a problem.'})
    CREATE (EdH:Person {name:'Ed Harris', born:1950})
    CREATE (BillPax:Person {name:'Bill Paxton', born:1955})
    CREATE
    (TomH)-[:ACTED_IN {roles:['Jim Lovell']}]->(Apollo13),
(KevinB)-[:ACTED_IN {roles:['Jack Swigert']}]->(Apollo13),
(EdH)-[:ACTED_IN {roles:['Gene Kranz']}]->(Apollo13),
(BillPax)-[:ACTED_IN {roles:['Fred Haise']}]->(Apollo13),
(GaryS)-[:ACTED_IN {roles:['Ken Mattingly']}]->(Apollo13),
(RonH)-[:DIRECTED]->(Apollo13)
    
    CREATE (Twister:Movie {title:'Twister', released:1996, tagline:"Don't Breathe. Don't Look Back."})
    CREATE (PhilipH:Person {name:'Philip Seymour Hoffman', born:1967})
    CREATE (JanB:Person {name:'Jan de Bont', born:1943})
    CREATE
    (BillPax)-[:ACTED_IN {roles:['Bill Harding']}]->(Twister),
(HelenH)-[:ACTED_IN {roles:['Dr. Jo Harding']}]->(Twister),
(ZachG)-[:ACTED_IN {roles:['Eddie']}]->(Twister),
(PhilipH)-[:ACTED_IN {roles:['Dustin "Dusty" Davis']}]->(Twister),
(JanB)-[:DIRECTED]->(Twister)
    
    CREATE (CastAway:Movie {title:'Cast Away', released:2000, tagline:'At the edge of the world, his journey begins.'})
    CREATE (RobertZ:Person {name:'Robert Zemeckis', born:1951})
    CREATE
    (TomH)-[:ACTED_IN {roles:['Chuck Noland']}]->(CastAway),
(HelenH)-[:ACTED_IN {roles:['Kelly Frears']}]->(CastAway),
(RobertZ)-[:DIRECTED]->(CastAway)
    
    CREATE (OneFlewOvertheCuckoosNest:Movie {title:"One Flew Over the Cuckoo's Nest", released:1975, tagline:"If he's crazy, what does that make you?"})
    CREATE (MilosF:Person {name:'Milos Forman', born:1932})
    CREATE
    (JackN)-[:ACTED_IN {roles:['Randle McMurphy']}]->(OneFlewOvertheCuckoosNest),
(DannyD)-[:ACTED_IN {roles:['Martini']}]->(OneFlewOvertheCuckoosNest),
(MilosF)-[:DIRECTED]->(OneFlewOvertheCuckoosNest)
    
    CREATE (SomethingsGottaGive:Movie {title:"Something's Gotta Give", released:2003})
    CREATE (DianeK:Person {name:'Diane Keaton', born:1946})
    CREATE (NancyM:Person {name:'Nancy Meyers', born:1949})
    CREATE
    (JackN)-[:ACTED_IN {roles:['Harry Sanborn']}]->(SomethingsGottaGive),
(DianeK)-[:ACTED_IN {roles:['Erica Barry']}]->(SomethingsGottaGive),
(Keanu)-[:ACTED_IN {roles:['Julian Mercer']}]->(SomethingsGottaGive),
(NancyM)-[:DIRECTED]->(SomethingsGottaGive),
(NancyM)-[:PRODUCED]->(SomethingsGottaGive),
(NancyM)-[:WROTE]->(SomethingsGottaGive)
    
    CREATE (BicentennialMan:Movie {title:'Bicentennial Man', released:1999, tagline:"One robot's 200 year journey to become an ordinary man."})
    CREATE (ChrisC:Person {name:'Chris Columbus', born:1958})
    CREATE
    (Robin)-[:ACTED_IN {roles:['Andrew Marin']}]->(BicentennialMan),
(OliverP)-[:ACTED_IN {roles:['Rupert Burns']}]->(BicentennialMan),
(ChrisC)-[:DIRECTED]->(BicentennialMan)
    
    CREATE (CharlieWilsonsWar:Movie {title:"Charlie Wilson's War", released:2007, tagline:"A stiff drink. A little mascara. A lot of nerve. Who said they couldn't bring down the Soviet empire."})
    CREATE (JuliaR:Person {name:'Julia Roberts', born:1967})
    CREATE
    (TomH)-[:ACTED_IN {roles:['Rep. Charlie Wilson']}]->(CharlieWilsonsWar),
(JuliaR)-[:ACTED_IN {roles:['Joanne Herring']}]->(CharlieWilsonsWar),
(PhilipH)-[:ACTED_IN {roles:['Gust Avrakotos']}]->(CharlieWilsonsWar),
(MikeN)-[:DIRECTED]->(CharlieWilsonsWar)
    
    CREATE (ThePolarExpress:Movie {title:'The Polar Express', released:2004, tagline:'This Holiday Season... Believe'})
    CREATE
    (TomH)-[:ACTED_IN {roles:['Hero Boy', 'Father', 'Conductor', 'Hobo', 'Scrooge', 'Santa Claus']}]->(ThePolarExpress),
(RobertZ)-[:DIRECTED]->(ThePolarExpress)
    
    CREATE (ALeagueofTheirOwn:Movie {title:'A League of Their Own', released:1992, tagline:'Once in a lifetime you get a chance to do something different.'})
    CREATE (Madonna:Person {name:'Madonna', born:1954})
    CREATE (GeenaD:Person {name:'Geena Davis', born:1956})
    CREATE (LoriP:Person {name:'Lori Petty', born:1963})
    CREATE (PennyM:Person {name:'Penny Marshall', born:1943})
    CREATE
    (TomH)-[:ACTED_IN {roles:['Jimmy Dugan']}]->(ALeagueofTheirOwn),
(GeenaD)-[:ACTED_IN {roles:['Dottie Hinson']}]->(ALeagueofTheirOwn),
(LoriP)-[:ACTED_IN {roles:['Kit Keller']}]->(ALeagueofTheirOwn),
(RosieO)-[:ACTED_IN {roles:['Doris Murphy']}]->(ALeagueofTheirOwn),
(Madonna)-[:ACTED_IN {roles:['"All the Way" Mae Mordabito']}]->(ALeagueofTheirOwn),
(BillPax)-[:ACTED_IN {roles:['Bob Hinson']}]->(ALeagueofTheirOwn),
(PennyM)-[:DIRECTED]->(ALeagueofTheirOwn)
    
    CREATE (PaulBlythe:Person {name:'Paul Blythe'})
    CREATE (AngelaScope:Person {name:'Angela Scope'})
    CREATE (JessicaThompson:Person {name:'Jessica Thompson'})
    CREATE (JamesThompson:Person {name:'James Thompson'})
    
    CREATE
    (JamesThompson)-[:FOLLOWS]->(JessicaThompson),
(AngelaScope)-[:FOLLOWS]->(JessicaThompson),
(PaulBlythe)-[:FOLLOWS]->(AngelaScope)
    
    CREATE
    (JessicaThompson)-[:REVIEWED {summary:'An amazing journey', rating:95}]->(CloudAtlas),
(JessicaThompson)-[:REVIEWED {summary:'Silly, but fun', rating:65}]->(TheReplacements),
(JamesThompson)-[:REVIEWED {summary:'The coolest football movie ever', rating:100}]->(TheReplacements),
(AngelaScope)-[:REVIEWED {summary:'Pretty funny at times', rating:62}]->(TheReplacements),
(JessicaThompson)-[:REVIEWED {summary:'Dark, but compelling', rating:85}]->(Unforgiven),
(JessicaThompson)-[:REVIEWED {summary:"Slapstick redeemed only by the Robin Williams and Gene Hackman's stellar performances", rating:45}]->(TheBirdcage),
(JessicaThompson)-[:REVIEWED {summary:'A solid romp', rating:68}]->(TheDaVinciCode),
(JamesThompson)-[:REVIEWED {summary:'Fun, but a little far fetched', rating:65}]->(TheDaVinciCode),
(JessicaThompson)-[:REVIEWED {summary:'You had me at Jerry', rating:92}]->(JerryMaguire)
    
    WITH TomH as a
      MATCH (a)-[:ACTED_IN]->(m)<-[:DIRECTED]-(d) RETURN a,m,d LIMIT 10;
```
### 父子节点关联查询
```cypher
# 查询感冒相关疾病
MATCH(d:Disease) where d.name =~'.*感冒.*' return d
MATCH (s1:Symptom) WHERE s1.name='全身酸痛' or s1.name='咳出黄痰' or s1.name='严重咳嗽' or s1.name='外冷内热' return s1;

// 重型风热感冒	全身酸痛	咳出黄痰
// 重型风寒感冒	严重咳嗽  外冷内热 

// 添加节点与关系
MATCH (d:Disease {name:'感冒'}) CREATE (d)-[:subclass]->(d1:Disease { name:'重型风热感冒'});
MATCH (d:Disease {name:'感冒'}) CREATE (d)-[:subclass]->(d2:Disease { name:'重型风寒感冒'});
MATCH (d1:Disease { name:'重型风热感冒'}) CREATE (d1)-[:has_symptom]->(s1:Symptom { name:'全身酸痛'});
MATCH (d1:Disease { name:'重型风热感冒'}) CREATE (d1)-[:has_symptom]->(s2:Symptom { name:'咳出黄痰'});
MATCH (d2:Disease { name:'重型风寒感冒'}) CREATE (d2)-[:has_symptom]->(s3:Symptom { name:'严重咳嗽'});
MATCH (d2:Disease { name:'重型风寒感冒'}) CREATE (d2)-[:has_symptom]->(s4:Symptom { name:'外冷内热'});

MATCH (d1:Disease { name:'重型风寒感冒' }) set d1.cure_way=['对症治疗','支持性治疗']                                                                              
MATCH (d1:Disease { name:'重型风热感冒' }) set d1.cure_way=['对症治疗','中医治疗','支持性治疗']

CREATE CONSTRAINT ON (d:Disease) ASSERT (n.name) IS UNIQUE
CREATE CONSTRAINT ON (n:Symptom) ASSERT (n.name) IS UNIQUE
CREATE INDEX index_dname FOR (n:Disease) ON (n.name);
CREATE INDEX index_sname FOR (n:Symptom) ON (n.name);
                                                      
// 删除节点与关系
MATCH (d1:Disease{name: '重型风热感冒'}) DETACH DELETE d1;
MATCH (d2:Disease{name: '重型风寒感冒'}) DETACH DELETE d2;
MATCH (s1:Symptom) WHERE s1.name='全身酸痛' or s1.name='咳出黄痰' or s1.name='严重咳嗽' or s1.name='外冷内热' DETACH DELETE s1;

# 关联查询（*0..1表示关系不确定，但是会严重影响到查询性能）
MATCH (s0:Symptom)<-[:has_symptom]-(:Disease)-[:subclass*0..1]->(d:Disease)-[r:has_symptom]->(s1:Symptom) 
WHERE s0.name='流鼻涕' OR s1.name='流鼻涕' 
WITH d 
MATCH (s2:Symptom)<-[:has_symptom]-(:Disease)-[:subclass*0..1]->(d:Disease)-[r:has_symptom]->(s3:Symptom)
WHERE s2.name='严重咳嗽' OR s3.name='严重咳嗽'
return  d

# 最终结果
MATCH (s0:Symptom)<-[:has_symptom]-(:Disease)-[:subclass*0..1]->(d:Disease)-[r:has_symptom]->(s1:Symptom) 
WHERE s0.name='流鼻涕' OR s1.name='流鼻涕' 
WITH d 
MATCH (s2:Symptom)<-[:has_symptom]-(:Disease)-[:subclass*0..1]->(d:Disease)-[r:has_symptom]->(s3:Symptom)
WHERE s2.name='严重咳嗽' OR s3.name='严重咳嗽'
WITH d
MATCH (ss2:Symptom)<-[:has_symptom]-(:Disease)-[:subclass]->(d:Disease) 
WHERE  ss2.name <> '流鼻涕' AND ss2.name <> '严重咳嗽' 
return d.name as dname,ss2.name as sname
UNION 
MATCH (s0:Symptom)<-[:has_symptom]-(:Disease)-[:subclass*0..1]->(d:Disease)-[r:has_symptom]->(s1:Symptom) 
WHERE s0.name='流鼻涕' OR s1.name='流鼻涕' 
WITH d 
MATCH (s2:Symptom)<-[:has_symptom]-(:Disease)-[:subclass*0..1]->(d:Disease)-[r:has_symptom]->(s3:Symptom)
WHERE s2.name='严重咳嗽' OR s3.name='严重咳嗽'
WITH d
MATCH (d:Disease)-[r:has_symptom]->(ss1:Symptom) 
WHERE ss1.name <> '流鼻涕' AND ss1.name <> '严重咳嗽' 
RETURN d.name as dname,ss1.name as sname
```

# python-kg 介绍

## 开始步骤

1. 安装依赖
```
pip install py2neo -i https://mirrors.aliyun.com/pypi/simple/
pip install pyahocorasick -i https://pypi.tuna.tsinghua.edu.cn/simple/

```
2. 知识图谱数据导入：python build_medicalgraph.py，导入的数据较多，估计需要几个小时。
`python build_medicalgraph.py`
3. 启动问答模式
`python chatbot_graph.py`

## 项目介绍

知识图谱是目前自然语言处理的一个热门方向。目前知识图谱在各个领域全面开花，如教育、医疗、司法、金融等。本项目立足医药领域，以垂直型医药网站为数据来源，以疾病为核心，构建起一个包含7类规模为4.4万的知识实体，11类规模约30万实体关系的知识图谱。
本项目将包括以下两部分的内容：
1) 基于垂直网站数据的医药知识图谱构建
2) 基于医药知识图谱的自动问答

- 本 demo 基于 https://github.com/liuhuanyong/QASystemOnMedicalKG ，进行了一定程度的改造，仅用于研究用途

# 项目最终效果
话不多少，直接上图。以下两图是实际问答运行过程中的截图：
![image](img/chat1.png)

![image](img/chat2.png)

# 项目运行方式
1、配置要求：要求配置neo4j数据库及相应的python依赖包。neo4j数据库用户名密码记住，并修改相应文件。  
2、知识图谱数据导入：python build_medicalgraph.py，导入的数据较多，估计需要几个小时。  
3、启动问答：python chat_graph.py

# 以下介绍详细方案
# 一、医疗知识图谱构建
# 1.1 业务驱动的知识图谱构建框架
![image](img/kg_route.png)

# 1.2 脚本目录
prepare_data/datasoider.py：网络资讯采集脚本  
prepare_data/datasoider.py：网络资讯采集脚本  
prepare_data/max_cut.py：基于词典的最大向前/向后切分脚本  
build_medicalgraph.py：知识图谱入库脚本    　　

# 1.3 医药领域知识图谱规模
1.3.1 neo4j图数据库存储规模
![image](img/graph_summary.png)

1.3.2 知识图谱实体类型

| 实体类型 | 中文含义 | 实体数量 |举例 |
| :--- | :---: | :---: | :--- |
| Check | 诊断检查项目 | 3,353| 支气管造影;关节镜检查|
| Department | 医疗科目 | 54 |  整形美容科;烧伤科|
| Disease | 疾病 | 8,807 |  血栓闭塞性脉管炎;胸降主动脉动脉瘤|
| Drug | 药品 | 3,828 |  京万红痔疮膏;布林佐胺滴眼液|
| Food | 食物 | 4,870 |  番茄冲菜牛肉丸汤;竹笋炖羊肉|
| Producer | 在售药品 | 17,201 |  通药制药青霉素V钾片;青阳醋酸地塞米松片|
| Symptom | 疾病症状 | 5,998 |  乳腺组织肥厚;脑实质深部出血|
| Total | 总计 | 44,111 | 约4.4万实体量级|


1.3.3 知识图谱实体关系类型

| 实体关系类型 | 中文含义 | 关系数量 | 举例|
| :--- | :---: | :---: | :--- |
| belongs_to | 属于 | 8,844| <妇科,属于,妇产科>|
| common_drug | 疾病常用药品 | 14,649 | <阳强,常用,甲磺酸酚妥拉明分散片>|
| do_eat |疾病宜吃食物 | 22,238| <胸椎骨折,宜吃,黑鱼>|
| drugs_of |  药品在售药品 | 17,315| <青霉素V钾片,在售,通药制药青霉素V钾片>|
| need_check | 疾病所需检查 | 39,422| <单侧肺气肿,所需检查,支气管造影>|
| no_eat | 疾病忌吃食物 | 22,247| <唇病,忌吃,杏仁>|
| recommand_drug | 疾病推荐药品 | 59,467 | <混合痔,推荐用药,京万红痔疮膏>|
| recommand_eat | 疾病推荐食谱 | 40,221 | <鞘膜积液,推荐食谱,番茄冲菜牛肉丸汤>|
| has_symptom | 疾病症状 | 5,998 |  <早期乳腺癌,疾病症状,乳腺组织肥厚>|
| acompany_with | 疾病并发疾病 | 12,029 | <下肢交通静脉瓣膜关闭不全,并发疾病,血栓闭塞性脉管炎>|
| Total | 总计 | 294,149 | 约30万关系量级|

1.3.4 知识图谱属性类型

| 属性类型 | 中文含义 | 举例 |
| :--- | :---: | :---: |
| name | 疾病名称 | 喘息样支气管炎 |
| desc | 疾病简介 | 又称哮喘性支气管炎... |
| cause | 疾病病因 | 常见的有合胞病毒等...|
| prevent | 预防措施 | 注意家族与患儿自身过敏史... |
| cure_lasttime | 治疗周期 | 6-12个月 |
| cure_way | 治疗方式 | "药物治疗","支持性治疗" |
| cured_prob | 治愈概率 | 95% |
| easy_get | 疾病易感人群 | 无特定的人群 |


# 二、基于医疗知识图谱的自动问答
# 2.1 技术架构
![image](img/qa_route.png)

# 2.2 脚本结构
question_classifier.py：问句类型分类脚本  
question_parser.py：问句解析脚本  
chatbot_graph.py：问答程序脚本  

# 2.3　支持问答类型

| 问句类型 | 中文含义 | 问句举例 |
| :--- | :---: | :---: |
| disease_symptom | 疾病症状| 乳腺癌的症状有哪些？ |
| symptom_disease | 已知症状找可能疾病 | 最近老流鼻涕怎么办？ |
| disease_cause | 疾病病因 | 为什么有的人会失眠？|
| disease_acompany | 疾病的并发症 | 失眠有哪些并发症？ |
| disease_not_food | 疾病需要忌口的食物 | 失眠的人不要吃啥？ |
| disease_do_food | 疾病建议吃什么食物 | 耳鸣了吃点啥？ |
| food_not_disease | 什么病最好不要吃某事物 | 哪些人最好不好吃蜂蜜？ |
| food_do_disease | 食物对什么病有好处| 鹅肉有什么好处？ |
| disease_drug | 啥病要吃啥药 | 肝病要吃啥药？ |
| drug_disease | 药品能治啥病 | 板蓝根颗粒能治啥病？ |
| disease_check | 疾病需要做什么检查 | 脑膜炎怎么才能查出来？|
| check_disease |　检查能查什么病 | 全血细胞计数能查出啥来？ |
| disease_prevent | 预防措施| 怎样才能预防肾虚？ |
| disease_lasttime | 治疗周期 | 感冒要多久才能好？ |
| disease_cureway | 治疗方式 | 高血压要怎么治？ |
| disease_cureprob | 治愈概率 | 白血病能治好吗？ |
| disease_easyget | 疾病易感人群 | 什么人容易得高血压？ |
| disease_desc | 疾病描述 | 糖尿病 |

# 问答结果展示

        用户:乳腺癌的症状有哪些？
        小勇: 乳腺癌的症状包括：乳腺癌的远处转移；胸痛；乳头溢液；乳头破碎；肝肿大；泌乳障碍；乳头内陷；乳房肿块；剧痛
        ******************************************************************************************
        用户:最近老流鼻涕怎么办？
        小勇: 症状流鼻涕可能染上的疾病有：枯草热；副流行性感冒；急性上呼吸道感染；硫化氢中毒；小儿衣原体肺炎；风寒感冒；慢性额窦炎；鼻源性头痛；人禽流行性感冒；小儿流行性喘憋性肺炎；病毒性感冒；慢性鼻炎；风热犯肺；感冒；顿呛；小儿急性上呼吸道感染；嗜酸细胞增多性非变态反应性鼻炎；干酪性鼻窦炎；下呼吸道感染；麻疹
        ******************************************************************************************
        用户:为什么有的人会失眠？
        小勇: 失眠可能的成因有：躯体疾病和服用药物可以影响睡眠，如消化不良，头痛，背痛，关节炎，心脏病，糖尿病，哮喘，鼻窦炎，溃疡病，或服用某些影响中枢神经的药物。
        由于生活方式引起睡眠问题也很常见，如饮用咖啡或茶叶，晚间饮酒，睡前进食或晚饭较晚造成满腹食物尚未消化，大量吸烟，睡前剧烈的体力活动，睡前过度的精神活动，夜班工作，白天小睡，上床时间不规律，起床时间不规律。
        可能的原因有压力很大，过度忧虑，紧张或焦虑，悲伤或抑郁，生气，容易出现睡眠问题。
        吵闹的睡眠环境，睡眠环境过于明亮，污染，过度拥挤。
        ******************************************************************************************
        用户:失眠有哪些并发症？
        小勇: 失眠的症状包括：心肾不交；神经性耳鸣；咽鼓管异常开放症；偏执狂；十二指肠胃反流及胆汁反流性胃炎；腋臭；黧黑斑；巨细胞动脉炎；Stargardt病；抑郁症；腔隙性脑梗死；甲状腺功能亢进伴发的精神障碍；紧张性头痛；胃下垂；心血虚；迷路震荡；口腔结核性溃疡；痰饮；游走性结节性脂膜炎；小儿脑震荡
        ******************************************************************************************
        用户:失眠的人不要吃啥？
        小勇: 失眠忌食的食物包括有：油条；河蚌；猪油（板油）；淡菜(鲜)
        ******************************************************************************************
        用户:耳鸣了吃点啥？
        小勇: 耳鸣宜食的食物包括有：南瓜子仁;鸡翅;芝麻;腰果
        推荐食谱包括有：紫菜芙蓉汤;羊肉汤面;油豆腐油菜;紫菜鸡蛋莲草汤;乌药羊肉汤;可乐鸡翅;栗子鸡翅;冬菇油菜心
        ******************************************************************************************
        用户:哪些人最好不好吃蜂蜜？
        小勇: 患有散发性脑炎伴发的精神障碍；情感性心境障碍；蝎螫伤；四肢淋巴水肿；农药中毒所致的精神障碍；肝错构瘤；细菌性肺炎；急性高原病；小儿颅后窝室管膜瘤；柯萨奇病毒疹；眼眶静脉性血管瘤；乙脑伴发的精神障碍；晚期产后出血；吸入性肺炎；腓总神经损伤；铍及其化合物引起的皮肤病；猝死型冠心病；彼得异常；过敏性急性小管间质性肾炎；小儿腹胀的人最好不要吃蜂蜜
        ******************************************************************************************
        用户:鹅肉有什么好处？
        小勇: 患有子宫内膜厚；呼吸疾病；肛肠病；闭经；丧偶后适应性障碍；宫颈外翻；巨球蛋白血症；急性颌下腺炎；锥体外系损害；腺样体炎；咳嗽；错构瘤；牙科病；子宫内膜炎；闭锁综合征；结膜炎；恶性淋巴瘤；足外翻；神经炎；病理性近视的人建议多试试鹅肉
        ******************************************************************************************
        用户:肝病要吃啥药？
        小勇: 肝病宜食的食物包括有：鹅肉;鸡肉;鸡肝;鸡腿
        推荐食谱包括有：小米红糖粥;小米蛋奶粥;扁豆小米粥;黄豆小米粥;人参小米粥;小米粉粥;鲜菇小米粥;芝麻小米粥
        肝病通常的使用的药品包括：恩替卡韦分散片；维生素C片；二十五味松石丸；拉米夫定胶囊；阿德福韦酯片
        ******************************************************************************************
        用户:板蓝根颗粒能治啥病？
        小勇: 板蓝根颗粒主治的疾病有流行性腮腺炎；喉痹；喉炎；咽部异感症；急性单纯性咽炎；腮腺隙感染；过敏性咽炎；咽囊炎；急性鼻咽炎；喉水肿；慢性化脓性腮腺炎；慢性咽炎；急性喉炎；咽异感症；鼻咽炎；锁喉痈；小儿咽喉炎；喉返神经损伤；化脓性腮腺炎；喉血管瘤,可以试试
        ******************************************************************************************
        用户:脑膜炎怎么才能查出来？
        小勇: 脑膜炎通常可以通过以下方式检查出来：脑脊液钠；尿常规；Fisher手指试验；颈项强直；脑脊液细菌培养；尿谷氨酰胺；脑脊液钾；脑脊液天门冬氨酸氨基转移酶；脑脊液病原体检查；硝酸盐还原试验
        ******************************************************************************************
        用户:怎样才能预防肾虚？
        小勇: 肾虚可能的成因有：1、多因房劳过度，或少年频繁手淫。2、思虑忧郁，损伤心脾，则病及阳明冲脉。3、恐惧伤肾，恐则伤肾。4、肝主筋，阴器为宗筋之汇，若情志不遂，忧思郁怒，肝失疏泄条达，则宗筋所聚无能。5、湿热下注，宗筋弛纵。
        肾虚是肾脏精气阴阳不足所产生的诸如精神疲乏、头晕耳鸣、健忘脱发、腰脊酸痛、遗精阳痿、男子不育、女子不孕、更年期综合征等多种病证的一个综合概念。关于肾虚形成的原因，可归结为两个方面，一为先天禀赋不足，二为后天因素引起。
        从引起肾虚的先天因素来看，首先是先天禀赋薄弱。《灵枢.寿天刚柔》篇说：“人之生也，有刚有柔，有弱有强。”由于父母体弱多病，精血亏虚时怀孕;或酒后房事怀孕;或年过五十精气力量大减之时怀孕;或男女双方年龄不够，身体发育不完全结婚，也就是早婚时怀孕，或生育过多，精血过度耗损;或妊娠期中失于调养，胎气不足等等都可导致肾的精气亏虚成为肾虚证形成的重要原因;其次，如果肾藏精功能失常就会导致性功能异常，生殖功能下降，影响生殖能力，便会引起下一代形体虚衰，或先天畸形、痴呆、缺陷、男子出现精少不育、早泄，女子出现闭经不孕、小产、习惯性流产等等。
        肾虚的预防措施包括：肾虚日常预防
        在预防方面，因起病与恣情纵欲有关的，应清心寡欲，戒除手淫;如与全身衰弱、营养不良或身心过劳有关的，应适当增加营养或注意劳逸结合，节制性欲。
        1、性生活要适度，不勉强，不放纵。
        2、饮食方面：无力疲乏时多吃含铁、蛋白质的食物，如木耳、大枣、乌鸡等;消化不良者多喝酸奶，吃山楂;平日护肾要多吃韭菜、海参、人参、乌鸡、家鸽等。
        3、经常进行腰部活动，这些运动可以健运命门，补肾纳气。还可多做一些刺激脚心的按摩，中医认为，脚心的涌泉穴是浊气下降的地方，经常按摩涌泉穴，可益精补肾、强身健体、防止早衰，并能舒肝明目，清喉定心，促进睡眠，增进食欲。
        4、充足的睡眠也是恢复精气神的重要保障，工作再紧张，家里的烦心事再多，到了该睡觉的时候也要按时休息。
        健康教育
        1、过度苦寒、冰凉的食物易伤肾，如芦荟、苦瓜、雪糕、鹅肉、啤酒进食过多都伤肾，应该多食黑色素含量高和温补性中药如黑米黑豆等。
        2、男性接触过多的洗涤剂也伤肾，家庭应少用洗涤剂清洗餐具及蔬果，以免洗涤剂残留物被过多摄入。
        3、适当运动可延缓衰老，但强度不宜太大，应选能力所及的运动项目，以促进血液循环，可改善血淤、气损等情况。散步、慢跑、快步走，或在鹅卵石上赤足适当行走，都会促进血液循环，对肾虚有辅助治疗作用。
        4、保持良好的作息习惯，尽量避免熬夜。
        5、积极参加户外运动，放松心情。
        6、不要给自己太大的压力，学会合理减压。
        ******************************************************************************************
        用户:感冒要多久才能好？
        小勇: 感冒治疗可能持续的周期为：7-14天
        ******************************************************************************************
        用户:高血压要怎么治？
        小勇: 高血压可以尝试如下治疗：药物治疗;手术治疗;支持性治疗
        ******************************************************************************************
        用户:白血病能治好吗？
        小勇: 白血病治愈的概率为（仅供参考）：50%-70%
        ******************************************************************************************
        用户:什么人容易得高血压？
        小勇: 高血压的易感人群包括：有高血压家族史，不良的生活习惯，缺乏运动的人群
        ******************************************************************************************
        用户:糖尿病
        小勇: 糖尿病,熟悉一下：糖尿病是一种比较常见的内分泌代谢性疾病。该病发病原因主要是由于胰岛素分泌不足，以及胰升高血糖素不适当地分泌过多所引起。多见于40岁以上喜食甜食而肥胖的病人，城市多于农村，常有家族史，故与遗传有关。少数病人与病毒感染和自身免疫反应有关。主要表现为烦渴、多饮、多尿、多食、乏力、消瘦等症状。生命的常见病，伴发高血压、冠心病、高脂血症等，严重时危及生命。
        中医学认为，肝主疏泄，关系人体接收机的升降与调畅，肝气郁滞则气机升降输布紊乱，肝失疏泄则血糖等精微物质不能随清阳之气输布于周身而郁滞于血中，出现高血糖或精微物质的输布紊乱，反见血糖升高，进一步导致血脂、蛋白等其它精微物质紊乱，引起其他合并症，治疗以疏肝调气为主，顺肝条达之性以恢复其生理功能，肝气条达，气机调畅，精微得以输布，糖被利用而血糖自然下降。
        另外，因糖尿病的发生和饮食有关，饮食控制的好坏直接影响着治疗的效果。再就是配合运动，注意调摄情志，再适当的配合中药治疗会取得良好的治疗效果。 
        ******************************************************************************************
        用户:全血细胞计数能查出啥来
        小勇: 通常可以通过全血细胞计数检查出来的疾病有成人类风湿性关节炎性巩膜炎；外阴-阴道-牙龈综合征；电击伤；老年收缩期高血压；小儿肝硬化；异常血红蛋白病；痴呆综合征；高血压病伴发的精神障碍；睾丸淋巴瘤；叶酸缺乏所致贫血；眼球内炎；不稳定血红蛋白病；类癌综合征；老年痴呆；急性淋巴管炎；宫颈妊娠；蚕食性角膜溃疡；低增生性急性白血病；交感性眼炎；原发性免疫缺陷病

# 总结
１、本项目完成了从无到有，以垂直网站为数据来源，构建起以疾病为中心的医疗知识图谱，实体规模4.4万，实体关系规模30万。并基于此，搭建起了一个可以回答18类问题的自动问答小系统。其中，数据采集与整理1天，知识图谱构建与入库0.5天，问答系统组件1.5天。总的来说，还是比较快速。      
2、本项目以业务驱动，构建医疗知识图谱，知识schema设计基于所采集的结构化数据生成(对网页结构化数据进行xpath解析)。    
3、本项目以neo4j作为存储，并基于传统规则的方式完成了知识问答，并最终以cypher查询语句作为问答搜索sql，支持了问答服务。  
4、本项目可以快速部署，数据已经放在data/medical.json当中，本项目的数据，如侵犯相关单位权益，请联系我删除。本数据请勿商用，以免引起不必要的纠纷。在本项目中的部署上，可以遵循项目运行步骤，完成数据库搭建，并提供搜索服务。  
5、本项目还有不足：关于疾病的起因、预防等，实际返回的是一大段文字，这里其实可以引入事件抽取的概念，进一步将原因结构化表示出来。这个可以后面进行尝试。    






