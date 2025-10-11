#!/bin/bash

uv run python -m grpc_tools.protoc \
  -I=server/src \
  --python_out=server/src \
  --grpc_python_out=server/src \
  --pyi_out=server/src \
  server/src/server/grpc_server/proto/definition.proto