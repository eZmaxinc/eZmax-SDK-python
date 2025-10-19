# RejectedoffertopurchaseImportIntoEDMV1Request

Request for POST /1/object/rejectedoffertopurchase/{pkiRejectedoffertopurchaseID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.rejectedoffertopurchase_import_into_edmv1_request import RejectedoffertopurchaseImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of RejectedoffertopurchaseImportIntoEDMV1Request from a JSON string
rejectedoffertopurchase_import_into_edmv1_request_instance = RejectedoffertopurchaseImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(RejectedoffertopurchaseImportIntoEDMV1Request.to_json())

# convert the object into a dict
rejectedoffertopurchase_import_into_edmv1_request_dict = rejectedoffertopurchase_import_into_edmv1_request_instance.to_dict()
# create an instance of RejectedoffertopurchaseImportIntoEDMV1Request from a dict
rejectedoffertopurchase_import_into_edmv1_request_from_dict = RejectedoffertopurchaseImportIntoEDMV1Request.from_dict(rejectedoffertopurchase_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


