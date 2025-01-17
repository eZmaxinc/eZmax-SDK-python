# ApikeyGenerateDelegatedCredentialsV1Response

Response for POST /1/object/apikey/generateDelegatedCredentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**ApikeyGenerateDelegatedCredentialsV1ResponseMPayload**](ApikeyGenerateDelegatedCredentialsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.apikey_generate_delegated_credentials_v1_response import ApikeyGenerateDelegatedCredentialsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyGenerateDelegatedCredentialsV1Response from a JSON string
apikey_generate_delegated_credentials_v1_response_instance = ApikeyGenerateDelegatedCredentialsV1Response.from_json(json)
# print the JSON string representation of the object
print(ApikeyGenerateDelegatedCredentialsV1Response.to_json())

# convert the object into a dict
apikey_generate_delegated_credentials_v1_response_dict = apikey_generate_delegated_credentials_v1_response_instance.to_dict()
# create an instance of ApikeyGenerateDelegatedCredentialsV1Response from a dict
apikey_generate_delegated_credentials_v1_response_from_dict = ApikeyGenerateDelegatedCredentialsV1Response.from_dict(apikey_generate_delegated_credentials_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


