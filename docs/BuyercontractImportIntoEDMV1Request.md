# BuyercontractImportIntoEDMV1Request

Request for POST /1/object/buyercontract/{pkiBuyercontractID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.buyercontract_import_into_edmv1_request import BuyercontractImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractImportIntoEDMV1Request from a JSON string
buyercontract_import_into_edmv1_request_instance = BuyercontractImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(BuyercontractImportIntoEDMV1Request.to_json())

# convert the object into a dict
buyercontract_import_into_edmv1_request_dict = buyercontract_import_into_edmv1_request_instance.to_dict()
# create an instance of BuyercontractImportIntoEDMV1Request from a dict
buyercontract_import_into_edmv1_request_from_dict = BuyercontractImportIntoEDMV1Request.from_dict(buyercontract_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


