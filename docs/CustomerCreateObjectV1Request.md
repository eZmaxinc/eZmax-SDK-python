# CustomerCreateObjectV1Request

Request for POST /1/object/customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_customer** | [**List[CustomerRequestCompound]**](CustomerRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.customer_create_object_v1_request import CustomerCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerCreateObjectV1Request from a JSON string
customer_create_object_v1_request_instance = CustomerCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(CustomerCreateObjectV1Request.to_json())

# convert the object into a dict
customer_create_object_v1_request_dict = customer_create_object_v1_request_instance.to_dict()
# create an instance of CustomerCreateObjectV1Request from a dict
customer_create_object_v1_request_from_dict = CustomerCreateObjectV1Request.from_dict(customer_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


