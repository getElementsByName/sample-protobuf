
PROTOPATH_PATH=./proto
PROTOFILE_PATH=./proto/*.proto

DST_DIR=./proto
compile.create_dir:
	mkdir -p $(DST_DIR)

compile.proto: compile.create_dir
	protoc -I=$(PROTOPATH_PATH) --python_out=$(DST_DIR) $(PROTOFILE_PATH)

start:
	python ./main.py