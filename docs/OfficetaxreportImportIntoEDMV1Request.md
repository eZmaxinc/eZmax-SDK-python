# OfficetaxreportImportIntoEDMV1Request

Request for POST /1/object/officetaxreport/{pkiOfficetaxreportID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.officetaxreport_import_into_edmv1_request import OfficetaxreportImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of OfficetaxreportImportIntoEDMV1Request from a JSON string
officetaxreport_import_into_edmv1_request_instance = OfficetaxreportImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(OfficetaxreportImportIntoEDMV1Request.to_json())

# convert the object into a dict
officetaxreport_import_into_edmv1_request_dict = officetaxreport_import_into_edmv1_request_instance.to_dict()
# create an instance of OfficetaxreportImportIntoEDMV1Request from a dict
officetaxreport_import_into_edmv1_request_from_dict = OfficetaxreportImportIntoEDMV1Request.from_dict(officetaxreport_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


