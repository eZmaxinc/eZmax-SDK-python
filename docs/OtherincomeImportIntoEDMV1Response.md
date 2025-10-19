# OtherincomeImportIntoEDMV1Response

Response for POST /1/object/otherincome/{pkiOtherincomeID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**OtherincomeImportIntoEDMV1ResponseMPayload**](OtherincomeImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.otherincome_import_into_edmv1_response import OtherincomeImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of OtherincomeImportIntoEDMV1Response from a JSON string
otherincome_import_into_edmv1_response_instance = OtherincomeImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(OtherincomeImportIntoEDMV1Response.to_json())

# convert the object into a dict
otherincome_import_into_edmv1_response_dict = otherincome_import_into_edmv1_response_instance.to_dict()
# create an instance of OtherincomeImportIntoEDMV1Response from a dict
otherincome_import_into_edmv1_response_from_dict = OtherincomeImportIntoEDMV1Response.from_dict(otherincome_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


