# SupplierSyncDocumenttypechecklistV1Response

Response for POST /1/object/supplier/{pkiSupplierID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SupplierSyncDocumenttypechecklistV1ResponseMPayload**](SupplierSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.supplier_sync_documenttypechecklist_v1_response import SupplierSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierSyncDocumenttypechecklistV1Response from a JSON string
supplier_sync_documenttypechecklist_v1_response_instance = SupplierSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(SupplierSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
supplier_sync_documenttypechecklist_v1_response_dict = supplier_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of SupplierSyncDocumenttypechecklistV1Response from a dict
supplier_sync_documenttypechecklist_v1_response_from_dict = SupplierSyncDocumenttypechecklistV1Response.from_dict(supplier_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


