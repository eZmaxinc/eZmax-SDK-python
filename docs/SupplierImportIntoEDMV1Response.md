# SupplierImportIntoEDMV1Response

Response for POST /1/object/supplier/{pkiSupplierID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SupplierImportIntoEDMV1ResponseMPayload**](SupplierImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.supplier_import_into_edmv1_response import SupplierImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierImportIntoEDMV1Response from a JSON string
supplier_import_into_edmv1_response_instance = SupplierImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(SupplierImportIntoEDMV1Response.to_json())

# convert the object into a dict
supplier_import_into_edmv1_response_dict = supplier_import_into_edmv1_response_instance.to_dict()
# create an instance of SupplierImportIntoEDMV1Response from a dict
supplier_import_into_edmv1_response_from_dict = SupplierImportIntoEDMV1Response.from_dict(supplier_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


