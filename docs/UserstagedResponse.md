# UserstagedResponse

A Userstaged Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_userstaged_id** | **int** | The unique ID of the Userstaged | 
**fki_email_id** | **int** | The unique ID of the Email | 
**s_email_address** | **str** | The email address. | 
**s_userstaged_firstname** | **str** | The firstname of the Userstaged | 
**s_userstaged_lastname** | **str** | The lastname of the Userstaged | 
**s_userstaged_externalid** | **str** | The externalid of the Userstaged | 

## Example

```python
from eZmaxApi.models.userstaged_response import UserstagedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserstagedResponse from a JSON string
userstaged_response_instance = UserstagedResponse.from_json(json)
# print the JSON string representation of the object
print UserstagedResponse.to_json()

# convert the object into a dict
userstaged_response_dict = userstaged_response_instance.to_dict()
# create an instance of UserstagedResponse from a dict
userstaged_response_form_dict = userstaged_response.from_dict(userstaged_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


