from __future__ import unicode_literals

import redis


# fill in the following.
# HOST = "redis-11363.c1.asia-northeast1-1.gce.cloud.redislabs.com"
HOST = "redis-15505.c51.ap-southeast-2-1.ec2.cloud.redislabs.com"
# PWD = "1nOA0St0I7p9pQqu8HkQ18XqDfnoPeoL"
PWD = "6sWrOl7eJKwFiWW6SMO844tgkTZIhcYa"
PORT = "15505" 

redis1 = redis.Redis(host = HOST, password = PWD, port = PORT)

while True:
    msg = input("Please enter your query (type 'quit' or 'exit' to end):").strip()
    if msg == 'quit' or msg == 'exit':
        break
    if msg == '':
        continue
    print("You have entered " + msg, end=' ') 

   
    # Add your code here



    print('for X times')
