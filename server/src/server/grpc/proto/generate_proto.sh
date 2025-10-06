#!/bin/bash

uv run python -m grpc_tools.protoc -Iserver/src/server/grpc/proto --python_out=server/src/server/grpc/proto --pyi_out=server/src/server/grpc/proto --grpc_python_out=server/src/server/grpc/proto server/src/server/grpc/proto/definition.proto