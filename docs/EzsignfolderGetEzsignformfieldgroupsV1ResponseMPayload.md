# EzsignfolderGetEzsignformfieldgroupsV1ResponseMPayload

Payload for GET /1/object/ezsignfolder/{pkiEzsignfolderID}/getEzsignformfieldgroups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigndocument** | [**List[CustomEzsigndocumentGetEzsignformfieldgroupsResponse]**](CustomEzsigndocumentGetEzsignformfieldgroupsResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_ezsignformfieldgroups_v1_response_m_payload import EzsignfolderGetEzsignformfieldgroupsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetEzsignformfieldgroupsV1ResponseMPayload from a JSON string
ezsignfolder_get_ezsignformfieldgroups_v1_response_m_payload_instance = EzsignfolderGetEzsignformfieldgroupsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetEzsignformfieldgroupsV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignfolder_get_ezsignformfieldgroups_v1_response_m_payload_dict = ezsignfolder_get_ezsignformfieldgroups_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderGetEzsignformfieldgroupsV1ResponseMPayload from a dict
ezsignfolder_get_ezsignformfieldgroups_v1_response_m_payload_from_dict = EzsignfolderGetEzsignformfieldgroupsV1ResponseMPayload.from_dict(ezsignfolder_get_ezsignformfieldgroups_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


