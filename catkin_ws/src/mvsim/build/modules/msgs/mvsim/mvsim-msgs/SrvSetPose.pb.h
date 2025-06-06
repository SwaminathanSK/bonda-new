// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: SrvSetPose.proto

#ifndef PROTOBUF_INCLUDED_SrvSetPose_2eproto
#define PROTOBUF_INCLUDED_SrvSetPose_2eproto

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 3006001
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 3006001 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/inlined_string_field.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/unknown_field_set.h>
#include "Pose.pb.h"
// @@protoc_insertion_point(includes)
#define PROTOBUF_INTERNAL_EXPORT_protobuf_SrvSetPose_2eproto 

namespace protobuf_SrvSetPose_2eproto {
// Internal implementation detail -- do not use these members.
struct TableStruct {
  static const ::google::protobuf::internal::ParseTableField entries[];
  static const ::google::protobuf::internal::AuxillaryParseTableField aux[];
  static const ::google::protobuf::internal::ParseTable schema[1];
  static const ::google::protobuf::internal::FieldMetadata field_metadata[];
  static const ::google::protobuf::internal::SerializationTable serialization_table[];
  static const ::google::protobuf::uint32 offsets[];
};
void AddDescriptors();
}  // namespace protobuf_SrvSetPose_2eproto
namespace mvsim_msgs {
class SrvSetPose;
class SrvSetPoseDefaultTypeInternal;
extern SrvSetPoseDefaultTypeInternal _SrvSetPose_default_instance_;
}  // namespace mvsim_msgs
namespace google {
namespace protobuf {
template<> ::mvsim_msgs::SrvSetPose* Arena::CreateMaybeMessage<::mvsim_msgs::SrvSetPose>(Arena*);
}  // namespace protobuf
}  // namespace google
namespace mvsim_msgs {

// ===================================================================

class SrvSetPose : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:mvsim_msgs.SrvSetPose) */ {
 public:
  SrvSetPose();
  virtual ~SrvSetPose();

  SrvSetPose(const SrvSetPose& from);

