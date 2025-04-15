
import sys
_b = (((sys.version_info[0] < 3) and (lambda x: x)) or (lambda x: x.encode('latin1')))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(name='SrvSetControllerTwistAnswer.proto', package='mvsim_msgs', syntax='proto2', serialized_options=None, serialized_pb=_b('\n!SrvSetControllerTwistAnswer.proto\x12\nmvsim_msgs"D\n\x1bSrvSetControllerTwistAnswer\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x14\n\x0cerrorMessage\x18\x02 \x01(\t'))
_SRVSETCONTROLLERTWISTANSWER = _descriptor.Descriptor(name='SrvSetControllerTwistAnswer', full_name='mvsim_msgs.SrvSetControllerTwistAnswer', filename=None, file=DESCRIPTOR, containing_type=None, fields=[_descriptor.FieldDescriptor(name='success', full_name='mvsim_msgs.SrvSetControllerTwistAnswer.success', index=0, number=1, type=8, cpp_type=7, label=2, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR), _descriptor.FieldDescriptor(name='errorMessage', full_name='mvsim_msgs.SrvSetControllerTwistAnswer.errorMessage', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=_b('').decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto2', extension_ranges=[], oneofs=[], serialized_start=49, serialized_end=117)
DESCRIPTOR.message_types_by_name['SrvSetControllerTwistAnswer'] = _SRVSETCONTROLLERTWISTANSWER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
SrvSetControllerTwistAnswer = _reflection.GeneratedProtocolMessageType('SrvSetControllerTwistAnswer', (_message.Message,), dict(DESCRIPTOR=_SRVSETCONTROLLERTWISTANSWER, __module__='SrvSetControllerTwistAnswer_pb2'))
_sym_db.RegisterMessage(SrvSetControllerTwistAnswer)
