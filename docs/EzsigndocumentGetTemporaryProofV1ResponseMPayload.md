# EzsigndocumentGetTemporaryProofV1ResponseMPayload

Payload for GET /1/object/ezsigndocument/{pkiEzsigndocumentID}/getTemporaryProof

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigndocumentlog** | [**List[EzsigndocumentlogResponseCompound]**](EzsigndocumentlogResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_temporary_proof_v1_response_m_payload import EzsigndocumentGetTemporaryProofV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetTemporaryProofV1ResponseMPayload from a JSON string
ezsigndocument_get_temporary_proof_v1_response_m_payload_instance = EzsigndocumentGetTemporaryProofV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetTemporaryProofV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigndocument_get_temporary_proof_v1_response_m_payload_dict = ezsigndocument_get_temporary_proof_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigndocumentGetTemporaryProofV1ResponseMPayload from a dict
ezsigndocument_get_temporary_proof_v1_response_m_payload_form_dict = ezsigndocument_get_temporary_proof_v1_response_m_payload.from_dict(ezsigndocument_get_temporary_proof_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


