# Data-Models
client - server implementation to serve a “workload query” scenario

a client - server implementation to serve a “workload query” scenario. We implemented a data communication model between the client and server through two methods, namely text-based (de)-serialization using JSON and binary (de)-serialization using protocol buffers for the workload data related to industrial benchmarks, NDBench from Netflix and Dell DVD store from Dell. GRPC framework has been used to work with protocol buffers.The server programs implemented for both the methods are successfully hosted on an Amazon EC2 instance.
