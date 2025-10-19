# SupplierGetListV1Response

Response for GET /1/object/supplier/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SupplierGetListV1ResponseMPayload**](SupplierGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.supplier_get_list_v1_response import SupplierGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierGetListV1Response from a JSON string
supplier_get_list_v1_response_instance = SupplierGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(SupplierGetListV1Response.to_json())

# convert the object into a dict
supplier_get_list_v1_response_dict = supplier_get_list_v1_response_instance.to_dict()
# create an instance of SupplierGetListV1Response from a dict
supplier_get_list_v1_response_from_dict = SupplierGetListV1Response.from_dict(supplier_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


