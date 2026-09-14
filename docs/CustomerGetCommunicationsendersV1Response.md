# CustomerGetCommunicationsendersV1Response

Response for GET /1/object/customer/{pkiCustomerID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CustomerGetCommunicationsendersV1ResponseMPayload**](CustomerGetCommunicationsendersV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.customer_get_communicationsenders_v1_response import CustomerGetCommunicationsendersV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetCommunicationsendersV1Response from a JSON string
customer_get_communicationsenders_v1_response_instance = CustomerGetCommunicationsendersV1Response.from_json(json)
# print the JSON string representation of the object
print(CustomerGetCommunicationsendersV1Response.to_json())

# convert the object into a dict
customer_get_communicationsenders_v1_response_dict = customer_get_communicationsenders_v1_response_instance.to_dict()
# create an instance of CustomerGetCommunicationsendersV1Response from a dict
customer_get_communicationsenders_v1_response_from_dict = CustomerGetCommunicationsendersV1Response.from_dict(customer_get_communicationsenders_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


