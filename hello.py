# import os
#
# my_name = os.getenv("MY_NAME", "Gayeeeee")
#
# print("hello,",my_name)




import psutil

def kill_process_using_port(port):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for conn in proc.net_connections(kind='inet'):
                if conn.laddr.port == port:
                    print(f"Killing process {proc.info['name']} with PID {proc.info['pid']} using port {port}")
                    proc.kill()
                    return True
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass
    return False

# Example usage
kill_process_using_port(5000)
