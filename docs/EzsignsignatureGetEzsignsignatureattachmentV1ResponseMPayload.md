# EzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload

Response for GET /1/object/ezsignsignature/{pkiEzsignsignatureID}/getEzsignsignatureattachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignsignatureattachment** | [**List[EzsignsignatureattachmentResponse]**](EzsignsignatureattachmentResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_get_ezsignsignatureattachment_v1_response_m_payload import EzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload from a JSON string
ezsignsignature_get_ezsignsignatureattachment_v1_response_m_payload_instance = EzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload.to_json()

# convert the object into a dict
ezsignsignature_get_ezsignsignatureattachment_v1_response_m_payload_dict = ezsignsignature_get_ezsignsignatureattachment_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload from a dict
ezsignsignature_get_ezsignsignatureattachment_v1_response_m_payload_form_dict = ezsignsignature_get_ezsignsignatureattachment_v1_response_m_payload.from_dict(ezsignsignature_get_ezsignsignatureattachment_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


