# OfficetaxreportImportIntoEDMV1Response

Response for POST /1/object/officetaxreport/{pkiOfficetaxreportID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**OfficetaxreportImportIntoEDMV1ResponseMPayload**](OfficetaxreportImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.officetaxreport_import_into_edmv1_response import OfficetaxreportImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of OfficetaxreportImportIntoEDMV1Response from a JSON string
officetaxreport_import_into_edmv1_response_instance = OfficetaxreportImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(OfficetaxreportImportIntoEDMV1Response.to_json())

# convert the object into a dict
officetaxreport_import_into_edmv1_response_dict = officetaxreport_import_into_edmv1_response_instance.to_dict()
# create an instance of OfficetaxreportImportIntoEDMV1Response from a dict
officetaxreport_import_into_edmv1_response_from_dict = OfficetaxreportImportIntoEDMV1Response.from_dict(officetaxreport_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


