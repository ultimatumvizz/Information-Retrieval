import twitter
import yaml

t_key = '984322021-XlOk3E6cLn2q8JbuPiv2qzdqxrgA42UD3Z0pnm1x'
t_secret = 'X7TA3lDKp96z2fg1Bxm2UiNeKTdUDYmIZEW6F4AqsB5b1'
c_key = 'QjLzZQnARCxxBECVIL2H0mBx7'
c_secret = 'dfCfLSaSaz64wPGIMs6qb8wnHiQYkZRnMot0WvmeUpIjkVBxtu'

api=twitter.Api(consumer_key=c_key, consumer_secret= c_secret, access_token_key= t_key, access_token_secret= t_secret)
dick = {}
#dick = api.VerifyCredentials()
dick = api.GetFollowers(screen_name='narendramodi', skip_status = True, total_count = 3000)
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
