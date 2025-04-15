// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: ListNodesRequest.proto

#include "ListNodesRequest.pb.h"

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
class ListNodesRequestDefaultTypeInternal {
 public:
  ::google::protobuf::internal::ExplicitlyConstructed<ListNodesRequest>
      _instance;
} _ListNodesRequest_default_instance_;
}  // namespace mvsim_msgs
namespace protobuf_ListNodesRequest_2eproto {
static void InitDefaultsListNodesRequest() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::mvsim_msgs::_ListNodesRequest_default_instance_;
    new (ptr) ::mvsim_msgs::ListNodesRequest();
    ::google::protobuf::internal::OnShutdownDestroyMessage(ptr);
  }
  ::mvsim_msgs::ListNodesRequest::InitAsDefaultInstance();
}

::google::protobuf::internal::SCCInfo<0> scc_info_ListNodesRequest =
    {{ATOMIC_VAR_INIT(::google::protobuf::internal::SCCInfoBase::kUninitialized), 0, InitDefaultsListNodesRequest}, {}};

void InitDefaults() {
  ::google::protobuf::internal::InitSCC(&scc_info_ListNodesRequest.base);
}

::google::protobuf::Metadata file_level_metadata[1];

const ::google::protobuf::uint32 TableStruct::offsets[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::mvsim_msgs::ListNodesRequest, _has_bits_),
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::mvsim_msgs::ListNodesRequest, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::mvsim_msgs::ListNodesRequest, nodestartswith_),
  0,
};
static const ::google::protobuf::internal::MigrationSchema schemas[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
  { 0, 6, sizeof(::mvsim_msgs::ListNodesRequest)},
};

static ::google::protobuf::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::google::protobuf::Message*>(&::mvsim_msgs::_ListNodesRequest_default_instance_),
};

void protobuf_AssignDescriptors() {
  AddDescriptors();
  AssignDescriptors(
      "ListNodesRequest.proto", schemas, file_default_instances, TableStruct::offsets,
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
      "\n\026ListNodesRequest.proto\022\nmvsim_msgs\"*\n\020"
      "ListNodesRequest\022\026\n\016nodeStartsWith\030\001 \001(\t"
  };
  ::google::protobuf::DescriptorPool::InternalAddGeneratedFile(
      descriptor, 80);
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedFile(
    "ListNodesRequest.proto", &protobuf_RegisterTypes);
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
}  // namespace protobuf_ListNodesRequest_2eproto
namespace mvsim_msgs {

// ===================================================================

void ListNodesRequest::InitAsDefaultInstance() {
}
#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int ListNodesRequest::kNodeStartsWithFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

ListNodesRequest::ListNodesRequest()
  : ::google::protobuf::Message(), _internal_metadata_(NULL) {
  ::google::protobuf::internal::InitSCC(
      &protobuf_ListNodesRequest_2eproto::scc_info_ListNodesRequest.base);
  SharedCtor();
  // @@protoc_insertion_point(constructor:mvsim_msgs.ListNodesRequest)
}
ListNodesRequest::ListNodesRequest(const ListNodesRequest& from)
  : ::google::protobuf::Message(),
      _internal_metadata_(NULL),
      _has_bits_(from._has_bits_) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  nodestartswith_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  if (from.has_nodestartswith()) {
    nodestartswith_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.nodestartswith_);
  }
  // @@protoc_insertion_point(copy_constructor:mvsim_msgs.ListNodesRequest)
}

void ListNodesRequest::SharedCtor() {
  nodestartswith_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}

ListNodesRequest::~ListNodesRequest() {
  // @@protoc_insertion_point(destructor:mvsim_msgs.ListNodesRequest)
  SharedDtor();
}

void ListNodesRequest::SharedDtor() {
  nodestartswith_.DestroyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}

void ListNodesRequest::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const ::google::protobuf::Descriptor* ListNodesRequest::descriptor() {
  ::protobuf_ListNodesRequest_2eproto::protobuf_AssignDescriptorsOnce();
  return ::protobuf_ListNodesRequest_2eproto::file_level_metadata[kIndexInFileMessages].descriptor;
}

const ListNodesRequest& ListNodesRequest::default_instance() {
  ::google::protobuf::internal::InitSCC(&protobuf_ListNodesRequest_2eproto::scc_info_ListNodesRequest.base);
  return *internal_default_instance();
}


void ListNodesRequest::Clear() {
// @@protoc_insertion_point(message_clear_start:mvsim_msgs.ListNodesRequest)
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  cached_has_bits = _has_bits_[0];
  if (cached_has_bits & 0x00000001u) {
    nodestartswith_.ClearNonDefaultToEmptyNoArena();
  }
  _has_bits_.Clear();
  _internal_metadata_.Clear();
}

