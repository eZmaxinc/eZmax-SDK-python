# CustomContactNameResponse

A Custom ContactName Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_contact_firstname** | **str** | The First name of the contact | [optional] 
**s_contact_lastname** | **str** | The Last name of the contact | [optional] 
**s_contact_company** | **str** | The Company name of the contact | [optional] 

## Example

```python
from eZmaxApi.models.custom_contact_name_response import CustomContactNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomContactNameResponse from a JSON string
custom_contact_name_response_instance = CustomContactNameResponse.from_json(json)
# print the JSON string representation of the object
print(CustomContactNameResponse.to_json())

# convert the object into a dict
custom_contact_name_response_dict = custom_contact_name_response_instance.to_dict()
# create an instance of CustomContactNameResponse from a dict
custom_contact_name_response_from_dict = CustomContactNameResponse.from_dict(custom_contact_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


