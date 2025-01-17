# AuthenticationexternalGetListV1Response

Response for GET /1/object/authenticationexternal/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**AuthenticationexternalGetListV1ResponseMPayload**](AuthenticationexternalGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.authenticationexternal_get_list_v1_response import AuthenticationexternalGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalGetListV1Response from a JSON string
authenticationexternal_get_list_v1_response_instance = AuthenticationexternalGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalGetListV1Response.to_json())

# convert the object into a dict
authenticationexternal_get_list_v1_response_dict = authenticationexternal_get_list_v1_response_instance.to_dict()
# create an instance of AuthenticationexternalGetListV1Response from a dict
authenticationexternal_get_list_v1_response_from_dict = AuthenticationexternalGetListV1Response.from_dict(authenticationexternal_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


