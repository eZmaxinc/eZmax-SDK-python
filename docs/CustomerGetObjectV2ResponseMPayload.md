# CustomerGetObjectV2ResponseMPayload

Payload for GET /2/object/customer/{pkiCustomerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_customer** | [**CustomerResponseCompound**](CustomerResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.customer_get_object_v2_response_m_payload import CustomerGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetObjectV2ResponseMPayload from a JSON string
customer_get_object_v2_response_m_payload_instance = CustomerGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CustomerGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
customer_get_object_v2_response_m_payload_dict = customer_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of CustomerGetObjectV2ResponseMPayload from a dict
customer_get_object_v2_response_m_payload_from_dict = CustomerGetObjectV2ResponseMPayload.from_dict(customer_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


