# AuthenticationexternalGetListV1ResponseMPayload

Payload for GET /1/object/authenticationexternal/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_authenticationexternal** | [**List[AuthenticationexternalListElement]**](AuthenticationexternalListElement.md) |  | 

## Example

```python
from eZmaxApi.models.authenticationexternal_get_list_v1_response_m_payload import AuthenticationexternalGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalGetListV1ResponseMPayload from a JSON string
authenticationexternal_get_list_v1_response_m_payload_instance = AuthenticationexternalGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalGetListV1ResponseMPayload.to_json())

# convert the object into a dict
authenticationexternal_get_list_v1_response_m_payload_dict = authenticationexternal_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of AuthenticationexternalGetListV1ResponseMPayload from a dict
authenticationexternal_get_list_v1_response_m_payload_from_dict = AuthenticationexternalGetListV1ResponseMPayload.from_dict(authenticationexternal_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


