# EzsignfolderGetEzsignsignaturesAutomaticV1Response

Response for GET /1/object/ezsignfolder/{pkiEzsignfolderID}/getEzsignsignaturesAutomatic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignfolderGetEzsignsignaturesAutomaticV1ResponseMPayload**](EzsignfolderGetEzsignsignaturesAutomaticV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_ezsignsignatures_automatic_v1_response import EzsignfolderGetEzsignsignaturesAutomaticV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetEzsignsignaturesAutomaticV1Response from a JSON string
ezsignfolder_get_ezsignsignatures_automatic_v1_response_instance = EzsignfolderGetEzsignsignaturesAutomaticV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetEzsignsignaturesAutomaticV1Response.to_json())

# convert the object into a dict
ezsignfolder_get_ezsignsignatures_automatic_v1_response_dict = ezsignfolder_get_ezsignsignatures_automatic_v1_response_instance.to_dict()
# create an instance of EzsignfolderGetEzsignsignaturesAutomaticV1Response from a dict
ezsignfolder_get_ezsignsignatures_automatic_v1_response_from_dict = EzsignfolderGetEzsignsignaturesAutomaticV1Response.from_dict(ezsignfolder_get_ezsignsignatures_automatic_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


