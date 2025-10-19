# OtherincomeImportIntoEDMV1Request

Request for POST /1/object/otherincome/{pkiOtherincomeID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.otherincome_import_into_edmv1_request import OtherincomeImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of OtherincomeImportIntoEDMV1Request from a JSON string
otherincome_import_into_edmv1_request_instance = OtherincomeImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(OtherincomeImportIntoEDMV1Request.to_json())

# convert the object into a dict
otherincome_import_into_edmv1_request_dict = otherincome_import_into_edmv1_request_instance.to_dict()
# create an instance of OtherincomeImportIntoEDMV1Request from a dict
otherincome_import_into_edmv1_request_from_dict = OtherincomeImportIntoEDMV1Request.from_dict(otherincome_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


