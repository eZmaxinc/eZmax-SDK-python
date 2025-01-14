# BillingentityexternalGenerateFederationTokenV1Request

Request for POST /1/object/billingentityexternal/{pkiBillingentityexternalID}/generateFederationToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fks_ezmaxcustomer_code** | **str** | The Ezmaxcustomer code | 

## Example

```python
from eZmaxApi.models.billingentityexternal_generate_federation_token_v1_request import BillingentityexternalGenerateFederationTokenV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityexternalGenerateFederationTokenV1Request from a JSON string
billingentityexternal_generate_federation_token_v1_request_instance = BillingentityexternalGenerateFederationTokenV1Request.from_json(json)
# print the JSON string representation of the object
print(BillingentityexternalGenerateFederationTokenV1Request.to_json())

# convert the object into a dict
billingentityexternal_generate_federation_token_v1_request_dict = billingentityexternal_generate_federation_token_v1_request_instance.to_dict()
# create an instance of BillingentityexternalGenerateFederationTokenV1Request from a dict
billingentityexternal_generate_federation_token_v1_request_from_dict = BillingentityexternalGenerateFederationTokenV1Request.from_dict(billingentityexternal_generate_federation_token_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


