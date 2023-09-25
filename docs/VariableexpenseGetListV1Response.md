# VariableexpenseGetListV1Response

Response for GET /1/object/variableexpense/getList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**VariableexpenseGetListV1ResponseMPayload**](VariableexpenseGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.variableexpense_get_list_v1_response import VariableexpenseGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of VariableexpenseGetListV1Response from a JSON string
variableexpense_get_list_v1_response_instance = VariableexpenseGetListV1Response.from_json(json)
# print the JSON string representation of the object
print VariableexpenseGetListV1Response.to_json()

# convert the object into a dict
variableexpense_get_list_v1_response_dict = variableexpense_get_list_v1_response_instance.to_dict()
# create an instance of VariableexpenseGetListV1Response from a dict
variableexpense_get_list_v1_response_form_dict = variableexpense_get_list_v1_response.from_dict(variableexpense_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


