# CustomerGetObjectV2Response

Response for GET /2/object/customer/{pkiCustomerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**CustomerGetObjectV2ResponseMPayload**](CustomerGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.customer_get_object_v2_response import CustomerGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetObjectV2Response from a JSON string
customer_get_object_v2_response_instance = CustomerGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(CustomerGetObjectV2Response.to_json())

# convert the object into a dict
customer_get_object_v2_response_dict = customer_get_object_v2_response_instance.to_dict()
# create an instance of CustomerGetObjectV2Response from a dict
customer_get_object_v2_response_from_dict = CustomerGetObjectV2Response.from_dict(customer_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