  inline SrvSetPose& operator=(const SrvSetPose& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  SrvSetPose(SrvSetPose&& from) noexcept
    : SrvSetPose() {
    *this = ::std::move(from);
  }

  inline SrvSetPose& operator=(SrvSetPose&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _internal_metadata_.unknown_fields();
  }
  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return _internal_metadata_.mutable_unknown_fields();
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const SrvSetPose& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const SrvSetPose* internal_default_instance() {
    return reinterpret_cast<const SrvSetPose*>(
               &_SrvSetPose_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  void Swap(SrvSetPose* other);
  friend void swap(SrvSetPose& a, SrvSetPose& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline SrvSetPose* New() const final {
    return CreateMaybeMessage<SrvSetPose>(NULL);
  }

  SrvSetPose* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<SrvSetPose>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const SrvSetPose& from);
  void MergeFrom(const SrvSetPose& from);
  void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(SrvSetPose* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return NULL;
  }
  inline void* MaybeArenaPtr() const {
    return NULL;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // required string objectId = 1;
  bool has_objectid() const;
  void clear_objectid();
  static const int kObjectIdFieldNumber = 1;
  const ::std::string& objectid() const;
  void set_objectid(const ::std::string& value);
  #if LANG_CXX11
  void set_objectid(::std::string&& value);
  #endif
  void set_objectid(const char* value);
  void set_objectid(const char* value, size_t size);
  ::std::string* mutable_objectid();
  ::std::string* release_objectid();
  void set_allocated_objectid(::std::string* objectid);

  // required .mvsim_msgs.Pose pose = 2;
  bool has_pose() const;
  void clear_pose();
  static const int kPoseFieldNumber = 2;
  private:
  const ::mvsim_msgs::Pose& _internal_pose() const;
  public:
  const ::mvsim_msgs::Pose& pose() const;
  ::mvsim_msgs::Pose* release_pose();
  ::mvsim_msgs::Pose* mutable_pose();
  void set_allocated_pose(::mvsim_msgs::Pose* pose);

  // optional bool relativeIncrement = 3;
  bool has_relativeincrement() const;
  void clear_relativeincrement();
  static const int kRelativeIncrementFieldNumber = 3;
  bool relativeincrement() const;
  void set_relativeincrement(bool value);

  // @@protoc_insertion_point(class_scope:mvsim_msgs.SrvSetPose)
 private:
  void set_has_objectid();
  void clear_has_objectid();
  void set_has_pose();
  void clear_has_pose();
  void set_has_relativeincrement();
  void clear_has_relativeincrement();

  // helper for ByteSizeLong()
  size_t RequiredFieldsByteSizeFallback() const;

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::internal::HasBits<1> _has_bits_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  ::google::protobuf::internal::ArenaStringPtr objectid_;
  ::mvsim_msgs::Pose* pose_;
  bool relativeincrement_;
  friend struct ::protobuf_SrvSetPose_2eproto::TableStruct;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// SrvSetPose

// required string objectId = 1;
inline bool SrvSetPose::has_objectid() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void SrvSetPose::set_has_objectid() {
  _has_bits_[0] |= 0x00000001u;
}
inline void SrvSetPose::clear_has_objectid() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void SrvSetPose::clear_objectid() {
  objectid_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  clear_has_objectid();
}
inline const ::std::string& SrvSetPose::objectid() const {
  // @@protoc_insertion_point(field_get:mvsim_msgs.SrvSetPose.objectId)
  return objectid_.GetNoArena();
}
inline void SrvSetPose::set_objectid(const ::std::string& value) {
  set_has_objectid();
  objectid_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:mvsim_msgs.SrvSetPose.objectId)
}
#if LANG_CXX11
inline void SrvSetPose::set_objectid(::std::string&& value) {
  set_has_objectid();
  objectid_.SetNoArena(
    &::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::move(value));
  // @@protoc_insertion_point(field_set_rvalue:mvsim_msgs.SrvSetPose.objectId)
}
#endif
inline void SrvSetPose::set_objectid(const char* value) {
  GOOGLE_DCHECK(value != NULL);
  set_has_objectid();
  objectid_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:mvsim_msgs.SrvSetPose.objectId)
}
inline void SrvSetPose::set_objectid(const char* value, size_t size) {
  set_has_objectid();
  objectid_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:mvsim_msgs.SrvSetPose.objectId)
}
inline ::std::string* SrvSetPose::mutable_objectid() {
  set_has_objectid();
  // @@protoc_insertion_point(field_mutable:mvsim_msgs.SrvSetPose.objectId)
  return objectid_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* SrvSetPose::release_objectid() {
  // @@protoc_insertion_point(field_release:mvsim_msgs.SrvSetPose.objectId)
  if (!has_objectid()) {
    return NULL;
  }
  clear_has_objectid();
  return objectid_.ReleaseNonDefaultNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void SrvSetPose::set_allocated_objectid(::std::string* objectid) {
  if (objectid != NULL) {
    set_has_objectid();
  } else {
    clear_has_objectid();
  }
  objectid_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), objectid);
  // @@protoc_insertion_point(field_set_allocated:mvsim_msgs.SrvSetPose.objectId)
}

// required .mvsim_msgs.Pose pose = 2;
inline bool SrvSetPose::has_pose() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void SrvSetPose::set_has_pose() {
  _has_bits_[0] |= 0x00000002u;
}
inline void SrvSetPose::clear_has_pose() {
  _has_bits_[0] &= ~0x00000002u;
}
inline const ::mvsim_msgs::Pose& SrvSetPose::_internal_pose() const {
  return *pose_;
}
inline const ::mvsim_msgs::Pose& SrvSetPose::pose() const {
  const ::mvsim_msgs::Pose* p = pose_;
  // @@protoc_insertion_point(field_get:mvsim_msgs.SrvSetPose.pose)
  return p != NULL ? *p : *reinterpret_cast<const ::mvsim_msgs::Pose*>(
      &::mvsim_msgs::_Pose_default_instance_);
}
inline ::mvsim_msgs::Pose* SrvSetPose::release_pose() {
  // @@protoc_insertion_point(field_release:mvsim_msgs.SrvSetPose.pose)
  clear_has_pose();
  ::mvsim_msgs::Pose* temp = pose_;
  pose_ = NULL;
  return temp;
}
inline ::mvsim_msgs::Pose* SrvSetPose::mutable_pose() {
  set_has_pose();
  if (pose_ == NULL) {
    auto* p = CreateMaybeMessage<::mvsim_msgs::Pose>(GetArenaNoVirtual());
    pose_ = p;
  }
  // @@protoc_insertion_point(field_mutable:mvsim_msgs.SrvSetPose.pose)
  return pose_;
}
inline void SrvSetPose::set_allocated_pose(::mvsim_msgs::Pose* pose) {
  ::google::protobuf::Arena* message_arena = GetArenaNoVirtual();
  if (message_arena == NULL) {
    delete reinterpret_cast< ::google::protobuf::MessageLite*>(pose_);
  }
  if (pose) {
    ::google::protobuf::Arena* submessage_arena = NULL;
    if (message_arena != submessage_arena) {
      pose = ::google::protobuf::internal::GetOwnedMessage(
          message_arena, pose, submessage_arena);
    }
    set_has_pose();
  } else {
    clear_has_pose();
  }
  pose_ = pose;
  // @@protoc_insertion_point(field_set_allocated:mvsim_msgs.SrvSetPose.pose)
}

// optional bool relativeIncrement = 3;
inline bool SrvSetPose::has_relativeincrement() const {
  return (_has_bits_[0] & 0x00000004u) != 0;
}
inline void SrvSetPose::set_has_relativeincrement() {
  _has_bits_[0] |= 0x00000004u;
}
inline void SrvSetPose::clear_has_relativeincrement() {
  _has_bits_[0] &= ~0x00000004u;
}
inline void SrvSetPose::clear_relativeincrement() {
  relativeincrement_ = false;
  clear_has_relativeincrement();
}
inline bool SrvSetPose::relativeincrement() const {
  // @@protoc_insertion_point(field_get:mvsim_msgs.SrvSetPose.relativeIncrement)
  return relativeincrement_;
}
inline void SrvSetPose::set_relativeincrement(bool value) {
  set_has_relativeincrement();
  relativeincrement_ = value;
  // @@protoc_insertion_point(field_set:mvsim_msgs.SrvSetPose.relativeIncrement)
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__

// @@protoc_insertion_point(namespace_scope)

}  // namespace mvsim_msgs

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_INCLUDED_SrvSetPose_2eproto
