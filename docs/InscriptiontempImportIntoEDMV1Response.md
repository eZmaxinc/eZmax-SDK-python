# InscriptiontempImportIntoEDMV1Response

Response for POST /1/object/inscriptiontemp/{pkiInscriptiontempID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptiontempImportIntoEDMV1ResponseMPayload**](InscriptiontempImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptiontemp_import_into_edmv1_response import InscriptiontempImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptiontempImportIntoEDMV1Response from a JSON string
inscriptiontemp_import_into_edmv1_response_instance = InscriptiontempImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptiontempImportIntoEDMV1Response.to_json())

# convert the object into a dict
inscriptiontemp_import_into_edmv1_response_dict = inscriptiontemp_import_into_edmv1_response_instance.to_dict()
# create an instance of InscriptiontempImportIntoEDMV1Response from a dict
inscriptiontemp_import_into_edmv1_response_from_dict = InscriptiontempImportIntoEDMV1Response.from_dict(inscriptiontemp_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


