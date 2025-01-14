# CustomerCreateObjectV1ResponseMPayload

Payload for POST /1/object/customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_customer_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.customer_create_object_v1_response_m_payload import CustomerCreateObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerCreateObjectV1ResponseMPayload from a JSON string
customer_create_object_v1_response_m_payload_instance = CustomerCreateObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CustomerCreateObjectV1ResponseMPayload.to_json())

# convert the object into a dict
customer_create_object_v1_response_m_payload_dict = customer_create_object_v1_response_m_payload_instance.to_dict()
# create an instance of CustomerCreateObjectV1ResponseMPayload from a dict
customer_create_object_v1_response_m_payload_from_dict = CustomerCreateObjectV1ResponseMPayload.from_dict(customer_create_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


