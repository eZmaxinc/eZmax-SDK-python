# DisclosureGetDocumenttypechecklistV1Response

Response for GET /1/object/disclosure/{pkiDisclosureID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DisclosureGetDocumenttypechecklistV1ResponseMPayload**](DisclosureGetDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.disclosure_get_documenttypechecklist_v1_response import DisclosureGetDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureGetDocumenttypechecklistV1Response from a JSON string
disclosure_get_documenttypechecklist_v1_response_instance = DisclosureGetDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(DisclosureGetDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
disclosure_get_documenttypechecklist_v1_response_dict = disclosure_get_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of DisclosureGetDocumenttypechecklistV1Response from a dict
disclosure_get_documenttypechecklist_v1_response_from_dict = DisclosureGetDocumenttypechecklistV1Response.from_dict(disclosure_get_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


