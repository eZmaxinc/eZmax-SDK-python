# UserCreateEzsignuserV1Request

Request for POST /1/module/user/createEzsignuser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_user_firstname** | **str** | The first name of the user | 
**s_user_lastname** | **str** | The last name of the user | 
**s_email_address** | **str** | The email address. | 
**s_phone_region** | **str** | The region of the phone number. (For a North America Number only)  The region is the \&quot;514\&quot; section in this sample phone number: (514) 990-1516 x123 | 
**s_phone_exchange** | **str** | The exchange of the phone number. (For a North America Number only)  The exchange is the \&quot;990\&quot; section in this sample phone number: (514) 990-1516 x123 | 
**s_phone_number** | **str** | The number of the phone number. (For a North America Number only)  The number is the \&quot;1516\&quot; section in this sample phone number: (514) 990-1516 x123 | 
**s_phone_extension** | **str** | The extension of the phone number.  The extension is the \&quot;123\&quot; section in this sample phone number: (514) 990-1516 x123.  It can also be used with international phone numbers | [optional] 

## Example

```python
from eZmaxApi.models.user_create_ezsignuser_v1_request import UserCreateEzsignuserV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateEzsignuserV1Request from a JSON string
user_create_ezsignuser_v1_request_instance = UserCreateEzsignuserV1Request.from_json(json)
# print the JSON string representation of the object
print UserCreateEzsignuserV1Request.to_json()

# convert the object into a dict
user_create_ezsignuser_v1_request_dict = user_create_ezsignuser_v1_request_instance.to_dict()
# create an instance of UserCreateEzsignuserV1Request from a dict
user_create_ezsignuser_v1_request_form_dict = user_create_ezsignuser_v1_request.from_dict(user_create_ezsignuser_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


