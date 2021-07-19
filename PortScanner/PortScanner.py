import nmap

begin =""
end  = ""

while True:
    ran = input("Port Range....")
    while True:
    ran = input("Port Range....")
    if "-" in ran:
        begin,end = ran.split("-")
        if int(begin) > 0 and int(end) <= 65535  :
            break
        else:
            print("Port range should be between 1-65535")
    else:
        print("!!!Format error!!!")
        print("Range format should be like: '1-9000' ")


target = input("Target IP........")
   
scanner = nmap.PortScanner()
scanner.scan(target, ran, arguments="-sV") 

close = int(end) - int(begin) + 1

for host in scanner.all_hosts():
    print('Host is  %s' % scanner[host].state())

for proto in scanner[host].all_protocols():
    lport = scanner[host][proto].keys()
    close = close - len(lport)
    print(f"Not shown: {close} closed ports")
    print('Port\tState\tServices')
    for port in lport:
        print(str(port)+"/",proto,"Open","\t" ,scanner[host][proto][port]['name'])

