# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:18:07 2020

@author: akhilmovva
"""

import grpc
import json
from concurrent import futures
import time
import requestResponse_pb2_grpc as pb2_grpc
import requestResponse_pb2 as pb2
import pandas as pd

class requestResponseService(pb2_grpc.requestResponseServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        
        rfw_ID=request.rfwID
        benchmark_type =request.benchmarkType
        workload_metric=request.workloadMetric
        batch_unit=request.batchUnit
        batch_id=request.batchID
        batch_size=request.batchSize
        
        last_batch_id=batch_id-1+batch_size
        
                    
        dat=[]
                   
        for i in range(batch_id,(last_batch_id+1)):
            data1=pd.read_csv("https://raw.githubusercontent.com/haniehalipour/Online-Machine-Learning-for-Cloud-Resource-Provisioning-of-Microservice-Backend-Systems/master/Workload%20Data/"+benchmark_type+".csv")
            data2=pd.DataFrame(data1[workload_metric])
            dam=data2.iloc[i*batch_unit:(i+1)*batch_unit]
            print(dam)
            dam=str(dam)
            dat.append(dam)
            i+=1
            batch_id+=1
        
        result = {'rfwID': rfw_ID,'lastbatchID': last_batch_id,'samples' : dat}
        
        return pb2.MessageResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_requestResponseServicer_to_server(requestResponseService(),server)
    server.add_insecure_port('localhost:8192')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
