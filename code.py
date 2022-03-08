import yaml
import time
from datetime import datetime

file=open("Milestone1\Milestone1A.yaml")
data = yaml.load(file, Loader=yaml.FullLoader)
out=open("Milestone1\log.txt",'w')
def seq(dic,a1,s1):
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
            out.write(str(datetime.now())+";"+a1+"."+s1+"." +key+" Exit"+"\n")
                        
for key,val in data.items():
    s1=""
    out.write(str(datetime.now())+";"+key+" Entry"+"\n")
    if val["Type"]=="Flow":
        if val["Execution"]=="Sequential":
            seq(val['Activities'],key,s1)
    out.write(str(datetime.now())+";"+key+" Exit"+"\n")
out.close()
print("exit")