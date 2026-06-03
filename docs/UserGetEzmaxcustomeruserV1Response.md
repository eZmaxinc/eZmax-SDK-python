# UserGetEzmaxcustomeruserV1Response

Response for GET /1/object/user/getEzmaxcustomeruser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UserGetEzmaxcustomeruserV1ResponseMPayload**](UserGetEzmaxcustomeruserV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.user_get_ezmaxcustomeruser_v1_response import UserGetEzmaxcustomeruserV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetEzmaxcustomeruserV1Response from a JSON string
user_get_ezmaxcustomeruser_v1_response_instance = UserGetEzmaxcustomeruserV1Response.from_json(json)
# print the JSON string representation of the object
print(UserGetEzmaxcustomeruserV1Response.to_json())

# convert the object into a dict
user_get_ezmaxcustomeruser_v1_response_dict = user_get_ezmaxcustomeruser_v1_response_instance.to_dict()
# create an instance of UserGetEzmaxcustomeruserV1Response from a dict
user_get_ezmaxcustomeruser_v1_response_from_dict = UserGetEzmaxcustomeruserV1Response.from_dict(user_get_ezmaxcustomeruser_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


