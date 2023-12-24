# ModulegroupGetAllV1Response

Response for GET /1/object/modulegroup/getAll

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ModulegroupGetAllV1ResponseMPayload**](ModulegroupGetAllV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.modulegroup_get_all_v1_response import ModulegroupGetAllV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ModulegroupGetAllV1Response from a JSON string
modulegroup_get_all_v1_response_instance = ModulegroupGetAllV1Response.from_json(json)
# print the JSON string representation of the object
print ModulegroupGetAllV1Response.to_json()

# convert the object into a dict
modulegroup_get_all_v1_response_dict = modulegroup_get_all_v1_response_instance.to_dict()
# create an instance of ModulegroupGetAllV1Response from a dict
modulegroup_get_all_v1_response_form_dict = modulegroup_get_all_v1_response.from_dict(modulegroup_get_all_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


