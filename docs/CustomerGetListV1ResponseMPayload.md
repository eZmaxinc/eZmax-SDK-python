# CustomerGetListV1ResponseMPayload

Payload for GET /1/object/customer/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_row_returned** | **int** | The number of rows returned | 
**i_row_filtered** | **int** | The number of rows matching your filters (if any) or the total number of rows | 
**a_obj_customer** | [**List[CustomerListElement]**](CustomerListElement.md) |  | 

## Example

```python
from eZmaxApi.models.customer_get_list_v1_response_m_payload import CustomerGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetListV1ResponseMPayload from a JSON string
customer_get_list_v1_response_m_payload_instance = CustomerGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CustomerGetListV1ResponseMPayload.to_json())

# convert the object into a dict
customer_get_list_v1_response_m_payload_dict = customer_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of CustomerGetListV1ResponseMPayload from a dict
customer_get_list_v1_response_m_payload_from_dict = CustomerGetListV1ResponseMPayload.from_dict(customer_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


