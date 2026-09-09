# PurchaseImportIntoEDMV1Request

Request for POST /1/object/purchase/{pkiPurchaseID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.purchase_import_into_edmv1_request import PurchaseImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseImportIntoEDMV1Request from a JSON string
purchase_import_into_edmv1_request_instance = PurchaseImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(PurchaseImportIntoEDMV1Request.to_json())

# convert the object into a dict
purchase_import_into_edmv1_request_dict = purchase_import_into_edmv1_request_instance.to_dict()
# create an instance of PurchaseImportIntoEDMV1Request from a dict
purchase_import_into_edmv1_request_from_dict = PurchaseImportIntoEDMV1Request.from_dict(purchase_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


