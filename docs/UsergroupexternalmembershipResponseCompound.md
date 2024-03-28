# UsergroupexternalmembershipResponseCompound

A Usergroupexternalmembership Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_usergroupexternalmembership_id** | **int** | The unique ID of the Usergroupexternalmembership | 
**fki_usergroupexternal_id** | **int** | The unique ID of the Usergroupexternal | 
**fki_user_id** | **int** | The unique ID of the User | 
**s_user_firstname** | **str** | The first name of the user | 
**s_user_lastname** | **str** | The last name of the user | 
**s_user_loginname** | **str** | The login name of the User. | 
**s_email_address** | **str** | The email address. | 
**s_usergroupexternal_name** | **str** | The name of the Usergroupexternal | 

## Example

```python
from eZmaxApi.models.usergroupexternalmembership_response_compound import UsergroupexternalmembershipResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalmembershipResponseCompound from a JSON string
usergroupexternalmembership_response_compound_instance = UsergroupexternalmembershipResponseCompound.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalmembershipResponseCompound.to_json())

# convert the object into a dict
usergroupexternalmembership_response_compound_dict = usergroupexternalmembership_response_compound_instance.to_dict()
# create an instance of UsergroupexternalmembershipResponseCompound from a dict
usergroupexternalmembership_response_compound_form_dict = usergroupexternalmembership_response_compound.from_dict(usergroupexternalmembership_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


