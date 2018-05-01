import nmap

def write_to_file(host,result):
    name = "%s.txt"%(host)
    file = open(name,'w')
    file.write(result)
    file.close()
for host in hosts:
        nm.scan(host,'21-1000')
        res = "Host : %s" %host + '\n' + "State : %s" %nm[host].state() + '\n'+ "info : %s" %nm.scaninfo()
        write_to_file(host,res)

def port_scanner():
    file = open('hosts.txt','r')
    hosts = file.read()
    hosts = hosts.split('\n')

    nm =  nmap.PortScanner()
    
def main():
    port_scanner()

main()
