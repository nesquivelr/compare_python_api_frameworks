from concurrent import futures

import locus_message_pb2
import locus_message_pb2_grpc

import grpc


class LocusMessagerServicer(locus_message_pb2_grpc.LocusMessagerServicer):
    def SendLocus(self, request, context):
        print(request.id)
        return locus_message_pb2.FilterExecution(status=True)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    locus_message_pb2_grpc.add_LocusMessagerServicer_to_server(
        LocusMessagerServicer(), server
    )
    server.add_insecure_port("[::]:" + port)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
