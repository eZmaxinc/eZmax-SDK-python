# OtherincomeGetDocumenttypechecklistV1Response

Response for GET /1/object/otherincome/{pkiOtherincomeID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**OtherincomeGetDocumenttypechecklistV1ResponseMPayload**](OtherincomeGetDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.otherincome_get_documenttypechecklist_v1_response import OtherincomeGetDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of OtherincomeGetDocumenttypechecklistV1Response from a JSON string
otherincome_get_documenttypechecklist_v1_response_instance = OtherincomeGetDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(OtherincomeGetDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
otherincome_get_documenttypechecklist_v1_response_dict = otherincome_get_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of OtherincomeGetDocumenttypechecklistV1Response from a dict
otherincome_get_documenttypechecklist_v1_response_from_dict = OtherincomeGetDocumenttypechecklistV1Response.from_dict(otherincome_get_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


