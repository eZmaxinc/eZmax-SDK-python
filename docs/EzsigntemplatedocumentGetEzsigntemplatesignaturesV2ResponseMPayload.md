# EzsigntemplatedocumentGetEzsigntemplatesignaturesV2ResponseMPayload

Payload for GET /2/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/getEzsigntemplatesignatures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatesignature** | [**List[EzsigntemplatesignatureResponseCompound]**](EzsigntemplatesignatureResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_get_ezsigntemplatesignatures_v2_response_m_payload import EzsigntemplatedocumentGetEzsigntemplatesignaturesV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentGetEzsigntemplatesignaturesV2ResponseMPayload from a JSON string
ezsigntemplatedocument_get_ezsigntemplatesignatures_v2_response_m_payload_instance = EzsigntemplatedocumentGetEzsigntemplatesignaturesV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentGetEzsigntemplatesignaturesV2ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatedocument_get_ezsigntemplatesignatures_v2_response_m_payload_dict = ezsigntemplatedocument_get_ezsigntemplatesignatures_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatedocumentGetEzsigntemplatesignaturesV2ResponseMPayload from a dict
ezsigntemplatedocument_get_ezsigntemplatesignatures_v2_response_m_payload_from_dict = EzsigntemplatedocumentGetEzsigntemplatesignaturesV2ResponseMPayload.from_dict(ezsigntemplatedocument_get_ezsigntemplatesignatures_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


