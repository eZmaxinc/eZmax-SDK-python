# ApikeyGenerateDelegatedCredentialsV1Request

Request for POST /1/object/apikey/generateDelegatedCredentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_expiration_minutes** | **int** | The number of minute before key is no longer active | 

## Example

```python
from eZmaxApi.models.apikey_generate_delegated_credentials_v1_request import ApikeyGenerateDelegatedCredentialsV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyGenerateDelegatedCredentialsV1Request from a JSON string
apikey_generate_delegated_credentials_v1_request_instance = ApikeyGenerateDelegatedCredentialsV1Request.from_json(json)
# print the JSON string representation of the object
print(ApikeyGenerateDelegatedCredentialsV1Request.to_json())

# convert the object into a dict
apikey_generate_delegated_credentials_v1_request_dict = apikey_generate_delegated_credentials_v1_request_instance.to_dict()
# create an instance of ApikeyGenerateDelegatedCredentialsV1Request from a dict
apikey_generate_delegated_credentials_v1_request_from_dict = ApikeyGenerateDelegatedCredentialsV1Request.from_dict(apikey_generate_delegated_credentials_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


