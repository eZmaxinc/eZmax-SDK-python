# CustomerImportIntoEDMV1Response

Response for POST /1/object/customer/{pkiCustomerID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CustomerImportIntoEDMV1ResponseMPayload**](CustomerImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.customer_import_into_edmv1_response import CustomerImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerImportIntoEDMV1Response from a JSON string
customer_import_into_edmv1_response_instance = CustomerImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(CustomerImportIntoEDMV1Response.to_json())

# convert the object into a dict
customer_import_into_edmv1_response_dict = customer_import_into_edmv1_response_instance.to_dict()
# create an instance of CustomerImportIntoEDMV1Response from a dict
customer_import_into_edmv1_response_from_dict = CustomerImportIntoEDMV1Response.from_dict(customer_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


