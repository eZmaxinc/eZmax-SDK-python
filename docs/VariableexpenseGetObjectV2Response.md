# VariableexpenseGetObjectV2Response

Response for GET /2/object/variableexpense/{pkiVariableexpenseID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**VariableexpenseGetObjectV2ResponseMPayload**](VariableexpenseGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.variableexpense_get_object_v2_response import VariableexpenseGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of VariableexpenseGetObjectV2Response from a JSON string
variableexpense_get_object_v2_response_instance = VariableexpenseGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print VariableexpenseGetObjectV2Response.to_json()

# convert the object into a dict
variableexpense_get_object_v2_response_dict = variableexpense_get_object_v2_response_instance.to_dict()
# create an instance of VariableexpenseGetObjectV2Response from a dict
variableexpense_get_object_v2_response_form_dict = variableexpense_get_object_v2_response.from_dict(variableexpense_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


