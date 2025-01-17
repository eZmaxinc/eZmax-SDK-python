# ActivesessionGenerateFederationTokenV1Response

Response for POST /1/object/activesession/generateFederationToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**ActivesessionGenerateFederationTokenV1ResponseMPayload**](ActivesessionGenerateFederationTokenV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.activesession_generate_federation_token_v1_response import ActivesessionGenerateFederationTokenV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActivesessionGenerateFederationTokenV1Response from a JSON string
activesession_generate_federation_token_v1_response_instance = ActivesessionGenerateFederationTokenV1Response.from_json(json)
# print the JSON string representation of the object
print(ActivesessionGenerateFederationTokenV1Response.to_json())

# convert the object into a dict
activesession_generate_federation_token_v1_response_dict = activesession_generate_federation_token_v1_response_instance.to_dict()
# create an instance of ActivesessionGenerateFederationTokenV1Response from a dict
activesession_generate_federation_token_v1_response_from_dict = ActivesessionGenerateFederationTokenV1Response.from_dict(activesession_generate_federation_token_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


