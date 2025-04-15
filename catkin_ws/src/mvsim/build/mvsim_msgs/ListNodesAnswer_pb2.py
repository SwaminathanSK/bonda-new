
import sys
_b = (((sys.version_info[0] < 3) and (lambda x: x)) or (lambda x: x.encode('latin1')))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(name='ListNodesAnswer.proto', package='mvsim_msgs', syntax='proto2', serialized_options=None, serialized_pb=_b('\n\x15ListNodesAnswer.proto\x12\nmvsim_msgs" \n\x0fListNodesAnswer\x12\r\n\x05nodes\x18\x01 \x03(\t'))
_LISTNODESANSWER = _descriptor.Descriptor(name='ListNodesAnswer', full_name='mvsim_msgs.ListNodesAnswer', filename=None, file=DESCRIPTOR, containing_type=None, fields=[_descriptor.FieldDescriptor(name='nodes', full_name='mvsim_msgs.ListNodesAnswer.nodes', index=0, number=1, type=9, cpp_type=9, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto2', extension_ranges=[], oneofs=[], serialized_start=37, serialized_end=69)
DESCRIPTOR.message_types_by_name['ListNodesAnswer'] = _LISTNODESANSWER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
ListNodesAnswer = _reflection.GeneratedProtocolMessageType('ListNodesAnswer', (_message.Message,), dict(DESCRIPTOR=_LISTNODESANSWER, __module__='ListNodesAnswer_pb2'))
_sym_db.RegisterMessage(ListNodesAnswer)
