import json
import pika
import logging
logging.basicConfig()

#Establish a connection to the broker
creds = pika.PlainCredentials("test","testrabbitmq")
parameter = pika.ConnectionParameters('137.140.3.151', credentials = creds)

connection = pika.BlockingConnection(parameter)

#Obtain a channel
channel = connection.channel()

#Declare an exchange
channel.exchange_declare(exchange='sdn_events',
                         type='topic')

#s = "2014-04-02 12:34:35.123  DEBUG [a.b.c.d.MyClass] this is a message" #Sample of log entry format

#Read from file
with open("C:/Users/ransomer/Downloads/log.txt",'r') as my_file:
    #Read lines from a file by looping over the file object
    for s in my_file:
        sList=s.split(None,4)
        myclass=sList[3][1:-1]
        d = {'date':sList[0],'time':sList[1],'level':sList[2],'class':myclass.split('.')[-1],'message':sList[3]}
        key='.'.join((d['level'],d['class']))
        
        #Convert each dict d element to JSON string
        myDump=json.dumps(d)
        {u'dict_string': [{u'date': u'2014-04-02', u'message': u'this is a message', u'time': u'12:34:35.123', u'class': u'MyClass', u'level': u'DEBUG'}]}
        print myDump
        
        channel.basic_publish('sdn_events',
                              routing_key = key,
                              body = myDump)
                              
        
            
#s = "2014-04-02 12:34:35.123  DEBUG [a.b.c.d.MyClass] this is a message"

# now include json

#'{"ID": [{"date": "2014-04-02", "message": "this is a message", "level": "DEBUG", "class": "MyClass", "time": "12:34:35.123"}]}'






#connection.close()


'''
Created on Apr 10, 2014

@author: Ray
'''
