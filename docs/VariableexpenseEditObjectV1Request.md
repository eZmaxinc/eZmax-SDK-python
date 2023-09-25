# VariableexpenseEditObjectV1Request

Request for PUT /1/object/variableexpense/{pkiVariableexpenseID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_variableexpense** | [**VariableexpenseRequestCompound**](VariableexpenseRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.variableexpense_edit_object_v1_request import VariableexpenseEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of VariableexpenseEditObjectV1Request from a JSON string
variableexpense_edit_object_v1_request_instance = VariableexpenseEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print VariableexpenseEditObjectV1Request.to_json()

# convert the object into a dict
variableexpense_edit_object_v1_request_dict = variableexpense_edit_object_v1_request_instance.to_dict()
# create an instance of VariableexpenseEditObjectV1Request from a dict
variableexpense_edit_object_v1_request_form_dict = variableexpense_edit_object_v1_request.from_dict(variableexpense_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


