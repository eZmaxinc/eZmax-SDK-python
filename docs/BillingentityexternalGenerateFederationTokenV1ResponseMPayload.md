# BillingentityexternalGenerateFederationTokenV1ResponseMPayload

Payload for POST /1/object/billingentityexternal/{pkiBillingentityexternalID}/generateFederationToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_apikeyfederation** | [**CustomApikeyfederation**](CustomApikeyfederation.md) |  | 
**s_ezmaxcustomercode_url** | **str** | The url of the server the Ezmaxcustomer is located | 

## Example

```python
from eZmaxApi.models.billingentityexternal_generate_federation_token_v1_response_m_payload import BillingentityexternalGenerateFederationTokenV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityexternalGenerateFederationTokenV1ResponseMPayload from a JSON string
billingentityexternal_generate_federation_token_v1_response_m_payload_instance = BillingentityexternalGenerateFederationTokenV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BillingentityexternalGenerateFederationTokenV1ResponseMPayload.to_json())

# convert the object into a dict
billingentityexternal_generate_federation_token_v1_response_m_payload_dict = billingentityexternal_generate_federation_token_v1_response_m_payload_instance.to_dict()
# create an instance of BillingentityexternalGenerateFederationTokenV1ResponseMPayload from a dict
billingentityexternal_generate_federation_token_v1_response_m_payload_from_dict = BillingentityexternalGenerateFederationTokenV1ResponseMPayload.from_dict(billingentityexternal_generate_federation_token_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


