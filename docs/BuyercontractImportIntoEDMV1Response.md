# BuyercontractImportIntoEDMV1Response

Response for POST /1/object/buyercontract/{pkiBuyercontractID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BuyercontractImportIntoEDMV1ResponseMPayload**](BuyercontractImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.buyercontract_import_into_edmv1_response import BuyercontractImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractImportIntoEDMV1Response from a JSON string
buyercontract_import_into_edmv1_response_instance = BuyercontractImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(BuyercontractImportIntoEDMV1Response.to_json())

# convert the object into a dict
buyercontract_import_into_edmv1_response_dict = buyercontract_import_into_edmv1_response_instance.to_dict()
# create an instance of BuyercontractImportIntoEDMV1Response from a dict
buyercontract_import_into_edmv1_response_from_dict = BuyercontractImportIntoEDMV1Response.from_dict(buyercontract_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


