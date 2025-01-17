# PaymenttermCreateObjectV1Response

Response for POST /1/object/paymentterm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**PaymenttermCreateObjectV1ResponseMPayload**](PaymenttermCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.paymentterm_create_object_v1_response import PaymenttermCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymenttermCreateObjectV1Response from a JSON string
paymentterm_create_object_v1_response_instance = PaymenttermCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(PaymenttermCreateObjectV1Response.to_json())

# convert the object into a dict
paymentterm_create_object_v1_response_dict = paymentterm_create_object_v1_response_instance.to_dict()
# create an instance of PaymenttermCreateObjectV1Response from a dict
paymentterm_create_object_v1_response_from_dict = PaymenttermCreateObjectV1Response.from_dict(paymentterm_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


