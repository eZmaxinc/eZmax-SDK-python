# NotaryImportIntoEDMV1Response

Response for POST /1/object/notary/{pkiNotaryID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**NotaryImportIntoEDMV1ResponseMPayload**](NotaryImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.notary_import_into_edmv1_response import NotaryImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of NotaryImportIntoEDMV1Response from a JSON string
notary_import_into_edmv1_response_instance = NotaryImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(NotaryImportIntoEDMV1Response.to_json())

# convert the object into a dict
notary_import_into_edmv1_response_dict = notary_import_into_edmv1_response_instance.to_dict()
# create an instance of NotaryImportIntoEDMV1Response from a dict
notary_import_into_edmv1_response_from_dict = NotaryImportIntoEDMV1Response.from_dict(notary_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


