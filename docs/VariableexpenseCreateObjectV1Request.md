# VariableexpenseCreateObjectV1Request

Request for POST /1/object/variableexpense

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_variableexpense** | [**List[VariableexpenseRequestCompound]**](VariableexpenseRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.variableexpense_create_object_v1_request import VariableexpenseCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of VariableexpenseCreateObjectV1Request from a JSON string
variableexpense_create_object_v1_request_instance = VariableexpenseCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(VariableexpenseCreateObjectV1Request.to_json())

# convert the object into a dict
variableexpense_create_object_v1_request_dict = variableexpense_create_object_v1_request_instance.to_dict()
# create an instance of VariableexpenseCreateObjectV1Request from a dict
variableexpense_create_object_v1_request_from_dict = VariableexpenseCreateObjectV1Request.from_dict(variableexpense_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


