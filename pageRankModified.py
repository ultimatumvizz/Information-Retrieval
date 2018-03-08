def calculate_pr(inb):
    pages = len(inb)
    pr_initial = 1.0/(pages)
    pagerank = 0.0
    damping_factor = 0.85
    sum = 0.0
    for i in range(1,len(inb)):
    	if inb[i] != 0:
        	sum += (pr_initial/inb[i])
    pagerank = float((1-damping_factor)/pages) + (damping_factor * sum)
    return pagerank
f = open("modi.txt",'r')
#f=open("bachan.txt",'r')
Text=f.read()
print Text[1:len(Text)-2].split(",")
inb = [ int(num) for num in Text[1:len(Text)-2].split(",")]
print inb
print calculate_pr(inb)
