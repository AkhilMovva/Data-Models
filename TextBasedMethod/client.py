import socket
import json
HOST = '52.86.83.216'  # The server's hostname or IP address
PORT = 8192        # The port used by the server

def json_message():
    local_ip = socket.gethostbyname(socket.gethostname())
    rfw_id=input("rfw_id: ")
    benchmark_type=input("Enter file to read from DVD-testing, DVD-training, NDBench-training, NDBench-training : ")
    workload_metric=input("Enter which metric you want:")
    batch_unit=int(input("batch_unit: "))
    batch_id=int(input("batch_id: "))
    batch_size=int(input("batch_size: "))
    a_file = open("rfw.json", "r")
    data = json.load(a_file)
    data["rfw_id"] = rfw_id
    data["benchmark_type"] = benchmark_type
    data["workload_metric"] = workload_metric
    data["batch_unit"] = batch_unit
    data["batch_id"] = batch_id
    data["batch_size"] = batch_size

    send_message(json.dumps(data))

    return data
def send_message(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data.encode())
        data = s.recv(2048)
        json_data=json.loads(data)
		
    print(json_data)

json_message()