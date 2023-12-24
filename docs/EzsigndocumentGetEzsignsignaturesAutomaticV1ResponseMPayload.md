# EzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload

Payload for GET /1/object/ezsigndocument/{pkiEzsigndocumentID}/getEzsignsignaturesAutomatic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_e_ezsignsignature_type** | [**List[FieldEEzsignsignatureType]**](FieldEEzsignsignatureType.md) | All eEzsignsignatureType contained in the response | 
**a_obj_ezsignfolder** | [**List[CustomEzsignfolderEzsignsignaturesAutomaticResponse]**](CustomEzsignfolderEzsignsignaturesAutomaticResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_ezsignsignatures_automatic_v1_response_m_payload import EzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload from a JSON string
ezsigndocument_get_ezsignsignatures_automatic_v1_response_m_payload_instance = EzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload.to_json()

# convert the object into a dict
ezsigndocument_get_ezsignsignatures_automatic_v1_response_m_payload_dict = ezsigndocument_get_ezsignsignatures_automatic_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload from a dict
ezsigndocument_get_ezsignsignatures_automatic_v1_response_m_payload_form_dict = ezsigndocument_get_ezsignsignatures_automatic_v1_response_m_payload.from_dict(ezsigndocument_get_ezsignsignatures_automatic_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


