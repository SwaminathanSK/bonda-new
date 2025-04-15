// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: SrvGetPose.proto

#include "SrvGetPose.pb.h"

#include <algorithm>

#include <google/protobuf/stubs/common.h>
#include <google/protobuf/stubs/port.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/wire_format_lite_inl.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// This is a temporary google only hack
#ifdef GOOGLE_PROTOBUF_ENFORCE_UNIQUENESS
#include "third_party/protobuf/version.h"
#endif
// @@protoc_insertion_point(includes)

namespace mvsim_msgs {
class SrvGetPoseDefaultTypeInternal {
 public:
  ::google::protobuf::internal::ExplicitlyConstructed<SrvGetPose>
      _instance;
} _SrvGetPose_default_instance_;
}  // namespace mvsim_msgs
namespace protobuf_SrvGetPose_2eproto {
static void InitDefaultsSrvGetPose() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::mvsim_msgs::_SrvGetPose_default_instance_;
    new (ptr) ::mvsim_msgs::SrvGetPose();
    ::google::protobuf::internal::OnShutdownDestroyMessage(ptr);
  }
  ::mvsim_msgs::SrvGetPose::InitAsDefaultInstance();
}

::google::protobuf::internal::SCCInfo<0> scc_info_SrvGetPose =
    {{ATOMIC_VAR_INIT(::google::protobuf::internal::SCCInfoBase::kUninitialized), 0, InitDefaultsSrvGetPose}, {}};

void InitDefaults() {
  ::google::protobuf::internal::InitSCC(&scc_info_SrvGetPose.base);
}

::google::protobuf::Metadata file_level_metadata[1];

const ::google::protobuf::uint32 TableStruct::offsets[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::mvsim_msgs::SrvGetPose, _has_bits_),
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::mvsim_msgs::SrvGetPose, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::mvsim_msgs::SrvGetPose, objectid_),
  0,
};
static const ::google::protobuf::internal::MigrationSchema schemas[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
  { 0, 6, sizeof(::mvsim_msgs::SrvGetPose)},
};

static ::google::protobuf::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::google::protobuf::Message*>(&::mvsim_msgs::_SrvGetPose_default_instance_),
};

void protobuf_AssignDescriptors() {
  AddDescriptors();
  AssignDescriptors(
      "SrvGetPose.proto", schemas, file_default_instances, TableStruct::offsets,
      file_level_metadata, NULL, NULL);
}

void protobuf_AssignDescriptorsOnce() {
  static ::google::protobuf::internal::once_flag once;
  ::google::protobuf::internal::call_once(once, protobuf_AssignDescriptors);
}

void protobuf_RegisterTypes(const ::std::string&) GOOGLE_PROTOBUF_ATTRIBUTE_COLD;
void protobuf_RegisterTypes(const ::std::string&) {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::internal::RegisterAllTypes(file_level_metadata, 1);
}

void AddDescriptorsImpl() {
  InitDefaults();
  static const char descriptor[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
      "\n\020SrvGetPose.proto\022\nmvsim_msgs\"\036\n\nSrvGet"
      "Pose\022\020\n\010objectId\030\001 \002(\t"
  };
  ::google::protobuf::DescriptorPool::InternalAddGeneratedFile(
      descriptor, 62);
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedFile(
    "SrvGetPose.proto", &protobuf_RegisterTypes);
}

void AddDescriptors() {
  static ::google::protobuf::internal::once_flag once;
  ::google::protobuf::internal::call_once(once, AddDescriptorsImpl);
}
// Force AddDescriptors() to be called at dynamic initialization time.
struct StaticDescriptorInitializer {
  StaticDescriptorInitializer() {
    AddDescriptors();
  }
} static_descriptor_initializer;
}  // namespace protobuf_SrvGetPose_2eproto
namespace mvsim_msgs {

// ===================================================================

void SrvGetPose::InitAsDefaultInstance() {
}
#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int SrvGetPose::kObjectIdFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

SrvGetPose::SrvGetPose()
  : ::google::protobuf::Message(), _internal_metadata_(NULL) {
  ::google::protobuf::internal::InitSCC(
      &protobuf_SrvGetPose_2eproto::scc_info_SrvGetPose.base);
  SharedCtor();
  // @@protoc_insertion_point(constructor:mvsim_msgs.SrvGetPose)
}
SrvGetPose::SrvGetPose(const SrvGetPose& from)
  : ::google::protobuf::Message(),
      _internal_metadata_(NULL),
      _has_bits_(from._has_bits_) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  objectid_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  if (from.has_objectid()) {
    objectid_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.objectid_);
  }
  // @@protoc_insertion_point(copy_constructor:mvsim_msgs.SrvGetPose)
}

void SrvGetPose::SharedCtor() {
  objectid_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}

SrvGetPose::~SrvGetPose() {
  // @@protoc_insertion_point(destructor:mvsim_msgs.SrvGetPose)
  SharedDtor();
}

void SrvGetPose::SharedDtor() {
  objectid_.DestroyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}

void SrvGetPose::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const ::google::protobuf::Descriptor* SrvGetPose::descriptor() {
  ::protobuf_SrvGetPose_2eproto::protobuf_AssignDescriptorsOnce();
  return ::protobuf_SrvGetPose_2eproto::file_level_metadata[kIndexInFileMessages].descriptor;
}

const SrvGetPose& SrvGetPose::default_instance() {
  ::google::protobuf::internal::InitSCC(&protobuf_SrvGetPose_2eproto::scc_info_SrvGetPose.base);
  return *internal_default_instance();
}


