# BuyercontractGetDocumenttypechecklistV1Response

Response for GET /1/object/buyercontract/{pkiBuyercontractID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BuyercontractGetDocumenttypechecklistV1ResponseMPayload**](BuyercontractGetDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.buyercontract_get_documenttypechecklist_v1_response import BuyercontractGetDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractGetDocumenttypechecklistV1Response from a JSON string
buyercontract_get_documenttypechecklist_v1_response_instance = BuyercontractGetDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(BuyercontractGetDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
buyercontract_get_documenttypechecklist_v1_response_dict = buyercontract_get_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of BuyercontractGetDocumenttypechecklistV1Response from a dict
buyercontract_get_documenttypechecklist_v1_response_from_dict = BuyercontractGetDocumenttypechecklistV1Response.from_dict(buyercontract_get_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


