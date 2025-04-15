
import sys
_b = (((sys.version_info[0] < 3) and (lambda x: x)) or (lambda x: x.encode('latin1')))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from . import Pose_pb2 as Pose__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='SrvSetPoseAnswer.proto', package='mvsim_msgs', syntax='proto2', serialized_options=None, serialized_pb=_b('\n\x16SrvSetPoseAnswer.proto\x12\nmvsim_msgs\x1a\nPose.proto"\x82\x01\n\x10SrvSetPoseAnswer\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x14\n\x0cerrorMessage\x18\x02 \x01(\t\x12\x1b\n\x13objectIsInCollision\x18\x04 \x02(\x08\x12*\n\x10objectGlobalPose\x18\x05 \x01(\x0b2\x10.mvsim_msgs.Pose'), dependencies=[Pose__pb2.DESCRIPTOR])
_SRVSETPOSEANSWER = _descriptor.Descriptor(name='SrvSetPoseAnswer', full_name='mvsim_msgs.SrvSetPoseAnswer', filename=None, file=DESCRIPTOR, containing_type=None, fields=[_descriptor.FieldDescriptor(name='success', full_name='mvsim_msgs.SrvSetPoseAnswer.success', index=0, number=1, type=8, cpp_type=7, label=2, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR), _descriptor.FieldDescriptor(name='errorMessage', full_name='mvsim_msgs.SrvSetPoseAnswer.errorMessage', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=_b('').decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR), _descriptor.FieldDescriptor(name='objectIsInCollision', full_name='mvsim_msgs.SrvSetPoseAnswer.objectIsInCollision', index=2, number=4, type=8, cpp_type=7, label=2, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR), _descriptor.FieldDescriptor(name='objectGlobalPose', full_name='mvsim_msgs.SrvSetPoseAnswer.objectGlobalPose', index=3, number=5, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR)], extensions=[], nested_types=[], enum_types=[], serialized_options=None, is_extendable=False, syntax='proto2', extension_ranges=[], oneofs=[], serialized_start=51, serialized_end=181)
_SRVSETPOSEANSWER.fields_by_name['objectGlobalPose'].message_type = Pose__pb2._POSE
DESCRIPTOR.message_types_by_name['SrvSetPoseAnswer'] = _SRVSETPOSEANSWER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
SrvSetPoseAnswer = _reflection.GeneratedProtocolMessageType('SrvSetPoseAnswer', (_message.Message,), dict(DESCRIPTOR=_SRVSETPOSEANSWER, __module__='SrvSetPoseAnswer_pb2'))
_sym_db.RegisterMessage(SrvSetPoseAnswer)
