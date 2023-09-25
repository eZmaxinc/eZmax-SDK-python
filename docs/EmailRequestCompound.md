# EmailRequestCompound

An Email Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_email_id** | **int** | The unique ID of the Email | [optional] 
**fki_emailtype_id** | **int** | The unique ID of the Emailtype.  Valid values:  |Value|Description| |-|-| |1|Office| |2|Home| | 
**s_email_address** | **str** | The email address. | 

## Example

```python
from eZmaxApi.models.email_request_compound import EmailRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EmailRequestCompound from a JSON string
email_request_compound_instance = EmailRequestCompound.from_json(json)
# print the JSON string representation of the object
print EmailRequestCompound.to_json()

# convert the object into a dict
email_request_compound_dict = email_request_compound_instance.to_dict()
# create an instance of EmailRequestCompound from a dict
email_request_compound_form_dict = email_request_compound.from_dict(email_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


