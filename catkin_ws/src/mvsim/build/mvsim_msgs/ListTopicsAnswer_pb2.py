
import sys
_b = (((sys.version_info[0] < 3) and (lambda x: x)) or (lambda x: x.encode('latin1')))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import TopicInfo_pb2 as TopicInfo__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='ListTopicsAnswer.proto', package='mvsim_msgs', syntax='proto2', serialized_options=None, serialized_pb=_b('\n\x16ListTopicsAnswer.proto\x12\nmvsim_msgs\x1a\x0fTopicInfo.proto"9\n\x10ListTopicsAnswer\x12%\n\x06topics\x18\x01 \x03(\x0b2\x15.mvsim_msgs.TopicInfo'), dependencies=[TopicInfo__pb2.DESCRIPTOR])
_LISTTOPICSANSWER = _descriptor.Descriptor(name='ListTopicsAnswer', full_name='mvsim_msgs.ListTopicsAnswer', filename=None, file=DESCRIPTOR, containing_type=None, fields=[_descriptor.FieldDescriptor(name='topics', full_name='mvsim_msgs.ListTopicsAnswer.topics', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto2', extension_ranges=[], oneofs=[], serialized_start=55, serialized_end=112)
_LISTTOPICSANSWER.fields_by_name['topics'].message_type = TopicInfo__pb2._TOPICINFO
DESCRIPTOR.message_types_by_name['ListTopicsAnswer'] = _LISTTOPICSANSWER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
ListTopicsAnswer = _reflection.GeneratedProtocolMessageType('ListTopicsAnswer', (_message.Message,), dict(DESCRIPTOR=_LISTTOPICSANSWER, __module__='ListTopicsAnswer_pb2'))
_sym_db.RegisterMessage(ListTopicsAnswer)
