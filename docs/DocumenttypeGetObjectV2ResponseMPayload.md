# DocumenttypeGetObjectV2ResponseMPayload

Payload for GET /2/object/documenttype/{pkiDocumenttypeID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_documenttype** | [**DocumenttypeResponseCompound**](DocumenttypeResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.documenttype_get_object_v2_response_m_payload import DocumenttypeGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypeGetObjectV2ResponseMPayload from a JSON string
documenttype_get_object_v2_response_m_payload_instance = DocumenttypeGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DocumenttypeGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
documenttype_get_object_v2_response_m_payload_dict = documenttype_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of DocumenttypeGetObjectV2ResponseMPayload from a dict
documenttype_get_object_v2_response_m_payload_from_dict = DocumenttypeGetObjectV2ResponseMPayload.from_dict(documenttype_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


