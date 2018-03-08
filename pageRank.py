import os
import operator
def loop():
	print "running"
	for node in source:
		keys_list=[]
		temp=0.0
		flag=0
		flag1=0
		for link in source[node]:
			keys_list = [k for k, v in source.items() if link in v]
		for key in keys_list:
				flag=1
				temp=temp+(1.0-0.85/len(set(total_nodes))*1.0)+(0.85*(page_rank[key]/len(source[key])))
		if temp!=0.0:
			page_rank[node]=temp
		else:
			page_rank[node]=intial_pagerank
		#print page_rank[node],intial_pagerank

f=open("sample-large.txt",'r')
Text=f.read()
lines= Text.split("\n")
source={}
page_rank={}
total_nodes=[]
for line in lines:
	 nodes=line.split("\t")
	 for node in nodes:
	 	total_nodes.append(node)
	 temp=[]
	 for i in range(1,len(nodes)):
	 	temp.append(nodes[i])
	 if nodes[0]!='':
	 	source[nodes[0]]=temp
intial_pagerank=1.0/len(set(total_nodes))*1.0
for node in set(total_nodes):
	page_rank[node]=intial_pagerank

for x in range(60):
	loop()
page_rank= sorted(page_rank.items(), key=operator.itemgetter(1),reverse=True)
for i in range(len(page_rank)):
	print str(page_rank[i][0])+"  "+str(page_rank[i][1])

f = open("pageRank.txt","w")
f.write(str(page_rank))
f.close()
print 'Writing finished!!'
