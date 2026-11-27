# SupplierSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/supplier/{pkiSupplierID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.supplier_sync_documenttypechecklist_v1_response_m_payload import SupplierSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
supplier_sync_documenttypechecklist_v1_response_m_payload_instance = SupplierSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SupplierSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
supplier_sync_documenttypechecklist_v1_response_m_payload_dict = supplier_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of SupplierSyncDocumenttypechecklistV1ResponseMPayload from a dict
supplier_sync_documenttypechecklist_v1_response_m_payload_from_dict = SupplierSyncDocumenttypechecklistV1ResponseMPayload.from_dict(supplier_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


