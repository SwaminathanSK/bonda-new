
import sys
_b = (((sys.version_info[0] < 3) and (lambda x: x)) or (lambda x: x.encode('latin1')))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(name='SrvShutdownAnswer.proto', package='mvsim_msgs', syntax='proto2', serialized_options=None, serialized_pb=_b('\n\x17SrvShutdownAnswer.proto\x12\nmvsim_msgs"%\n\x11SrvShutdownAnswer\x12\x10\n\x08accepted\x18\x01 \x02(\x08'))
_SRVSHUTDOWNANSWER = _descriptor.Descriptor(name='SrvShutdownAnswer', full_name='mvsim_msgs.SrvShutdownAnswer', filename=None, file=DESCRIPTOR, containing_type=None, fields=[_descriptor.FieldDescriptor(name='accepted', full_name='mvsim_msgs.SrvShutdownAnswer.accepted', index=0, number=1, type=8, cpp_type=7, label=2, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto2', extension_ranges=[], oneofs=[], serialized_start=39, serialized_end=76)
DESCRIPTOR.message_types_by_name['SrvShutdownAnswer'] = _SRVSHUTDOWNANSWER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
SrvShutdownAnswer = _reflection.GeneratedProtocolMessageType('SrvShutdownAnswer', (_message.Message,), dict(DESCRIPTOR=_SRVSHUTDOWNANSWER, __module__='SrvShutdownAnswer_pb2'))
_sym_db.RegisterMessage(SrvShutdownAnswer)
