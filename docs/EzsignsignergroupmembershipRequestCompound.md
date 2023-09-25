# EzsignsignergroupmembershipRequestCompound

A Ezsignsignergroupmembership Object and children

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignsignergroupmembership_id** | **int** | The unique ID of the Ezsignsignergroupmembership | [optional] 
**fki_ezsignsignergroup_id** | **int** | The unique ID of the Ezsignsignergroup | 
**fki_ezsignsigner_id** | **int** | The unique ID of the Ezsignsigner | [optional] 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | [optional] 

## Example

```python
from eZmaxApi.models.ezsignsignergroupmembership_request_compound import EzsignsignergroupmembershipRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupmembershipRequestCompound from a JSON string
ezsignsignergroupmembership_request_compound_instance = EzsignsignergroupmembershipRequestCompound.from_json(json)
# print the JSON string representation of the object
print EzsignsignergroupmembershipRequestCompound.to_json()

# convert the object into a dict
ezsignsignergroupmembership_request_compound_dict = ezsignsignergroupmembership_request_compound_instance.to_dict()
# create an instance of EzsignsignergroupmembershipRequestCompound from a dict
ezsignsignergroupmembership_request_compound_form_dict = ezsignsignergroupmembership_request_compound.from_dict(ezsignsignergroupmembership_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


