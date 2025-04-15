
import sys
_b = (((sys.version_info[0] < 3) and (lambda x: x)) or (lambda x: x.encode('latin1')))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(name='SubscribeRequest.proto', package='mvsim_msgs', syntax='proto2', serialized_options=None, serialized_pb=_b('\n\x16SubscribeRequest.proto\x12\nmvsim_msgs":\n\x10SubscribeRequest\x12\r\n\x05topic\x18\x01 \x02(\t\x12\x17\n\x0fupdatesEndpoint\x18\x02 \x02(\t'))
_SUBSCRIBEREQUEST = _descriptor.Descriptor(name='SubscribeRequest', full_name='mvsim_msgs.SubscribeRequest', filename=None, file=DESCRIPTOR, containing_type=None, fields=[_descriptor.FieldDescriptor(name='topic', full_name='mvsim_msgs.SubscribeRequest.topic', index=0, number=1, type=9, cpp_type=9, label=2, has_default_value=False, default_value=_b('').decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR), _descriptor.FieldDescriptor(name='updatesEndpoint', full_name='mvsim_msgs.SubscribeRequest.updatesEndpoint', index=1, number=2, type=9, cpp_type=9, label=2, has_default_value=False, default_value=_b('').decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto2', extension_ranges=[], oneofs=[], serialized_start=38, serialized_end=96)
DESCRIPTOR.message_types_by_name['SubscribeRequest'] = _SUBSCRIBEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), dict(DESCRIPTOR=_SUBSCRIBEREQUEST, __module__='SubscribeRequest_pb2'))
_sym_db.RegisterMessage(SubscribeRequest)
