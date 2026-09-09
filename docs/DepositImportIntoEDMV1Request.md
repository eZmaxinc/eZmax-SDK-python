# DepositImportIntoEDMV1Request

Request for POST /1/object/deposit/{pkiDepositID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.deposit_import_into_edmv1_request import DepositImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DepositImportIntoEDMV1Request from a JSON string
deposit_import_into_edmv1_request_instance = DepositImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(DepositImportIntoEDMV1Request.to_json())

# convert the object into a dict
deposit_import_into_edmv1_request_dict = deposit_import_into_edmv1_request_instance.to_dict()
# create an instance of DepositImportIntoEDMV1Request from a dict
deposit_import_into_edmv1_request_from_dict = DepositImportIntoEDMV1Request.from_dict(deposit_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


