# CustomEzsignfolderezsigntemplatepublicSignerResponse

A form Signer Object in the context of an Ezsignfoldertransmissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_ezsignsignergroup_id** | **int** | The unique ID of the Ezsignsignergroup | [optional] 
**s_contact_firstname** | **str** | The First name of the contact | [optional] 
**s_contact_lastname** | **str** | The Last name of the contact | [optional] 
**s_ezsignsignergroup_description_x** | **str** | The Description of the Ezsignsignergroup in the language of the requester | [optional] 

## Example

```python
from eZmaxApi.models.custom_ezsignfolderezsigntemplatepublic_signer_response import CustomEzsignfolderezsigntemplatepublicSignerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignfolderezsigntemplatepublicSignerResponse from a JSON string
custom_ezsignfolderezsigntemplatepublic_signer_response_instance = CustomEzsignfolderezsigntemplatepublicSignerResponse.from_json(json)
# print the JSON string representation of the object
print(CustomEzsignfolderezsigntemplatepublicSignerResponse.to_json())

# convert the object into a dict
custom_ezsignfolderezsigntemplatepublic_signer_response_dict = custom_ezsignfolderezsigntemplatepublic_signer_response_instance.to_dict()
# create an instance of CustomEzsignfolderezsigntemplatepublicSignerResponse from a dict
custom_ezsignfolderezsigntemplatepublic_signer_response_from_dict = CustomEzsignfolderezsigntemplatepublicSignerResponse.from_dict(custom_ezsignfolderezsigntemplatepublic_signer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


