# ReconciliationImportIntoEDMV1Response

Response for POST /1/object/reconciliation/{pkiReconciliationID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ReconciliationImportIntoEDMV1ResponseMPayload**](ReconciliationImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.reconciliation_import_into_edmv1_response import ReconciliationImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationImportIntoEDMV1Response from a JSON string
reconciliation_import_into_edmv1_response_instance = ReconciliationImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(ReconciliationImportIntoEDMV1Response.to_json())

# convert the object into a dict
reconciliation_import_into_edmv1_response_dict = reconciliation_import_into_edmv1_response_instance.to_dict()
# create an instance of ReconciliationImportIntoEDMV1Response from a dict
reconciliation_import_into_edmv1_response_from_dict = ReconciliationImportIntoEDMV1Response.from_dict(reconciliation_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


