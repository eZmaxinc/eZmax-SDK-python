# ElectronicfundstransferGetDocumenttypechecklistV1Response

Response for GET /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ElectronicfundstransferGetDocumenttypechecklistV1ResponseMPayload**](ElectronicfundstransferGetDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.electronicfundstransfer_get_documenttypechecklist_v1_response import ElectronicfundstransferGetDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicfundstransferGetDocumenttypechecklistV1Response from a JSON string
electronicfundstransfer_get_documenttypechecklist_v1_response_instance = ElectronicfundstransferGetDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(ElectronicfundstransferGetDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
electronicfundstransfer_get_documenttypechecklist_v1_response_dict = electronicfundstransfer_get_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of ElectronicfundstransferGetDocumenttypechecklistV1Response from a dict
electronicfundstransfer_get_documenttypechecklist_v1_response_from_dict = ElectronicfundstransferGetDocumenttypechecklistV1Response.from_dict(electronicfundstransfer_get_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


