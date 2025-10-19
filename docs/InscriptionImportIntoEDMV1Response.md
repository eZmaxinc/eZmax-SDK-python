# InscriptionImportIntoEDMV1Response

Response for POST /1/object/inscription/{pkiInscriptionID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptionImportIntoEDMV1ResponseMPayload**](InscriptionImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscription_import_into_edmv1_response import InscriptionImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionImportIntoEDMV1Response from a JSON string
inscription_import_into_edmv1_response_instance = InscriptionImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionImportIntoEDMV1Response.to_json())

# convert the object into a dict
inscription_import_into_edmv1_response_dict = inscription_import_into_edmv1_response_instance.to_dict()
# create an instance of InscriptionImportIntoEDMV1Response from a dict
inscription_import_into_edmv1_response_from_dict = InscriptionImportIntoEDMV1Response.from_dict(inscription_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


