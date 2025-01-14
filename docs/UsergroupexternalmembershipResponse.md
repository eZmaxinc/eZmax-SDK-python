# UsergroupexternalmembershipResponse

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
from eZmaxApi.models.usergroupexternalmembership_response import UsergroupexternalmembershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalmembershipResponse from a JSON string
usergroupexternalmembership_response_instance = UsergroupexternalmembershipResponse.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalmembershipResponse.to_json())

# convert the object into a dict
usergroupexternalmembership_response_dict = usergroupexternalmembership_response_instance.to_dict()
# create an instance of UsergroupexternalmembershipResponse from a dict
usergroupexternalmembership_response_from_dict = UsergroupexternalmembershipResponse.from_dict(usergroupexternalmembership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


