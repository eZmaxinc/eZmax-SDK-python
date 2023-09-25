# EmailstaticResponse

An Emailstatic Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_emailstatic_id** | **int** | The unique ID of the Emailstatic | 
**s_emailstatic_address** | **str** | The email address. | 

## Example

```python
from eZmaxApi.models.emailstatic_response import EmailstaticResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailstaticResponse from a JSON string
emailstatic_response_instance = EmailstaticResponse.from_json(json)
# print the JSON string representation of the object
print EmailstaticResponse.to_json()

# convert the object into a dict
emailstatic_response_dict = emailstatic_response_instance.to_dict()
# create an instance of EmailstaticResponse from a dict
emailstatic_response_form_dict = emailstatic_response.from_dict(emailstatic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