void SrvGetPose::Clear() {
// @@protoc_insertion_point(message_clear_start:mvsim_msgs.SrvGetPose)
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  cached_has_bits = _has_bits_[0];
  if (cached_has_bits & 0x00000001u) {
    objectid_.ClearNonDefaultToEmptyNoArena();
  }
  _has_bits_.Clear();
  _internal_metadata_.Clear();
}

bool SrvGetPose::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!GOOGLE_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:mvsim_msgs.SrvGetPose)
  for (;;) {
    ::std::pair<::google::protobuf::uint32, bool> p = input->ReadTagWithCutoffNoLastTag(127u);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // required string objectId = 1;
      case 1: {
        if (static_cast< ::google::protobuf::uint8>(tag) ==
            static_cast< ::google::protobuf::uint8>(10u /* 10 & 0xFF */)) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadString(
                input, this->mutable_objectid()));
          ::google::protobuf::internal::WireFormat::VerifyUTF8StringNamedField(
            this->objectid().data(), static_cast<int>(this->objectid().length()),
            ::google::protobuf::internal::WireFormat::PARSE,
            "mvsim_msgs.SrvGetPose.objectId");
        } else {
          goto handle_unusual;
        }
        break;
      }

      default: {
      handle_unusual:
        if (tag == 0) {
          goto success;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, _internal_metadata_.mutable_unknown_fields()));
        break;
      }
    }
  }
success:
  // @@protoc_insertion_point(parse_success:mvsim_msgs.SrvGetPose)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:mvsim_msgs.SrvGetPose)
  return false;
#undef DO_
}

void SrvGetPose::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:mvsim_msgs.SrvGetPose)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  cached_has_bits = _has_bits_[0];
  // required string objectId = 1;
  if (cached_has_bits & 0x00000001u) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8StringNamedField(
      this->objectid().data(), static_cast<int>(this->objectid().length()),
      ::google::protobuf::internal::WireFormat::SERIALIZE,
      "mvsim_msgs.SrvGetPose.objectId");
    ::google::protobuf::internal::WireFormatLite::WriteStringMaybeAliased(
      1, this->objectid(), output);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        _internal_metadata_.unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:mvsim_msgs.SrvGetPose)
}

::google::protobuf::uint8* SrvGetPose::InternalSerializeWithCachedSizesToArray(
    bool deterministic, ::google::protobuf::uint8* target) const {
  (void)deterministic; // Unused
  // @@protoc_insertion_point(serialize_to_array_start:mvsim_msgs.SrvGetPose)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  cached_has_bits = _has_bits_[0];
  // required string objectId = 1;
  if (cached_has_bits & 0x00000001u) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8StringNamedField(
      this->objectid().data(), static_cast<int>(this->objectid().length()),
      ::google::protobuf::internal::WireFormat::SERIALIZE,
      "mvsim_msgs.SrvGetPose.objectId");
    target =
      ::google::protobuf::internal::WireFormatLite::WriteStringToArray(
        1, this->objectid(), target);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:mvsim_msgs.SrvGetPose)
  return target;
}

size_t SrvGetPose::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:mvsim_msgs.SrvGetPose)
  size_t total_size = 0;

  if (_internal_metadata_.have_unknown_fields()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        _internal_metadata_.unknown_fields());
  }
  // required string objectId = 1;
  if (has_objectid()) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::StringSize(
        this->objectid());
  }
  int cached_size = ::google::protobuf::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void SrvGetPose::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:mvsim_msgs.SrvGetPose)
  GOOGLE_DCHECK_NE(&from, this);
  const SrvGetPose* source =
      ::google::protobuf::internal::DynamicCastToGenerated<const SrvGetPose>(
          &from);
  if (source == NULL) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:mvsim_msgs.SrvGetPose)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:mvsim_msgs.SrvGetPose)
    MergeFrom(*source);
  }
}

void SrvGetPose::MergeFrom(const SrvGetPose& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:mvsim_msgs.SrvGetPose)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from.has_objectid()) {
    set_has_objectid();
    objectid_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.objectid_);
  }
}

void SrvGetPose::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:mvsim_msgs.SrvGetPose)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void SrvGetPose::CopyFrom(const SrvGetPose& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:mvsim_msgs.SrvGetPose)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool SrvGetPose::IsInitialized() const {
  if ((_has_bits_[0] & 0x00000001) != 0x00000001) return false;
  return true;
}

void SrvGetPose::Swap(SrvGetPose* other) {
  if (other == this) return;
  InternalSwap(other);
}
void SrvGetPose::InternalSwap(SrvGetPose* other) {
  using std::swap;
  objectid_.Swap(&other->objectid_, &::google::protobuf::internal::GetEmptyStringAlreadyInited(),
    GetArenaNoVirtual());
  swap(_has_bits_[0], other->_has_bits_[0]);
  _internal_metadata_.Swap(&other->_internal_metadata_);
}

::google::protobuf::Metadata SrvGetPose::GetMetadata() const {
  protobuf_SrvGetPose_2eproto::protobuf_AssignDescriptorsOnce();
  return ::protobuf_SrvGetPose_2eproto::file_level_metadata[kIndexInFileMessages];
}


// @@protoc_insertion_point(namespace_scope)
}  // namespace mvsim_msgs
namespace google {
namespace protobuf {
template<> GOOGLE_PROTOBUF_ATTRIBUTE_NOINLINE ::mvsim_msgs::SrvGetPose* Arena::CreateMaybeMessage< ::mvsim_msgs::SrvGetPose >(Arena* arena) {
  return Arena::CreateInternal< ::mvsim_msgs::SrvGetPose >(arena);
}
}  // namespace protobuf
}  // namespace google

// @@protoc_insertion_point(global_scope)
