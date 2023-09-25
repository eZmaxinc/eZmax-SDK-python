# EzsignsignergroupmembershipRequest

A Ezsignsignergroupmembership Object

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
from eZmaxApi.models.ezsignsignergroupmembership_request import EzsignsignergroupmembershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupmembershipRequest from a JSON string
ezsignsignergroupmembership_request_instance = EzsignsignergroupmembershipRequest.from_json(json)
# print the JSON string representation of the object
print EzsignsignergroupmembershipRequest.to_json()

# convert the object into a dict
ezsignsignergroupmembership_request_dict = ezsignsignergroupmembership_request_instance.to_dict()
# create an instance of EzsignsignergroupmembershipRequest from a dict
ezsignsignergroupmembership_request_form_dict = ezsignsignergroupmembership_request.from_dict(ezsignsignergroupmembership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


