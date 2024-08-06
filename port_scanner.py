import asyncio
import socket

print(r"""______            _     _  ______                 _           _ 
 ____  ____  ____  _____    ____  ____  ____  _      _      _____ ____    ____ ___  _   _      ____  _     _____ _  __
/  __\/  _ \/  __\/__ __\  / ___\/   _\/  _ \/ \  /|/ \  /|/  __//  __\  /  _ \\  \//  / \__/|/  _ \/ \   /  __// |/ /
|  \/|| / \||  \/|  / \    |    \|  /  | / \|| |\ ||| |\ |||  \  |  \/|  | | // \  /   | |\/||| / \|| |   |  \  |   / 
|  __/| \_/||    /  | |    \___ ||  \_ | |-||| | \||| | \|||  /_ |    /  | |_\\ / /    | |  ||| |-||| |_/\|  /_ |   \ 
\_/   \____/\_/\_\  \_/    \____/\____/\_/ \|\_/  \|\_/  \|\____\\_/\_\  \____//_/     \_/  \|\_/ \|\____/\____\\_|\_\
                                                                                                                    
                                                                                                                     """)
print("\n****************************************************************")
print("\n* Copyright of Malek, 2024                              *")
print("\n* https://x.com/FrankZane95                                  *")
print("\n* https://www.youtube.com/@duawp                          *")
print("\n****************************************************************")

async def scan_port(ip, port):
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        writer.close()
        await writer.wait_closed()
        return port
    except:
        return None

async def scan_ports(ip, start_port, end_port):
    open_ports = []
    tasks = [scan_port(ip, port) for port in range(start_port, end_port + 1)]
    for result in await asyncio.gather(*tasks):
        if result is not None:
            open_ports.append(result)
    return open_ports

def main():
    target_ip = input("What is your target IP? : ")
    port_range = input("Enter port range (e.g., 1-1024) or press Enter for default: ")
    
    try:
        if port_range:
            start_port, end_port = map(int, port_range.split('-'))
        else:
            start_port, end_port = 1, 1024

        loop = asyncio.get_event_loop()
        open_ports = loop.run_until_complete(scan_ports(target_ip, start_port, end_port))
        
        if open_ports:
            print(f"Open ports on {target_ip}: {', '.join(map(str, open_ports))}")
        else:
            print(f"No open ports found on {target_ip}.")
    
    except ValueError:
        print("Invalid port range. Please enter in the format 'start-end' (e.g., '20-80').")
    except KeyboardInterrupt:
        print("\nScan interrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

print("Press Enter to exit...")
input()
