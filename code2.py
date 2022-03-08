import yaml
import time
from datetime import datetime
import threading
import logging
logging.basicConfig(filename='code2.log', level=logging.INFO)
file=open("Milestone1\Milestone1B.yaml")
data = yaml.load(file, Loader=yaml.FullLoader)
#print(data)
out=open("Milestone1\log1B.txt",'w')

def fun(key,val,a1,s1,x1):
        temp=s1
        if x1=="":
            if s1=="":
                logging.info(' thread without x1 and without s1')
                out.write(str(datetime.now())+";"+a1+"." +key+" Entry"+"\n")
                if val["Type"]=="Task":
                    if val["Function"]=="TimeFunction":
                        out.write(str(datetime.now())+";" +a1+"." +key +" Executing " + val["Function"]+ " (" + key+"_Input" + ", " + val["Inputs"]["ExecutionTime"]+")"+"\n")
                        time.sleep(int(val["Inputs"]["ExecutionTime"]))
                        #out.write(str(datetime.now())+";"+key+" Exit"+"\n")
                if val["Type"]=="Flow":
                    if val["Execution"]=="Sequential":
                        seq(val["Activities"],a1,key)
                    elif val["Execution"]=="Concurrent":
                        con(val["Activities"],a1,temp,key)
                out.write(str(datetime.now())+";"+a1+"." +key+" Exit"+"\n")

            else:    
                logging.info(' thread without x1 and with s1')
                
                out.write(str(datetime.now())+";"+a1+"."+s1+"." +key+" Entry"+"\n")
                if val["Type"]=="Task":
                    if val["Function"]=="TimeFunction":
                        out.write(str(datetime.now())+";" +a1+"."+s1+"." +key +" Executing " + val["Function"]+ " (" + key+"_Input" + ", " + val["Inputs"]["ExecutionTime"]+")"+"\n")
                        time.sleep(int(val["Inputs"]["ExecutionTime"]))
                        #out.write(str(datetime.now())+";"+key+" Exit"+"\n")
                if val["Type"]=="Flow":
                    if val["Execution"]=="Sequential":
                        seq(val["Activities"],a1,key)
                    elif val["Execution"]=="Concurrent":
                        con(val["Activities"],a1,temp,key)
                out.write(str(datetime.now())+";"+a1+"."+s1+"." +key+" Exit"+"\n")
        else:
            if s1=="":
                out.write(str(datetime.now())+";"+a1+"." +key+" Entry"+"\n")
                if val["Type"]=="Task":
                    if val["Function"]=="TimeFunction":
                        out.write(str(datetime.now())+";" +a1+"." +temp+"."+key +" Executing " + val["Function"]+ " (" + key+"_Input" + ", " + val["Inputs"]["ExecutionTime"]+")"+"\n")
                        time.sleep(int(val["Inputs"]["ExecutionTime"]))
                        #out.write(str(datetime.now())+";"+key+" Exit"+"\n")
                if val["Type"]=="Flow":
                    if val["Execution"]=="Sequential":
                        seq(val["Activities"],a1,key)
                    elif val["Execution"]=="Concurrent":
                        con(val["Activities"],a1,temp,key)
                out.write(str(datetime.now())+";"+a1+"."+s1+"." +temp+"."+key+" Exit"+"\n")

            else:    
                out.write(str(datetime.now())+";"+a1+"."+s1+"." +key+" Entry"+"\n")
                if val["Type"]=="Task":
                    if val["Function"]=="TimeFunction":
                        out.write(str(datetime.now())+";" +a1+"." +temp+"."+key +" Executing " + val["Function"]+ " (" + key+"_Input" + ", " + val["Inputs"]["ExecutionTime"]+")"+"\n")
                        time.sleep(int(val["Inputs"]["ExecutionTime"]))
                        #out.write(str(datetime.now())+";"+key+" Exit"+"\n")
                if val["Type"]=="Flow":
                    if val["Execution"]=="Sequential":
                        seq(val["Activities"],a1,key)
                    elif val["Execution"]=="Concurrent":
                        con(val["Activities"],a1,temp,key)
                out.write(str(datetime.now())+";"+a1+"."+s1+"." +temp+"."+key+" Exit"+"\n")

def con(dic,a1,s1,x1):
    th=len(dic)
    threads =[]
    for key,val in dic.items():
        t1=threading.Thread(target=fun, args=[key,val,a1,s1,x1])
        t1.start()
        logging.info('subtask thread')
        threads.append(t1)

    for thr in threads:
        thr.join()
        logging.info('main thread')

def seq(dic,a1,s1):
    temp=s1
    for key,val in dic.items():
        if s1=="":
            out.write(str(datetime.now())+";"+a1+"." +key+" Entry"+"\n")
            if val["Type"]=="Task":
                if val["Function"]=="TimeFunction":
                    out.write(str(datetime.now())+";" +a1+"." +key +" Executing " + val["Function"]+ " (" + key+"_Input" + ", " + val["Inputs"]["ExecutionTime"]+")"+"\n")
                    time.sleep(int(val["Inputs"]["ExecutionTime"]))
                    #out.write(str(datetime.now())+";"+key+" Exit"+"\n")
            if val["Type"]=="Flow":
                if val["Execution"]=="Sequential":
                    seq(val["Activities"],a1,key)
                elif val["Execution"]=="Concurrent":
                    con(val["Activities"],a1,temp,key)
            out.write(str(datetime.now())+";"+a1+"." +key+" Exit"+"\n")

        else:    
            out.write(str(datetime.now())+";"+a1+"."+s1+"." +key+" Entry"+"\n")
            if val["Type"]=="Task":
                if val["Function"]=="TimeFunction":
                    out.write(str(datetime.now())+";" +a1+"."+s1+"." +key +" Executing " + val["Function"]+ " (" + key+"_Input" + ", " + val["Inputs"]["ExecutionTime"]+")"+"\n")
                    time.sleep(int(val["Inputs"]["ExecutionTime"]))
                    #out.write(str(datetime.now())+";"+key+" Exit"+"\n")
            if val["Type"]=="Flow":
                if val["Execution"]=="Sequential":
                    seq(val["Activities"],a1,key)
                elif val["Execution"]=="Concurrent":
                    con(val["Activities"],a1,temp,key)
            out.write(str(datetime.now())+";"+a1+"."+s1+"." +key+" Exit"+"\n")

for key,val in data.items():
    s1=""
    x1=""
    out.write(str(datetime.now())+";"+key+" Entry"+"\n")
    if val["Type"]=="Flow":
        if val["Execution"]=="Sequential":
            seq(val['Activities'],key,s1)
        elif val["Execution"]=="Concurrent":
            con(val["Activities"],key,s1,x1)
    out.write(str(datetime.now())+";"+key+" Exit"+"\n")
out.close()
print("exit")