import twitter
import ast
import yaml
import numpy as np
t_key = '984322021-XlOk3E6cLn2q8JbuPiv2qzdqxrgA42UD3Z0pnm1x'
t_secret = 'X7TA3lDKp96z2fg1Bxm2UiNeKTdUDYmIZEW6F4AqsB5b1'
c_key = 'QjLzZQnARCxxBECVIL2H0mBx7'
c_secret = 'dfCfLSaSaz64wPGIMs6qb8wnHiQYkZRnMot0WvmeUpIjkVBxtu'

'''
Calculate pagerank
pr(i) = 1-d/N + d(sum(pr(j)/in(j))) (j!=i)
'''

def calculate_pr(inb):
    pages = len(inb)
    pr_initial = 1.0/(pages)
    #pagerank = 0.0
    damping_factor = 0.85
    sum = 0.0
    for i in range(1,len(inbound_link_array)):
        sum += (pr_initial/inbound_link_array[i])
    pagerank = float((1-damping_factor)/pages) + (damping_factor * sum)
    return pagerank


api=twitter.Api(consumer_key=c_key, consumer_secret= c_secret, access_token_key= t_key, access_token_secret= t_secret)
dick = {}
#dick = api.VerifyCredentials()
dick = api.GetFollowers(screen_name='akshaykumar',count = 150, skip_status = True, total_count = 100)
inbound_link_array = []
inbound_link_array.append(len(dick))
for i in range(len(dick)):
    temp = str(dick[i])
    temp = yaml.load(temp)
    if 'followers_count' in temp:
        inbound_link_array.append(temp['followers_count'])
    else:
        inbound_link_array.append(0)
#print inbound_link_array
print len(inbound_link_array)
f = open("followers.txt","w")
f.write(str(inbound_link_array))
f.close()
print 'Writing finished!!'

#print calculate_pr(inbound_link_array)