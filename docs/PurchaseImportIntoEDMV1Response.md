# PurchaseImportIntoEDMV1Response

Response for POST /1/object/purchase/{pkiPurchaseID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PurchaseImportIntoEDMV1ResponseMPayload**](PurchaseImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.purchase_import_into_edmv1_response import PurchaseImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseImportIntoEDMV1Response from a JSON string
purchase_import_into_edmv1_response_instance = PurchaseImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(PurchaseImportIntoEDMV1Response.to_json())

# convert the object into a dict
purchase_import_into_edmv1_response_dict = purchase_import_into_edmv1_response_instance.to_dict()
# create an instance of PurchaseImportIntoEDMV1Response from a dict
purchase_import_into_edmv1_response_from_dict = PurchaseImportIntoEDMV1Response.from_dict(purchase_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


