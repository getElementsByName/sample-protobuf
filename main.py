from google.protobuf.wrappers_pb2 import StringValue, Int64Value
from google.protobuf import json_format
from proto.sample_pb2 import Sample

stringValueList = ["s", None, "1", ""]
int64ValueList = [1, None, 0, 1000]


def get_wrapper_string_value_list(value):
    return StringValue(value=value)


def get_wrapper_int64_value_list(value):
    return Int64Value(value=value)


def serialize():
    sample = Sample()
    protobuf_string_list = list(map(lambda item: get_wrapper_string_value_list(item), stringValueList))
    sample.stringValueList.extend(protobuf_string_list)

    protobuf_int_list = list(map(lambda item: get_wrapper_int64_value_list(item), int64ValueList))
    sample.int64ValueList.extend(protobuf_int_list)

    print(f'protobuf_instance: {sample}')

    sample_json = json_format.MessageToJson(
        sample,
        including_default_value_fields=True
    )
    return sample_json



json_value = serialize()
print(f'json: {json_value}')


assert(StringValue(value='a').value is 'a')
assert(StringValue(value=None).value is '')