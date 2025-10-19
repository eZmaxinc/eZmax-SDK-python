# TranqcontractImportIntoEDMV1Request

Request for POST /1/object/tranqcontract/{pkiTranqcontractID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.tranqcontract_import_into_edmv1_request import TranqcontractImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of TranqcontractImportIntoEDMV1Request from a JSON string
tranqcontract_import_into_edmv1_request_instance = TranqcontractImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(TranqcontractImportIntoEDMV1Request.to_json())

# convert the object into a dict
tranqcontract_import_into_edmv1_request_dict = tranqcontract_import_into_edmv1_request_instance.to_dict()
# create an instance of TranqcontractImportIntoEDMV1Request from a dict
tranqcontract_import_into_edmv1_request_from_dict = TranqcontractImportIntoEDMV1Request.from_dict(tranqcontract_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


