# DepartmentGetAutocompleteV2Response

Response for GET /2/object/department/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**DepartmentGetAutocompleteV2ResponseMPayload**](DepartmentGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.department_get_autocomplete_v2_response import DepartmentGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentGetAutocompleteV2Response from a JSON string
department_get_autocomplete_v2_response_instance = DepartmentGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(DepartmentGetAutocompleteV2Response.to_json())

# convert the object into a dict
department_get_autocomplete_v2_response_dict = department_get_autocomplete_v2_response_instance.to_dict()
# create an instance of DepartmentGetAutocompleteV2Response from a dict
department_get_autocomplete_v2_response_from_dict = DepartmentGetAutocompleteV2Response.from_dict(department_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


