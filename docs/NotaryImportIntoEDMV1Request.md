# NotaryImportIntoEDMV1Request

Request for POST /1/object/notary/{pkiNotaryID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.notary_import_into_edmv1_request import NotaryImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of NotaryImportIntoEDMV1Request from a JSON string
notary_import_into_edmv1_request_instance = NotaryImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(NotaryImportIntoEDMV1Request.to_json())

# convert the object into a dict
notary_import_into_edmv1_request_dict = notary_import_into_edmv1_request_instance.to_dict()
# create an instance of NotaryImportIntoEDMV1Request from a dict
notary_import_into_edmv1_request_from_dict = NotaryImportIntoEDMV1Request.from_dict(notary_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


