import locus_message_pb2
import locus_message_pb2_grpc

import grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = locus_message_pb2_grpc.LocusMessagerStub(channel)
        response = stub.SendLocus(locus_message_pb2.Locus(id="AN1234"))
    print(response.status)


if __name__ == "__main__":
    run()
