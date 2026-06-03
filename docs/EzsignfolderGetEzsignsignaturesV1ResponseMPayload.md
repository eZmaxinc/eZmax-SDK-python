# EzsignfolderGetEzsignsignaturesV1ResponseMPayload

Payload for GET /1/object/ezsignfolder/{pkiEzsignfolderID}/getEzsignsignatures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigndocument** | [**List[CustomEzsigndocumentGetEzsignsignaturesResponse]**](CustomEzsigndocumentGetEzsignsignaturesResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_ezsignsignatures_v1_response_m_payload import EzsignfolderGetEzsignsignaturesV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetEzsignsignaturesV1ResponseMPayload from a JSON string
ezsignfolder_get_ezsignsignatures_v1_response_m_payload_instance = EzsignfolderGetEzsignsignaturesV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetEzsignsignaturesV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignfolder_get_ezsignsignatures_v1_response_m_payload_dict = ezsignfolder_get_ezsignsignatures_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderGetEzsignsignaturesV1ResponseMPayload from a dict
ezsignfolder_get_ezsignsignatures_v1_response_m_payload_from_dict = EzsignfolderGetEzsignsignaturesV1ResponseMPayload.from_dict(ezsignfolder_get_ezsignsignatures_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


