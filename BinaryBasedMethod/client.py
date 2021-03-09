# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:18:33 2020

@author: yaswa
"""

import grpc
import requestResponse_pb2_grpc as pb2_grpc
import requestResponse_pb2 as pb2


class requestResponseClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 8192

        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        self.stub = pb2_grpc.requestResponseStub(self.channel)

    def get_url(self, message):
        
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    client = requestResponseClient()
    rfw_id=int(input("rfw_id: "))
    benchmark_type=input("Enter file to read from DVD-testing, DVD-training, NDBench-training, NDBench-training : ")
    workload_metric=input("Enter which metric you want:")
    batch_unit=int(input("batch_unit: "))
    batch_id=int(input("batch_id: "))
    batch_size=int(input("batch_size: "))
    message = pb2.Message(
        rfwID=rfw_id,
		benchmarkType =benchmark_type,
		workloadMetric=workload_metric,
		batchUnit=batch_unit,
		batchID=batch_id,
		batchSize=batch_size
           )
    result = client.get_url(message)
    print(f'{result}')
