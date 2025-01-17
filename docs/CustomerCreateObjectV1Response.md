# CustomerCreateObjectV1Response

Response for POST /1/object/customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CustomerCreateObjectV1ResponseMPayload**](CustomerCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.customer_create_object_v1_response import CustomerCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerCreateObjectV1Response from a JSON string
customer_create_object_v1_response_instance = CustomerCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(CustomerCreateObjectV1Response.to_json())

# convert the object into a dict
customer_create_object_v1_response_dict = customer_create_object_v1_response_instance.to_dict()
# create an instance of CustomerCreateObjectV1Response from a dict
customer_create_object_v1_response_from_dict = CustomerCreateObjectV1Response.from_dict(customer_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


