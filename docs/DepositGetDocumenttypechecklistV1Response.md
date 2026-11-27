# DepositGetDocumenttypechecklistV1Response

Response for GET /1/object/deposit/{pkiDepositID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DepositGetDocumenttypechecklistV1ResponseMPayload**](DepositGetDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.deposit_get_documenttypechecklist_v1_response import DepositGetDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DepositGetDocumenttypechecklistV1Response from a JSON string
deposit_get_documenttypechecklist_v1_response_instance = DepositGetDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(DepositGetDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
deposit_get_documenttypechecklist_v1_response_dict = deposit_get_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of DepositGetDocumenttypechecklistV1Response from a dict
deposit_get_documenttypechecklist_v1_response_from_dict = DepositGetDocumenttypechecklistV1Response.from_dict(deposit_get_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


