// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: SubscribeAnswer.proto

#ifndef PROTOBUF_INCLUDED_SubscribeAnswer_2eproto
#define PROTOBUF_INCLUDED_SubscribeAnswer_2eproto

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
// @@protoc_insertion_point(includes)
#define PROTOBUF_INTERNAL_EXPORT_protobuf_SubscribeAnswer_2eproto 

namespace protobuf_SubscribeAnswer_2eproto {
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
}  // namespace protobuf_SubscribeAnswer_2eproto
namespace mvsim_msgs {
class SubscribeAnswer;
class SubscribeAnswerDefaultTypeInternal;
extern SubscribeAnswerDefaultTypeInternal _SubscribeAnswer_default_instance_;
}  // namespace mvsim_msgs
namespace google {
namespace protobuf {
template<> ::mvsim_msgs::SubscribeAnswer* Arena::CreateMaybeMessage<::mvsim_msgs::SubscribeAnswer>(Arena*);
}  // namespace protobuf
}  // namespace google
namespace mvsim_msgs {

// ===================================================================

class SubscribeAnswer : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:mvsim_msgs.SubscribeAnswer) */ {
 public:
  SubscribeAnswer();
  virtual ~SubscribeAnswer();

  SubscribeAnswer(const SubscribeAnswer& from);

  inline SubscribeAnswer& operator=(const SubscribeAnswer& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  SubscribeAnswer(SubscribeAnswer&& from) noexcept
    : SubscribeAnswer() {
    *this = ::std::move(from);
  }

  inline SubscribeAnswer& operator=(SubscribeAnswer&& from) noexcept {
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
  static const SubscribeAnswer& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const SubscribeAnswer* internal_default_instance() {
    return reinterpret_cast<const SubscribeAnswer*>(
               &_SubscribeAnswer_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  void Swap(SubscribeAnswer* other);
  friend void swap(SubscribeAnswer& a, SubscribeAnswer& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline SubscribeAnswer* New() const final {
    return CreateMaybeMessage<SubscribeAnswer>(NULL);
  }

  SubscribeAnswer* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<SubscribeAnswer>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const SubscribeAnswer& from);
  void MergeFrom(const SubscribeAnswer& from);
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
  void InternalSwap(SubscribeAnswer* other);
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

  // required string topic = 1;
  bool has_topic() const;
  void clear_topic();
  static const int kTopicFieldNumber = 1;
  const ::std::string& topic() const;
  void set_topic(const ::std::string& value);
  #if LANG_CXX11
  void set_topic(::std::string&& value);
  #endif
  void set_topic(const char* value);
  void set_topic(const char* value, size_t size);
  ::std::string* mutable_topic();
  ::std::string* release_topic();
  void set_allocated_topic(::std::string* topic);

  // required bool success = 2;
  bool has_success() const;
  void clear_success();
  static const int kSuccessFieldNumber = 2;
  bool success() const;
  void set_success(bool value);

  // @@protoc_insertion_point(class_scope:mvsim_msgs.SubscribeAnswer)
 private:
  void set_has_topic();
  void clear_has_topic();
  void set_has_success();
  void clear_has_success();

  // helper for ByteSizeLong()
  size_t RequiredFieldsByteSizeFallback() const;

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::internal::HasBits<1> _has_bits_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  ::google::protobuf::internal::ArenaStringPtr topic_;
  bool success_;
  friend struct ::protobuf_SubscribeAnswer_2eproto::TableStruct;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// SubscribeAnswer

// required string topic = 1;
inline bool SubscribeAnswer::has_topic() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void SubscribeAnswer::set_has_topic() {
  _has_bits_[0] |= 0x00000001u;
}
inline void SubscribeAnswer::clear_has_topic() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void SubscribeAnswer::clear_topic() {
  topic_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  clear_has_topic();
}
inline const ::std::string& SubscribeAnswer::topic() const {
  // @@protoc_insertion_point(field_get:mvsim_msgs.SubscribeAnswer.topic)
  return topic_.GetNoArena();
}
inline void SubscribeAnswer::set_topic(const ::std::string& value) {
  set_has_topic();
  topic_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:mvsim_msgs.SubscribeAnswer.topic)
}
#if LANG_CXX11
inline void SubscribeAnswer::set_topic(::std::string&& value) {
  set_has_topic();
  topic_.SetNoArena(
    &::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::move(value));
  // @@protoc_insertion_point(field_set_rvalue:mvsim_msgs.SubscribeAnswer.topic)
}
#endif
inline void SubscribeAnswer::set_topic(const char* value) {
  GOOGLE_DCHECK(value != NULL);
  set_has_topic();
  topic_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:mvsim_msgs.SubscribeAnswer.topic)
}
inline void SubscribeAnswer::set_topic(const char* value, size_t size) {
  set_has_topic();
  topic_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:mvsim_msgs.SubscribeAnswer.topic)
}
inline ::std::string* SubscribeAnswer::mutable_topic() {
  set_has_topic();
  // @@protoc_insertion_point(field_mutable:mvsim_msgs.SubscribeAnswer.topic)
  return topic_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* SubscribeAnswer::release_topic() {
  // @@protoc_insertion_point(field_release:mvsim_msgs.SubscribeAnswer.topic)
  if (!has_topic()) {
    return NULL;
  }
  clear_has_topic();
  return topic_.ReleaseNonDefaultNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void SubscribeAnswer::set_allocated_topic(::std::string* topic) {
  if (topic != NULL) {
    set_has_topic();
  } else {
    clear_has_topic();
  }
  topic_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), topic);
  // @@protoc_insertion_point(field_set_allocated:mvsim_msgs.SubscribeAnswer.topic)
}

// required bool success = 2;
inline bool SubscribeAnswer::has_success() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void SubscribeAnswer::set_has_success() {
  _has_bits_[0] |= 0x00000002u;
}
inline void SubscribeAnswer::clear_has_success() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void SubscribeAnswer::clear_success() {
  success_ = false;
  clear_has_success();
}
inline bool SubscribeAnswer::success() const {
  // @@protoc_insertion_point(field_get:mvsim_msgs.SubscribeAnswer.success)
  return success_;
}
inline void SubscribeAnswer::set_success(bool value) {
  set_has_success();
  success_ = value;
  // @@protoc_insertion_point(field_set:mvsim_msgs.SubscribeAnswer.success)
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__

// @@protoc_insertion_point(namespace_scope)

}  // namespace mvsim_msgs

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_INCLUDED_SubscribeAnswer_2eproto
