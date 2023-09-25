# ActivesessionResponseCompoundUser

An Activesession->User Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_user_id** | **int** | The unique ID of the User | 
**fki_timezone_id** | **int** | The unique ID of the Timezone | 
**s_avatar_url** | **str** | The url of the picture used as avatar | 
**s_user_firstname** | **str** | The first name of the user | 
**s_user_lastname** | **str** | The last name of the user | 
**s_email_address** | **str** | The email address. | 
**e_user_ezsignsendreminderfrequency** | [**FieldEUserEzsignsendreminderfrequency**](FieldEUserEzsignsendreminderfrequency.md) |  | 
**i_user_interfacecolor** | **int** | The int32 representation of the interface color. For example, RGB color #39435B would be 3752795 | 
**b_user_interfacedark** | **bool** | Whether to use a dark mode interface | 
**i_user_listresult** | **int** | The number of rows to return by default in lists | 

## Example

```python
from eZmaxApi.models.activesession_response_compound_user import ActivesessionResponseCompoundUser

# TODO update the JSON string below
json = "{}"
# create an instance of ActivesessionResponseCompoundUser from a JSON string
activesession_response_compound_user_instance = ActivesessionResponseCompoundUser.from_json(json)
# print the JSON string representation of the object
print ActivesessionResponseCompoundUser.to_json()

# convert the object into a dict
activesession_response_compound_user_dict = activesession_response_compound_user_instance.to_dict()
# create an instance of ActivesessionResponseCompoundUser from a dict
activesession_response_compound_user_form_dict = activesession_response_compound_user.from_dict(activesession_response_compound_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


