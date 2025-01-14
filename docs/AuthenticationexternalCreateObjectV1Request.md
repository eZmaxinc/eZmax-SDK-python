# AuthenticationexternalCreateObjectV1Request

Request for POST /1/object/authenticationexternal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_authenticationexternal** | [**List[AuthenticationexternalRequestCompound]**](AuthenticationexternalRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.authenticationexternal_create_object_v1_request import AuthenticationexternalCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalCreateObjectV1Request from a JSON string
authenticationexternal_create_object_v1_request_instance = AuthenticationexternalCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalCreateObjectV1Request.to_json())

# convert the object into a dict
authenticationexternal_create_object_v1_request_dict = authenticationexternal_create_object_v1_request_instance.to_dict()
# create an instance of AuthenticationexternalCreateObjectV1Request from a dict
authenticationexternal_create_object_v1_request_from_dict = AuthenticationexternalCreateObjectV1Request.from_dict(authenticationexternal_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


