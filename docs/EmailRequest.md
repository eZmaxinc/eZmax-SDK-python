# EmailRequest

An Email Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_email_id** | **int** | The unique ID of the Email | [optional] 
**fki_emailtype_id** | **int** | The unique ID of the Emailtype.  Valid values:  |Value|Description| |-|-| |1|Office| |2|Home| | 
**s_email_address** | **str** | The email address. | 

## Example

```python
from eZmaxApi.models.email_request import EmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailRequest from a JSON string
email_request_instance = EmailRequest.from_json(json)
# print the JSON string representation of the object
print EmailRequest.to_json()

# convert the object into a dict
email_request_dict = email_request_instance.to_dict()
# create an instance of EmailRequest from a dict
email_request_form_dict = email_request.from_dict(email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


