# EzsignsignergroupmembershipResponseCompound

A Ezsignsignergroupmembership Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignsignergroupmembership_id** | **int** | The unique ID of the Ezsignsignergroupmembership | 
**fki_ezsignsignergroup_id** | **int** | The unique ID of the Ezsignsignergroup | 
**fki_ezsignsigner_id** | **int** | The unique ID of the Ezsignsigner | [optional] 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | [optional] 

## Example

```python
from eZmaxApi.models.ezsignsignergroupmembership_response_compound import EzsignsignergroupmembershipResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupmembershipResponseCompound from a JSON string
ezsignsignergroupmembership_response_compound_instance = EzsignsignergroupmembershipResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignsignergroupmembershipResponseCompound.to_json())

# convert the object into a dict
ezsignsignergroupmembership_response_compound_dict = ezsignsignergroupmembership_response_compound_instance.to_dict()
# create an instance of EzsignsignergroupmembershipResponseCompound from a dict
ezsignsignergroupmembership_response_compound_from_dict = EzsignsignergroupmembershipResponseCompound.from_dict(ezsignsignergroupmembership_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


