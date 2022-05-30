from asyncore import write
from pyspectator.processor import Cpu
from datetime import datetime
import csv
import sys

def conf_env():
    #creamos el fichero csv
    f = open("temp.csv","w")

    #escribimos la cabecera del fichero 
    csv.writer(f).writerow([0,'temp', 'time'])

    #cerramo el fichero 
    f.close()

def read_temp():
    
    exit=int(open("temp.csv" , "r").readlines()[-1].split(",")[0])
    if int(exit) < 130000:
        f = open("temp.csv","a",newline='')
        csv.writer(f).writerow([exit+1,f'{Cpu(monitoring_latency=1).temperature}°C', datetime.now().strftime('%H:%M')])
    else:
        f = open("temp.csv","w")
        csv.writer(f).writerow([f'{Cpu(monitoring_latency=1).temperature}°C', datetime.now().strftime('%H:%M')])
    f.close()

def main():
    args = sys.argv[1:]
    print (args)
    if not args:
        conf_env()
    elif args[0] == 'start':
        read_temp()
    
if __name__ == "__main__":
    main()
