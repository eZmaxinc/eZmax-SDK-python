# CustomEzsignfoldertransmissionSignerResponse

A form Signer Object in the context of an Ezsignfoldertransmissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**s_contact_firstname** | **str** | The First name of the contact | 
**s_contact_lastname** | **str** | The Last name of the contact | 

## Example

```python
from eZmaxApi.models.custom_ezsignfoldertransmission_signer_response import CustomEzsignfoldertransmissionSignerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignfoldertransmissionSignerResponse from a JSON string
custom_ezsignfoldertransmission_signer_response_instance = CustomEzsignfoldertransmissionSignerResponse.from_json(json)
# print the JSON string representation of the object
print(CustomEzsignfoldertransmissionSignerResponse.to_json())

# convert the object into a dict
custom_ezsignfoldertransmission_signer_response_dict = custom_ezsignfoldertransmission_signer_response_instance.to_dict()
# create an instance of CustomEzsignfoldertransmissionSignerResponse from a dict
custom_ezsignfoldertransmission_signer_response_from_dict = CustomEzsignfoldertransmissionSignerResponse.from_dict(custom_ezsignfoldertransmission_signer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


