# EzsignfolderGetListV1Response

Response for GET /1/object/ezsignfolder/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfolderGetListV1ResponseMPayload**](EzsignfolderGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_list_v1_response import EzsignfolderGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetListV1Response from a JSON string
ezsignfolder_get_list_v1_response_instance = EzsignfolderGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetListV1Response.to_json())

# convert the object into a dict
ezsignfolder_get_list_v1_response_dict = ezsignfolder_get_list_v1_response_instance.to_dict()
# create an instance of EzsignfolderGetListV1Response from a dict
ezsignfolder_get_list_v1_response_from_dict = EzsignfolderGetListV1Response.from_dict(ezsignfolder_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


