# EzsigntemplatedocumentGetEzsigntemplatesignaturesV1ResponseMPayload

Payload for GET /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocument}/getEzsigntemplatesignatures

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatesignature** | [**List[EzsigntemplatesignatureResponseCompound]**](EzsigntemplatesignatureResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response_m_payload import EzsigntemplatedocumentGetEzsigntemplatesignaturesV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentGetEzsigntemplatesignaturesV1ResponseMPayload from a JSON string
ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response_m_payload_instance = EzsigntemplatedocumentGetEzsigntemplatesignaturesV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatedocumentGetEzsigntemplatesignaturesV1ResponseMPayload.to_json()

# convert the object into a dict
ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response_m_payload_dict = ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatedocumentGetEzsigntemplatesignaturesV1ResponseMPayload from a dict
ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response_m_payload_form_dict = ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response_m_payload.from_dict(ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


