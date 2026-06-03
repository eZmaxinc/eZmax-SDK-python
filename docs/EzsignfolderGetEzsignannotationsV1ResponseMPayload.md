# EzsignfolderGetEzsignannotationsV1ResponseMPayload

Payload for GET /1/object/ezsignfolder/{pkiEzsignfolderID}/getEzsignannotations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigndocument** | [**List[CustomEzsigndocumentGetEzsignannotationsResponse]**](CustomEzsigndocumentGetEzsignannotationsResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_ezsignannotations_v1_response_m_payload import EzsignfolderGetEzsignannotationsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetEzsignannotationsV1ResponseMPayload from a JSON string
ezsignfolder_get_ezsignannotations_v1_response_m_payload_instance = EzsignfolderGetEzsignannotationsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetEzsignannotationsV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignfolder_get_ezsignannotations_v1_response_m_payload_dict = ezsignfolder_get_ezsignannotations_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderGetEzsignannotationsV1ResponseMPayload from a dict
ezsignfolder_get_ezsignannotations_v1_response_m_payload_from_dict = EzsignfolderGetEzsignannotationsV1ResponseMPayload.from_dict(ezsignfolder_get_ezsignannotations_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


