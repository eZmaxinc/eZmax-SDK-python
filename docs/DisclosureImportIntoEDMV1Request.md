# DisclosureImportIntoEDMV1Request

Request for POST /1/object/disclosure/{pkiDisclosureID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.disclosure_import_into_edmv1_request import DisclosureImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureImportIntoEDMV1Request from a JSON string
disclosure_import_into_edmv1_request_instance = DisclosureImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(DisclosureImportIntoEDMV1Request.to_json())

# convert the object into a dict
disclosure_import_into_edmv1_request_dict = disclosure_import_into_edmv1_request_instance.to_dict()
# create an instance of DisclosureImportIntoEDMV1Request from a dict
disclosure_import_into_edmv1_request_from_dict = DisclosureImportIntoEDMV1Request.from_dict(disclosure_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


