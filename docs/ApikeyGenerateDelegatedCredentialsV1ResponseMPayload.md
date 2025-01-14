# ApikeyGenerateDelegatedCredentialsV1ResponseMPayload

Payload for POST /1/object/apikey/generateDelegatedCredentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_apikey** | [**CustomApikey**](CustomApikey.md) |  | 

## Example

```python
from eZmaxApi.models.apikey_generate_delegated_credentials_v1_response_m_payload import ApikeyGenerateDelegatedCredentialsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyGenerateDelegatedCredentialsV1ResponseMPayload from a JSON string
apikey_generate_delegated_credentials_v1_response_m_payload_instance = ApikeyGenerateDelegatedCredentialsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ApikeyGenerateDelegatedCredentialsV1ResponseMPayload.to_json())

# convert the object into a dict
apikey_generate_delegated_credentials_v1_response_m_payload_dict = apikey_generate_delegated_credentials_v1_response_m_payload_instance.to_dict()
# create an instance of ApikeyGenerateDelegatedCredentialsV1ResponseMPayload from a dict
apikey_generate_delegated_credentials_v1_response_m_payload_from_dict = ApikeyGenerateDelegatedCredentialsV1ResponseMPayload.from_dict(apikey_generate_delegated_credentials_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


