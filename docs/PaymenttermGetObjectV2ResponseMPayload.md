# PaymenttermGetObjectV2ResponseMPayload

Payload for GET /2/object/paymentterm/{pkiPaymenttermID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_paymentterm** | [**PaymenttermResponseCompound**](PaymenttermResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.paymentterm_get_object_v2_response_m_payload import PaymenttermGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PaymenttermGetObjectV2ResponseMPayload from a JSON string
paymentterm_get_object_v2_response_m_payload_instance = PaymenttermGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print PaymenttermGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
paymentterm_get_object_v2_response_m_payload_dict = paymentterm_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of PaymenttermGetObjectV2ResponseMPayload from a dict
paymentterm_get_object_v2_response_m_payload_form_dict = paymentterm_get_object_v2_response_m_payload.from_dict(paymentterm_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


