# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AdvertiseTopicRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AdvertiseTopicRequest.proto',
  package='mvsim_msgs',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1b\x41\x64vertiseTopicRequest.proto\x12\nmvsim_msgs\"e\n\x15\x41\x64vertiseTopicRequest\x12\x11\n\ttopicName\x18\x01 \x02(\t\x12\x15\n\rtopicTypeName\x18\x02 \x02(\t\x12\x10\n\x08\x65ndpoint\x18\x03 \x02(\t\x12\x10\n\x08nodeName\x18\x04 \x02(\t')
)




_ADVERTISETOPICREQUEST = _descriptor.Descriptor(
  name='AdvertiseTopicRequest',
  full_name='mvsim_msgs.AdvertiseTopicRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topicName', full_name='mvsim_msgs.AdvertiseTopicRequest.topicName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topicTypeName', full_name='mvsim_msgs.AdvertiseTopicRequest.topicTypeName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='mvsim_msgs.AdvertiseTopicRequest.endpoint', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodeName', full_name='mvsim_msgs.AdvertiseTopicRequest.nodeName', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=144,
)

DESCRIPTOR.message_types_by_name['AdvertiseTopicRequest'] = _ADVERTISETOPICREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdvertiseTopicRequest = _reflection.GeneratedProtocolMessageType('AdvertiseTopicRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADVERTISETOPICREQUEST,
  __module__ = 'AdvertiseTopicRequest_pb2'
  # @@protoc_insertion_point(class_scope:mvsim_msgs.AdvertiseTopicRequest)
  ))
_sym_db.RegisterMessage(AdvertiseTopicRequest)


# @@protoc_insertion_point(module_scope)
