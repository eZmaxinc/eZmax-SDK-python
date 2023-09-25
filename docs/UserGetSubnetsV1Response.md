# UserGetSubnetsV1Response

Response for GET /1/object/user/{pkiUserID}/getSubnets

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UserGetSubnetsV1ResponseMPayload**](UserGetSubnetsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.user_get_subnets_v1_response import UserGetSubnetsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetSubnetsV1Response from a JSON string
user_get_subnets_v1_response_instance = UserGetSubnetsV1Response.from_json(json)
# print the JSON string representation of the object
print UserGetSubnetsV1Response.to_json()

# convert the object into a dict
user_get_subnets_v1_response_dict = user_get_subnets_v1_response_instance.to_dict()
# create an instance of UserGetSubnetsV1Response from a dict
user_get_subnets_v1_response_form_dict = user_get_subnets_v1_response.from_dict(user_get_subnets_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


