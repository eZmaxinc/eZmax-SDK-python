# ElectronicfundstransferImportIntoEDMV1Response

Response for POST /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ElectronicfundstransferImportIntoEDMV1ResponseMPayload**](ElectronicfundstransferImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.electronicfundstransfer_import_into_edmv1_response import ElectronicfundstransferImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicfundstransferImportIntoEDMV1Response from a JSON string
electronicfundstransfer_import_into_edmv1_response_instance = ElectronicfundstransferImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(ElectronicfundstransferImportIntoEDMV1Response.to_json())

# convert the object into a dict
electronicfundstransfer_import_into_edmv1_response_dict = electronicfundstransfer_import_into_edmv1_response_instance.to_dict()
# create an instance of ElectronicfundstransferImportIntoEDMV1Response from a dict
electronicfundstransfer_import_into_edmv1_response_from_dict = ElectronicfundstransferImportIntoEDMV1Response.from_dict(electronicfundstransfer_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


