# CreditcardclientGetObjectV2ResponseMPayload

Payload for GET /2/object/creditcardclient/{pkiCreditcardclientID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_creditcardclient** | [**CreditcardclientResponseCompound**](CreditcardclientResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardclient_get_object_v2_response_m_payload import CreditcardclientGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardclientGetObjectV2ResponseMPayload from a JSON string
creditcardclient_get_object_v2_response_m_payload_instance = CreditcardclientGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CreditcardclientGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
creditcardclient_get_object_v2_response_m_payload_dict = creditcardclient_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of CreditcardclientGetObjectV2ResponseMPayload from a dict
creditcardclient_get_object_v2_response_m_payload_from_dict = CreditcardclientGetObjectV2ResponseMPayload.from_dict(creditcardclient_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


