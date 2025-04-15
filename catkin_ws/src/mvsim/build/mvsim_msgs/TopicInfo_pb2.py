
import sys
_b = (((sys.version_info[0] < 3) and (lambda x: x)) or (lambda x: x.encode('latin1')))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor.FileDescriptor(name='TopicInfo.proto', package='mvsim_msgs', syntax='proto2', serialized_options=None, serialized_pb=_b('\n\x0fTopicInfo.proto\x12\nmvsim_msgs"c\n\tTopicInfo\x12\x11\n\ttopicName\x18\x01 \x02(\t\x12\x11\n\ttopicType\x18\x02 \x02(\t\x12\x19\n\x11publisherEndpoint\x18\x03 \x03(\t\x12\x15\n\rpublisherName\x18\x04 \x03(\t'))
_TOPICINFO = _descriptor.Descriptor(name='TopicInfo', full_name='mvsim_msgs.TopicInfo', filename=None, file=DESCRIPTOR, containing_type=None, fields=[_descriptor.FieldDescriptor(name='topicName', full_name='mvsim_msgs.TopicInfo.topicName', index=0, number=1, type=9, cpp_type=9, label=2, has_default_value=False, default_value=_b('').decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR), _descriptor.FieldDescriptor(name='topicType', full_name='mvsim_msgs.TopicInfo.topicType', index=1, number=2, type=9, cpp_type=9, label=2, has_default_value=False, default_value=_b('').decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR), _descriptor.FieldDescriptor(name='publisherEndpoint', full_name='mvsim_msgs.TopicInfo.publisherEndpoint', index=2, number=3, type=9, cpp_type=9, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR), _descriptor.FieldDescriptor(name='publisherName', full_name='mvsim_msgs.TopicInfo.publisherName', index=3, number=4, type=9, cpp_type=9, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto2', extension_ranges=[], oneofs=[], serialized_start=31, serialized_end=130)
DESCRIPTOR.message_types_by_name['TopicInfo'] = _TOPICINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
TopicInfo = _reflection.GeneratedProtocolMessageType('TopicInfo', (_message.Message,), dict(DESCRIPTOR=_TOPICINFO, __module__='TopicInfo_pb2'))
_sym_db.RegisterMessage(TopicInfo)
