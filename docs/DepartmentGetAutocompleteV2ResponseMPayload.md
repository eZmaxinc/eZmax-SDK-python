# DepartmentGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/department/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_department** | [**List[DepartmentAutocompleteElementResponse]**](DepartmentAutocompleteElementResponse.md) | An array of Department autocomplete element response. | 

## Example

```python
from eZmaxApi.models.department_get_autocomplete_v2_response_m_payload import DepartmentGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentGetAutocompleteV2ResponseMPayload from a JSON string
department_get_autocomplete_v2_response_m_payload_instance = DepartmentGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DepartmentGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
department_get_autocomplete_v2_response_m_payload_dict = department_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of DepartmentGetAutocompleteV2ResponseMPayload from a dict
department_get_autocomplete_v2_response_m_payload_form_dict = department_get_autocomplete_v2_response_m_payload.from_dict(department_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


