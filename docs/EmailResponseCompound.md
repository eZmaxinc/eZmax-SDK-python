# EmailResponseCompound

An Email Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_email_id** | **int** | The unique ID of the Email | 
**fki_emailtype_id** | **int** | The unique ID of the Emailtype.  Valid values:  |Value|Description| |-|-| |1|Office| |2|Home| | 
**s_email_address** | **str** | The email address. | 

## Example

```python
from eZmaxApi.models.email_response_compound import EmailResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EmailResponseCompound from a JSON string
email_response_compound_instance = EmailResponseCompound.from_json(json)
# print the JSON string representation of the object
print EmailResponseCompound.to_json()

# convert the object into a dict
email_response_compound_dict = email_response_compound_instance.to_dict()
# create an instance of EmailResponseCompound from a dict
email_response_compound_form_dict = email_response_compound.from_dict(email_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


