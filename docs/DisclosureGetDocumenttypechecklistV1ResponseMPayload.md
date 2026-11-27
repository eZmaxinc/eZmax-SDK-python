# DisclosureGetDocumenttypechecklistV1ResponseMPayload

Response for GET /1/object/disclosure/{pkiDisclosureID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.disclosure_get_documenttypechecklist_v1_response_m_payload import DisclosureGetDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureGetDocumenttypechecklistV1ResponseMPayload from a JSON string
disclosure_get_documenttypechecklist_v1_response_m_payload_instance = DisclosureGetDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DisclosureGetDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
disclosure_get_documenttypechecklist_v1_response_m_payload_dict = disclosure_get_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of DisclosureGetDocumenttypechecklistV1ResponseMPayload from a dict
disclosure_get_documenttypechecklist_v1_response_m_payload_from_dict = DisclosureGetDocumenttypechecklistV1ResponseMPayload.from_dict(disclosure_get_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


