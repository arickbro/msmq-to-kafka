import win32com.client
import os
import time


queueInfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
computerName = os.getenv('COMPUTERNAME')
queueInfo.FormatName="direct=os:"+computerName+"\\PRIVATE$\\myque"
queue=queueInfo.Open(2,0)   # Open a ref to queue
msg=win32com.client.Dispatch("MSMQ.MSMQMessage")
i=0
while True: 
    msg.Label="TestMsg "+str(i)
    msg.Body = "The quick brown fox jumps over the lazy dog"
    msg.Send(queue)
    time.sleep(2)
    i=i+1

queue.Close()