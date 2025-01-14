# ActivesessionGenerateFederationTokenV1Request

Request for POST /1/object/activesession/generateFederationToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fks_ezmaxcustomer_code** | **str** | The Ezmaxcustomer code | 

## Example

```python
from eZmaxApi.models.activesession_generate_federation_token_v1_request import ActivesessionGenerateFederationTokenV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of ActivesessionGenerateFederationTokenV1Request from a JSON string
activesession_generate_federation_token_v1_request_instance = ActivesessionGenerateFederationTokenV1Request.from_json(json)
# print the JSON string representation of the object
print(ActivesessionGenerateFederationTokenV1Request.to_json())

# convert the object into a dict
activesession_generate_federation_token_v1_request_dict = activesession_generate_federation_token_v1_request_instance.to_dict()
# create an instance of ActivesessionGenerateFederationTokenV1Request from a dict
activesession_generate_federation_token_v1_request_from_dict = ActivesessionGenerateFederationTokenV1Request.from_dict(activesession_generate_federation_token_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


