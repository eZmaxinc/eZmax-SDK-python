# DeposittransitchequeImportIntoEDMV1Request

Request for POST /1/object/deposittransitcheque/{pkiDeposittransitchequeID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.deposittransitcheque_import_into_edmv1_request import DeposittransitchequeImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DeposittransitchequeImportIntoEDMV1Request from a JSON string
deposittransitcheque_import_into_edmv1_request_instance = DeposittransitchequeImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(DeposittransitchequeImportIntoEDMV1Request.to_json())

# convert the object into a dict
deposittransitcheque_import_into_edmv1_request_dict = deposittransitcheque_import_into_edmv1_request_instance.to_dict()
# create an instance of DeposittransitchequeImportIntoEDMV1Request from a dict
deposittransitcheque_import_into_edmv1_request_from_dict = DeposittransitchequeImportIntoEDMV1Request.from_dict(deposittransitcheque_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


