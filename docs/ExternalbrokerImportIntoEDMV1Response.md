# ExternalbrokerImportIntoEDMV1Response

Response for POST /1/object/externalbroker/{pkiExternalbrokerID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ExternalbrokerImportIntoEDMV1ResponseMPayload**](ExternalbrokerImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.externalbroker_import_into_edmv1_response import ExternalbrokerImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalbrokerImportIntoEDMV1Response from a JSON string
externalbroker_import_into_edmv1_response_instance = ExternalbrokerImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(ExternalbrokerImportIntoEDMV1Response.to_json())

# convert the object into a dict
externalbroker_import_into_edmv1_response_dict = externalbroker_import_into_edmv1_response_instance.to_dict()
# create an instance of ExternalbrokerImportIntoEDMV1Response from a dict
externalbroker_import_into_edmv1_response_from_dict = ExternalbrokerImportIntoEDMV1Response.from_dict(externalbroker_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