bool ListNodesRequest::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!GOOGLE_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:mvsim_msgs.ListNodesRequest)
  for (;;) {
    ::std::pair<::google::protobuf::uint32, bool> p = input->ReadTagWithCutoffNoLastTag(127u);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // optional string nodeStartsWith = 1;
      case 1: {
        if (static_cast< ::google::protobuf::uint8>(tag) ==
            static_cast< ::google::protobuf::uint8>(10u /* 10 & 0xFF */)) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadString(
                input, this->mutable_nodestartswith()));
          ::google::protobuf::internal::WireFormat::VerifyUTF8StringNamedField(
            this->nodestartswith().data(), static_cast<int>(this->nodestartswith().length()),
            ::google::protobuf::internal::WireFormat::PARSE,
            "mvsim_msgs.ListNodesRequest.nodeStartsWith");
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
  // @@protoc_insertion_point(parse_success:mvsim_msgs.ListNodesRequest)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:mvsim_msgs.ListNodesRequest)
  return false;
#undef DO_
}

void ListNodesRequest::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:mvsim_msgs.ListNodesRequest)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  cached_has_bits = _has_bits_[0];
  // optional string nodeStartsWith = 1;
  if (cached_has_bits & 0x00000001u) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8StringNamedField(
      this->nodestartswith().data(), static_cast<int>(this->nodestartswith().length()),
      ::google::protobuf::internal::WireFormat::SERIALIZE,
      "mvsim_msgs.ListNodesRequest.nodeStartsWith");
    ::google::protobuf::internal::WireFormatLite::WriteStringMaybeAliased(
      1, this->nodestartswith(), output);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        _internal_metadata_.unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:mvsim_msgs.ListNodesRequest)
}

::google::protobuf::uint8* ListNodesRequest::InternalSerializeWithCachedSizesToArray(
    bool deterministic, ::google::protobuf::uint8* target) const {
  (void)deterministic; // Unused
  // @@protoc_insertion_point(serialize_to_array_start:mvsim_msgs.ListNodesRequest)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  cached_has_bits = _has_bits_[0];
  // optional string nodeStartsWith = 1;
  if (cached_has_bits & 0x00000001u) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8StringNamedField(
      this->nodestartswith().data(), static_cast<int>(this->nodestartswith().length()),
      ::google::protobuf::internal::WireFormat::SERIALIZE,
      "mvsim_msgs.ListNodesRequest.nodeStartsWith");
    target =
      ::google::protobuf::internal::WireFormatLite::WriteStringToArray(
        1, this->nodestartswith(), target);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:mvsim_msgs.ListNodesRequest)
  return target;
}

size_t ListNodesRequest::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:mvsim_msgs.ListNodesRequest)
  size_t total_size = 0;

  if (_internal_metadata_.have_unknown_fields()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        _internal_metadata_.unknown_fields());
  }
  // optional string nodeStartsWith = 1;
  if (has_nodestartswith()) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::StringSize(
        this->nodestartswith());
  }

  int cached_size = ::google::protobuf::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void ListNodesRequest::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:mvsim_msgs.ListNodesRequest)
  GOOGLE_DCHECK_NE(&from, this);
  const ListNodesRequest* source =
      ::google::protobuf::internal::DynamicCastToGenerated<const ListNodesRequest>(
          &from);
  if (source == NULL) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:mvsim_msgs.ListNodesRequest)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:mvsim_msgs.ListNodesRequest)
    MergeFrom(*source);
  }
}

void ListNodesRequest::MergeFrom(const ListNodesRequest& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:mvsim_msgs.ListNodesRequest)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from.has_nodestartswith()) {
    set_has_nodestartswith();
    nodestartswith_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.nodestartswith_);
  }
}

void ListNodesRequest::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:mvsim_msgs.ListNodesRequest)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void ListNodesRequest::CopyFrom(const ListNodesRequest& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:mvsim_msgs.ListNodesRequest)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool ListNodesRequest::IsInitialized() const {
  return true;
}

void ListNodesRequest::Swap(ListNodesRequest* other) {
  if (other == this) return;
  InternalSwap(other);
}
void ListNodesRequest::InternalSwap(ListNodesRequest* other) {
  using std::swap;
  nodestartswith_.Swap(&other->nodestartswith_, &::google::protobuf::internal::GetEmptyStringAlreadyInited(),
    GetArenaNoVirtual());
  swap(_has_bits_[0], other->_has_bits_[0]);
  _internal_metadata_.Swap(&other->_internal_metadata_);
}

::google::protobuf::Metadata ListNodesRequest::GetMetadata() const {
  protobuf_ListNodesRequest_2eproto::protobuf_AssignDescriptorsOnce();
  return ::protobuf_ListNodesRequest_2eproto::file_level_metadata[kIndexInFileMessages];
}


// @@protoc_insertion_point(namespace_scope)
}  // namespace mvsim_msgs
namespace google {
namespace protobuf {
template<> GOOGLE_PROTOBUF_ATTRIBUTE_NOINLINE ::mvsim_msgs::ListNodesRequest* Arena::CreateMaybeMessage< ::mvsim_msgs::ListNodesRequest >(Arena* arena) {
  return Arena::CreateInternal< ::mvsim_msgs::ListNodesRequest >(arena);
}
}  // namespace protobuf
}  // namespace google

// @@protoc_insertion_point(global_scope)
