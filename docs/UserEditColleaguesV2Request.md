# UserEditColleaguesV2Request

Request for PUT /2/object/user/{pkiUserID}/editColleagues

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_colleague** | [**List[ColleagueRequestCompoundV2]**](ColleagueRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.user_edit_colleagues_v2_request import UserEditColleaguesV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of UserEditColleaguesV2Request from a JSON string
user_edit_colleagues_v2_request_instance = UserEditColleaguesV2Request.from_json(json)
# print the JSON string representation of the object
print(UserEditColleaguesV2Request.to_json())

# convert the object into a dict
user_edit_colleagues_v2_request_dict = user_edit_colleagues_v2_request_instance.to_dict()
# create an instance of UserEditColleaguesV2Request from a dict
user_edit_colleagues_v2_request_from_dict = UserEditColleaguesV2Request.from_dict(user_edit_colleagues_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


