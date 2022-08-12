version:
	python -m bluecc.bundles.bundles_cli version

note:
    env PYTHONPATH=`pwd`:`pwd`/pb:`pwd`/pb/ents jupyter notebook

ipython:
    env PYTHONPATH=`pwd`:`pwd`/pb ipython

deps:
    pip install grpcio-tools
    pip install slugid

gen_proto file:
    protoc --python_out=./pb  \
                -I{{env_var('PROTOBUF')}}/src \
                -I/opt/app/apiset/entity/src/main/proto \
                -I/opt/app/apiset/proto/src/main/proto \
                -I/opt/app/apiset/mesh/src/main/proto \
                -I/opt/app/apiset/mods/src/main/proto \
                -I/opt/app/apiset/facade/src/main/proto {{file}}
    python -m grpc_tools.protoc --python_out=./pb --grpc_python_out=./pb \
                -I{{env_var('PROTOBUF')}}/src \
                -I/opt/app/apiset/entity/src/main/proto \
                -I/opt/app/apiset/proto/src/main/proto \
                -I/opt/app/apiset/mesh/src/main/proto \
                -I/opt/app/apiset/mods/src/main/proto \
                -I/opt/app/apiset/facade/src/main/proto {{file}}

fund:
    just gen_proto "/opt/app/apiset/proto/src/main/proto/*.proto"

ents:
    just gen_proto "/opt/app/apiset/entity/src/main/proto/*.proto"
    just gen_proto "/opt/app/apiset/entity/src/main/proto/ents/*.proto"

types:
    just gen_proto "/opt/app/apiset/entity/src/main/proto/types/*.proto"

extra:
    just gen_proto "/opt/app/apiset/mesh/src/main/proto/extra/*.proto"

mods:
    just gen_proto "/opt/app/apiset/mods/src/main/proto/extra/*.proto"

allents:
    just ents
    just types
    just extra
    just mods

