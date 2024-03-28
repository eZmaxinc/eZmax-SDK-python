# EzsignfoldertypeGetListV1Response

Response for GET /1/object/ezsignfoldertype/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfoldertypeGetListV1ResponseMPayload**](EzsignfoldertypeGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_get_list_v1_response import EzsignfoldertypeGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeGetListV1Response from a JSON string
ezsignfoldertype_get_list_v1_response_instance = EzsignfoldertypeGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeGetListV1Response.to_json())

# convert the object into a dict
ezsignfoldertype_get_list_v1_response_dict = ezsignfoldertype_get_list_v1_response_instance.to_dict()
# create an instance of EzsignfoldertypeGetListV1Response from a dict
ezsignfoldertype_get_list_v1_response_form_dict = ezsignfoldertype_get_list_v1_response.from_dict(ezsignfoldertype_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


