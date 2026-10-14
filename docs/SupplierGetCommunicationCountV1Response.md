# SupplierGetCommunicationCountV1Response

Response for GET /1/object/supplier/{pkiSupplierID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SupplierGetCommunicationCountV1ResponseMPayload**](SupplierGetCommunicationCountV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.supplier_get_communication_count_v1_response import SupplierGetCommunicationCountV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierGetCommunicationCountV1Response from a JSON string
supplier_get_communication_count_v1_response_instance = SupplierGetCommunicationCountV1Response.from_json(json)
# print the JSON string representation of the object
print(SupplierGetCommunicationCountV1Response.to_json())

# convert the object into a dict
supplier_get_communication_count_v1_response_dict = supplier_get_communication_count_v1_response_instance.to_dict()
# create an instance of SupplierGetCommunicationCountV1Response from a dict
supplier_get_communication_count_v1_response_from_dict = SupplierGetCommunicationCountV1Response.from_dict(supplier_get_communication_count_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


