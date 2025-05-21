This is a simple command-line utility written in Python that allows you to scan a target IP address or hostname for open TCP ports within a specified range. It's a useful tool for basic network reconnaissance, security auditing, or checking the availability of services on a remote host.

*** Features ***

+ Scans a user-defined range of TCP ports.

+ Provides clear output indicating whether a port is OPEN (in green) or closed (in red).

+ Handles common network errors such as unresolvable hostnames or connection issues.

+ Allows for user interruption (Ctrl+C) during the scan.

*** Prerequisites ***
+ Python 3.x installed on your system.

*** How to Use ***
+ Save the script:
+ Save the provided Python code into a file named port_scanner.py (or any .py extension).

Run from the terminal:
+ Open your terminal or command prompt, navigate to the directory where you saved the script, and run it using the python3 command:


python3 port_scanner.py
=

Enter Target and Port Range:
+ The script will then prompt you for the following information:

+ Target IP address: Enter the IP address (e.g., 192.168.1.1) or hostname (e.g., example.com) of the machine you want to scan.

+ Start port (default: 1): Enter the starting port number for your scan. If you leave this blank, it will default to 1.

+ End port (default: 65535): Enter the ending port number for your scan. If you leave this blank, it will default to 65535.

Example Input:

Target IP address: 192.168.1.1
Start port (default: 1): 20
End port (default: 65535): 100
=

*** Output ***
During the scan, you will see real-time updates:

Open Ports: Ports found to be open will be displayed in green on a new line, like this:


Port 22 is OPEN!
Port 80 is OPEN!
=

Closed Ports: Ports found to be closed will be displayed in red, typically overwriting the same line to show progress without cluttering the screen:


Port 23: closed
=

(This line will rapidly change as the scanner moves through closed ports.)

Scan Summary: After the scan completes (or is interrupted), a summary will be displayed, including the total time taken and a sorted list of all identified open ports.


Scan completed in 15.34 seconds!
Open ports: [22, 80, 443]
=

*** Error Handling ***
The script includes basic error handling for:

+ Invalid Port Range: If you enter an invalid port range (e.g., start port > end port, or ports outside 1-65535), it will print an error message in red.

+ Hostname Resolution: If the target hostname cannot be resolved to an IP address, it will notify you.

+ Connection Errors: General network connection errors will be reported.

+ User Interruption: Pressing Ctrl+C will stop the scan gracefully.

Note: Port scanning can be a sensitive activity. Always ensure you have explicit permission to scan any network or host you do not own or manage. Unauthorized port scanning may be illegal or violate terms of service.
