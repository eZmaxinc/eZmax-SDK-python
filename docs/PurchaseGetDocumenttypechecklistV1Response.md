# PurchaseGetDocumenttypechecklistV1Response

Response for GET /1/object/purchase/{pkiPurchaseID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PurchaseGetDocumenttypechecklistV1ResponseMPayload**](PurchaseGetDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.purchase_get_documenttypechecklist_v1_response import PurchaseGetDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseGetDocumenttypechecklistV1Response from a JSON string
purchase_get_documenttypechecklist_v1_response_instance = PurchaseGetDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(PurchaseGetDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
purchase_get_documenttypechecklist_v1_response_dict = purchase_get_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of PurchaseGetDocumenttypechecklistV1Response from a dict
purchase_get_documenttypechecklist_v1_response_from_dict = PurchaseGetDocumenttypechecklistV1Response.from_dict(purchase_get_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


