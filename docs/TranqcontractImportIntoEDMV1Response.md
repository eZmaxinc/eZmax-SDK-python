# TranqcontractImportIntoEDMV1Response

Response for POST /1/object/tranqcontract/{pkiTranqcontractID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**TranqcontractImportIntoEDMV1ResponseMPayload**](TranqcontractImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.tranqcontract_import_into_edmv1_response import TranqcontractImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of TranqcontractImportIntoEDMV1Response from a JSON string
tranqcontract_import_into_edmv1_response_instance = TranqcontractImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(TranqcontractImportIntoEDMV1Response.to_json())

# convert the object into a dict
tranqcontract_import_into_edmv1_response_dict = tranqcontract_import_into_edmv1_response_instance.to_dict()
# create an instance of TranqcontractImportIntoEDMV1Response from a dict
tranqcontract_import_into_edmv1_response_from_dict = TranqcontractImportIntoEDMV1Response.from_dict(tranqcontract_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


