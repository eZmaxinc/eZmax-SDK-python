# EmailstaticResponseCompound

An Emailstatic Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_emailstatic_id** | **int** | The unique ID of the Emailstatic | 
**s_emailstatic_address** | **str** | The email address. | 

## Example

```python
from eZmaxApi.models.emailstatic_response_compound import EmailstaticResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EmailstaticResponseCompound from a JSON string
emailstatic_response_compound_instance = EmailstaticResponseCompound.from_json(json)
# print the JSON string representation of the object
print EmailstaticResponseCompound.to_json()

# convert the object into a dict
emailstatic_response_compound_dict = emailstatic_response_compound_instance.to_dict()
# create an instance of EmailstaticResponseCompound from a dict
emailstatic_response_compound_form_dict = emailstatic_response_compound.from_dict(emailstatic_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


