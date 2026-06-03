# EzsignfolderDuplicateV1Response

Response for POST /1/object/ezsignfolder/{pkiEzsignfolderID}/duplicate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfolderDuplicateV1ResponseMPayload**](EzsignfolderDuplicateV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_duplicate_v1_response import EzsignfolderDuplicateV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderDuplicateV1Response from a JSON string
ezsignfolder_duplicate_v1_response_instance = EzsignfolderDuplicateV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderDuplicateV1Response.to_json())

# convert the object into a dict
ezsignfolder_duplicate_v1_response_dict = ezsignfolder_duplicate_v1_response_instance.to_dict()
# create an instance of EzsignfolderDuplicateV1Response from a dict
ezsignfolder_duplicate_v1_response_from_dict = EzsignfolderDuplicateV1Response.from_dict(ezsignfolder_duplicate_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


