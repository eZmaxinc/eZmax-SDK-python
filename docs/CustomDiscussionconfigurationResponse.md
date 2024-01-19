# CustomDiscussionconfigurationResponse

A Custom Discussionconfiguration Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_discussionconfiguration_completehistorywhenadded** | **bool** | If the added Discussionmembership will have access to the entire history or not | 
**b_discussionconfiguration_createallowed** | **bool** | If the the creation of the Discussion is allowed or not | 
**b_discussionconfiguration_deleteallowed** | **bool** | If the the destruction of the Discussion is allowed or not | 
**b_discussionconfiguration_deletediscussionmessageallowed** | **bool** | If the the destruction of the Discussionmessage is allowed or not | 
**b_discussionconfiguration_editdiscussionmessageallowed** | **bool** | If the the creation of the Discussionmessage is allowed or not | 

## Example

```python
from eZmaxApi.models.custom_discussionconfiguration_response import CustomDiscussionconfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDiscussionconfigurationResponse from a JSON string
custom_discussionconfiguration_response_instance = CustomDiscussionconfigurationResponse.from_json(json)
# print the JSON string representation of the object
print CustomDiscussionconfigurationResponse.to_json()

# convert the object into a dict
custom_discussionconfiguration_response_dict = custom_discussionconfiguration_response_instance.to_dict()
# create an instance of CustomDiscussionconfigurationResponse from a dict
custom_discussionconfiguration_response_form_dict = custom_discussionconfiguration_response.from_dict(custom_discussionconfiguration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


