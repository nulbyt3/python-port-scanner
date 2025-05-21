import socket
import time

# define colors for better output
COLOR_GREEN = '\033[92m' # green color for SUCCESS
COLOR_RED = '\033[91m' # red color for FAIL
COLOR_RESET = '\033[0m' # reset color

def scan_port(target_ip_address, start_port = 0, end_port = 65535):
    ''' ========== Scan ports on target IP address ========== '''
    print(f'Scanning port on {target_ip_address} between {start_port} - {end_port}...')
    
    # defint an array to display open ports
    open_ports = []
    
    # scan ports on given range (by default 0 - 65535)
    for port in range(start_port, end_port + 1):
        # create a new socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   

        try:
            # set timeout to avoid hanging
            server_socket.settimeout(1)
            # attempt to connect to the port
            result = server_socket.connect_ex((target_ip_address, port))
            
            if result == 0:
                print(f'{COLOR_GREEN}Port {port} is OPEN!')
                open_ports.append(port)
            else:
                # giving the clear output during scanning
                status = 'closed'
                print(f'{COLOR_RESET}Port {port}: ', status, end='\r')
        # handle user interrruption
        except KeyboardInterrupt:
            print('\n Scan has been stopped by the user')
            return open_ports
        # handle cases where the hostname cannot be resolver
        except socket.gaierror:
            print(f'{COLOR_RED}Hostname could not be resolved!')
            return []
        # handle general socket errors
        except socket.error:
            print(f'{COLOR_RED}Could not connect to the server')
            return []
        finally:
            server_socket.close()
        
    return open_ports

if __name__ == '__main__':
    # get the user input
    target_ip_address = input('Target IP address: ')
    start_port = input('Start port ( default: 0 ): ')
    end_port = input('End port ( default: 65535 ): ')
    
    # set ports by default or correct use input to integer
    # using 1 and 1024 for most common default scan ranges
    start_port = int(start_port) if start_port else 1
    end_port = int(end_port) if end_port else 65535
    
    # validate user input
    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535 and start_port <= end_port):
        print('Invalid port range:\nPorts must be between 1 and 65535, and start port must be less than or equal to end port.')
    else:
        start_time = time.time()
        # call the scan port function
        open_ports = scan_port(target_ip_address, start_port, end_port)
        end_time = time.time()
        
        # print scan summary
        print('\nScan completed in {:.2f} seconds!'.format(end_time - start_time))
        if open_ports:
            print(f'{COLOR_GREEN}Open ports: {sorted(open_ports)}')
        else:
            print(f'{COLOR_RED}No open ports found in specified ip range.')
            
            
    
