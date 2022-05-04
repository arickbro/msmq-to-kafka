import win32com.client
import os
import json
from kafka import KafkaProducer

queueName="myque"
producer = KafkaProducer(bootstrap_servers='192.168.56.111:29092')

queueInfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
computerName = os.getenv('COMPUTERNAME')
queueInfo.FormatName="direct=os:"+computerName+"\\PRIVATE$\\"+queueName
queue=queueInfo.Open(1,0)

counter = 0
while True:
    msg=queue.Receive()
    message = {
        'computerName': computerName,
        'label': msg.Label,
        'sentTime': int(msg.SentTime) ,
        'arrivedTime': int(msg.ArrivedTime),
        'priority': msg.Priority
    }
    print(message)
    producer.send('foobar', key=json.dumps(message), value=bytes(msg.Body))
    
    if counter >= 1000:
        producer.flush()
        counter =0
    
queue.Close()