# VariableexpenseEditObjectV1Response

Response for PUT /1/object/variableexpense/{pkiVariableexpenseID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.variableexpense_edit_object_v1_response import VariableexpenseEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of VariableexpenseEditObjectV1Response from a JSON string
variableexpense_edit_object_v1_response_instance = VariableexpenseEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(VariableexpenseEditObjectV1Response.to_json())

# convert the object into a dict
variableexpense_edit_object_v1_response_dict = variableexpense_edit_object_v1_response_instance.to_dict()
# create an instance of VariableexpenseEditObjectV1Response from a dict
variableexpense_edit_object_v1_response_from_dict = VariableexpenseEditObjectV1Response.from_dict(variableexpense_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


