import re
import pika
import json
"""
#Establish a connection to the broker
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='137.140.3.151'))

#Obtain a channel
channel = connection.channel()

#Create an empty list
my_list = []


#Read from file
with open ("/home/ransomer/Downloads/log.txt") as my_file:
    lines = my_file().splitlines()

"""

#declare empty dictionary for storing parsed information
dict={}
#Read from file on Windows
with open ('C:/Users/ransomer/Downloads/log.txt') as my_file:
    
    lines = my_file.read().splitlines()
    #lines = lines.strip() #remove the newline character at the end of each line
    
    

    

    #Parse one string (element) to test how it could be broken down
    #further
    for idx, item in enumerate(lines):
        stuff=lines[idx].split()
        #print 'lines[%d] = %s' % (idx, item)
        #print stuff
print lines[1]    
print len(lines)
    ##print lines.count('...')
    #my_file.close()
re.split(' |]', lines[0])
print lines[0]
json_output=open('C:/Users/ransomer/Downloads/json_output.txt', 'w')
json.dump(stuff,json_output)
#print my_file.read()




#Separate each line even further by space delimiter
with open ('C:/Users/ransomer/Downloads/json_output.txt') as my_json:
    lines = my_json.read().split()
 
json_outputtwo= open('C:/Users/ransomer/Downloads/json_outputtwo.txt', 'w')   
json.dump(lines,json_outputtwo)    




    


"""
#Declare an exchange
channel.exchange_declare(exchange='topic_logs',
                         type='topic')

channel.basic_publish(exchange='topics_logs',
                      routing_key='*.DEBUG.*',
                      body='my_file')

my_file.close()

connection.close()

"""