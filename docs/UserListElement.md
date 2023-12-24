# UserListElement

A User List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_user_id** | **int** | The unique ID of the User | 
**s_user_firstname** | **str** | The first name of the user | 
**s_user_lastname** | **str** | The last name of the user | 
**s_user_loginname** | **str** | The login name of the User. | 
**b_user_isactive** | **bool** | Whether the User is active or not | 
**e_user_type** | [**FieldEUserType**](FieldEUserType.md) |  | 
**e_user_origin** | [**FieldEUserOrigin**](FieldEUserOrigin.md) |  | 
**e_user_ezsignaccess** | [**FieldEUserEzsignaccess**](FieldEUserEzsignaccess.md) |  | 
**dt_user_ezsignprepaidexpiration** | **str** | The eZsign prepaid expiration date | [optional] 
**s_email_address** | **str** | The email address. | 

## Example

```python
from eZmaxApi.models.user_list_element import UserListElement

# TODO update the JSON string below
json = "{}"
# create an instance of UserListElement from a JSON string
user_list_element_instance = UserListElement.from_json(json)
# print the JSON string representation of the object
print UserListElement.to_json()

# convert the object into a dict
user_list_element_dict = user_list_element_instance.to_dict()
# create an instance of UserListElement from a dict
user_list_element_form_dict = user_list_element.from_dict(user_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


