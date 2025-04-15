
import sys
_b = (((sys.version_info[0] < 3) and (lambda x: x)) or (lambda x: x.encode('latin1')))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import Pose_pb2 as Pose__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='TimeStampedPose.proto', package='mvsim_msgs', syntax='proto2', serialized_options=None, serialized_pb=_b('\n\x15TimeStampedPose.proto\x12\nmvsim_msgs\x1a\nPose.proto"v\n\x0fTimeStampedPose\x12\x15\n\runixTimestamp\x18\x01 \x02(\x01\x12\x10\n\x08objectId\x18\x02 \x02(\t\x12\x1a\n\x12relativeToObjectId\x18\x04 \x01(\t\x12\x1e\n\x04pose\x18\x03 \x02(\x0b2\x10.mvsim_msgs.Pose'), dependencies=[Pose__pb2.DESCRIPTOR])
_TIMESTAMPEDPOSE = _descriptor.Descriptor(name='TimeStampedPose', full_name='mvsim_msgs.TimeStampedPose', filename=None, file=DESCRIPTOR, containing_type=None, fields=[_descriptor.FieldDescriptor(name='unixTimestamp', full_name='mvsim_msgs.TimeStampedPose.unixTimestamp', index=0, number=1, type=1, cpp_type=5, label=2, has_default_value=False, default_value=float(0), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR), _descriptor.FieldDescriptor(name='objectId', full_name='mvsim_msgs.TimeStampedPose.objectId', index=1, number=2, type=9, cpp_type=9, label=2, has_default_value=False, default_value=_b('').decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR), _descriptor.FieldDescriptor(name='relativeToObjectId', full_name='mvsim_msgs.TimeStampedPose.relativeToObjectId', index=2, number=4, type=9, cpp_type=9, label=1, has_default_value=False, default_value=_b('').decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR), _descriptor.FieldDescriptor(name='pose', full_name='mvsim_msgs.TimeStampedPose.pose', index=3, number=3, type=11, cpp_type=10, label=2, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto2', extension_ranges=[], oneofs=[], serialized_start=49, serialized_end=167)
_TIMESTAMPEDPOSE.fields_by_name['pose'].message_type = Pose__pb2._POSE
DESCRIPTOR.message_types_by_name['TimeStampedPose'] = _TIMESTAMPEDPOSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
TimeStampedPose = _reflection.GeneratedProtocolMessageType('TimeStampedPose', (_message.Message,), dict(DESCRIPTOR=_TIMESTAMPEDPOSE, __module__='TimeStampedPose_pb2'))
_sym_db.RegisterMessage(TimeStampedPose)
