# EzsignsignatureGetEzsignsignaturesAutomaticV1ResponseMPayload

Payload for GET /1/object/ezsigsignature/getEzsignsignaturesAutomatic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_e_ezsignsignature_type** | [**List[FieldEEzsignsignatureType]**](FieldEEzsignsignatureType.md) | All eEzsignsignatureType contained in the response | 
**a_obj_ezsignfolder** | [**List[CustomEzsignfolderEzsignsignaturesAutomaticResponse]**](CustomEzsignfolderEzsignsignaturesAutomaticResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_get_ezsignsignatures_automatic_v1_response_m_payload import EzsignsignatureGetEzsignsignaturesAutomaticV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureGetEzsignsignaturesAutomaticV1ResponseMPayload from a JSON string
ezsignsignature_get_ezsignsignatures_automatic_v1_response_m_payload_instance = EzsignsignatureGetEzsignsignaturesAutomaticV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignsignatureGetEzsignsignaturesAutomaticV1ResponseMPayload.to_json()

# convert the object into a dict
ezsignsignature_get_ezsignsignatures_automatic_v1_response_m_payload_dict = ezsignsignature_get_ezsignsignatures_automatic_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignsignatureGetEzsignsignaturesAutomaticV1ResponseMPayload from a dict
ezsignsignature_get_ezsignsignatures_automatic_v1_response_m_payload_form_dict = ezsignsignature_get_ezsignsignatures_automatic_v1_response_m_payload.from_dict(ezsignsignature_get_ezsignsignatures_automatic_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


