# EmailResponse

An Email Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_email_id** | **int** | The unique ID of the Email | 
**fki_emailtype_id** | **int** | The unique ID of the Emailtype.  Valid values:  |Value|Description| |-|-| |1|Office| |2|Home| | 
**s_email_address** | **str** | The email address. | 

## Example

```python
from eZmaxApi.models.email_response import EmailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailResponse from a JSON string
email_response_instance = EmailResponse.from_json(json)
# print the JSON string representation of the object
print(EmailResponse.to_json())

# convert the object into a dict
email_response_dict = email_response_instance.to_dict()
# create an instance of EmailResponse from a dict
email_response_from_dict = EmailResponse.from_dict(email_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


