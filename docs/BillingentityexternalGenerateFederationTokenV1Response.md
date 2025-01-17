# BillingentityexternalGenerateFederationTokenV1Response

Response for POST /1/object/billingentityexternal/{pkiBillingentityexternalID}/generateFederationToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BillingentityexternalGenerateFederationTokenV1ResponseMPayload**](BillingentityexternalGenerateFederationTokenV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.billingentityexternal_generate_federation_token_v1_response import BillingentityexternalGenerateFederationTokenV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BillingentityexternalGenerateFederationTokenV1Response from a JSON string
billingentityexternal_generate_federation_token_v1_response_instance = BillingentityexternalGenerateFederationTokenV1Response.from_json(json)
# print the JSON string representation of the object
print(BillingentityexternalGenerateFederationTokenV1Response.to_json())

# convert the object into a dict
billingentityexternal_generate_federation_token_v1_response_dict = billingentityexternal_generate_federation_token_v1_response_instance.to_dict()
# create an instance of BillingentityexternalGenerateFederationTokenV1Response from a dict
billingentityexternal_generate_federation_token_v1_response_from_dict = BillingentityexternalGenerateFederationTokenV1Response.from_dict(billingentityexternal_generate_federation_token_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


