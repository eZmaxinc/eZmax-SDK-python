# AdjustmentImportIntoEDMV1Request

Response for POST /1/object/adjustment/{pkiAdjustmentID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.adjustment_import_into_edmv1_request import AdjustmentImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentImportIntoEDMV1Request from a JSON string
adjustment_import_into_edmv1_request_instance = AdjustmentImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(AdjustmentImportIntoEDMV1Request.to_json())

# convert the object into a dict
adjustment_import_into_edmv1_request_dict = adjustment_import_into_edmv1_request_instance.to_dict()
# create an instance of AdjustmentImportIntoEDMV1Request from a dict
adjustment_import_into_edmv1_request_from_dict = AdjustmentImportIntoEDMV1Request.from_dict(adjustment_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


