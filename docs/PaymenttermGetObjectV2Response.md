# PaymenttermGetObjectV2Response

Response for GET /2/object/paymentterm/{pkiPaymenttermID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**PaymenttermGetObjectV2ResponseMPayload**](PaymenttermGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.paymentterm_get_object_v2_response import PaymenttermGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymenttermGetObjectV2Response from a JSON string
paymentterm_get_object_v2_response_instance = PaymenttermGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(PaymenttermGetObjectV2Response.to_json())

# convert the object into a dict
paymentterm_get_object_v2_response_dict = paymentterm_get_object_v2_response_instance.to_dict()
# create an instance of PaymenttermGetObjectV2Response from a dict
paymentterm_get_object_v2_response_from_dict = PaymenttermGetObjectV2Response.from_dict(paymentterm_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


