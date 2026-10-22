# DocumenttypechecklistGetObjectV2ResponseMPayload

Payload for GET /2/object/documenttypechecklist/{pkiDocumenttypechecklistID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_documenttypechecklist** | [**DocumenttypechecklistResponseCompound**](DocumenttypechecklistResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.documenttypechecklist_get_object_v2_response_m_payload import DocumenttypechecklistGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypechecklistGetObjectV2ResponseMPayload from a JSON string
documenttypechecklist_get_object_v2_response_m_payload_instance = DocumenttypechecklistGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DocumenttypechecklistGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
documenttypechecklist_get_object_v2_response_m_payload_dict = documenttypechecklist_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of DocumenttypechecklistGetObjectV2ResponseMPayload from a dict
documenttypechecklist_get_object_v2_response_m_payload_from_dict = DocumenttypechecklistGetObjectV2ResponseMPayload.from_dict(documenttypechecklist_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


