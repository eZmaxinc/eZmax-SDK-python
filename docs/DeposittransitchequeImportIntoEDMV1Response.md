# DeposittransitchequeImportIntoEDMV1Response

Response for POST /1/object/deposittransitcheque/{pkiDeposittransitchequeID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DeposittransitchequeImportIntoEDMV1ResponseMPayload**](DeposittransitchequeImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.deposittransitcheque_import_into_edmv1_response import DeposittransitchequeImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeposittransitchequeImportIntoEDMV1Response from a JSON string
deposittransitcheque_import_into_edmv1_response_instance = DeposittransitchequeImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(DeposittransitchequeImportIntoEDMV1Response.to_json())

# convert the object into a dict
deposittransitcheque_import_into_edmv1_response_dict = deposittransitcheque_import_into_edmv1_response_instance.to_dict()
# create an instance of DeposittransitchequeImportIntoEDMV1Response from a dict
deposittransitcheque_import_into_edmv1_response_from_dict = DeposittransitchequeImportIntoEDMV1Response.from_dict(deposittransitcheque_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


