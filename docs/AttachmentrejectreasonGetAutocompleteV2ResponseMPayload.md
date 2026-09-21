# AttachmentrejectreasonGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/attachmentrejectreason/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachmentrejectreason** | [**List[AttachmentrejectreasonAutocompleteElementResponse]**](AttachmentrejectreasonAutocompleteElementResponse.md) | An array of Attachmentrejectreason autocomplete element response. | 

## Example

```python
from eZmaxApi.models.attachmentrejectreason_get_autocomplete_v2_response_m_payload import AttachmentrejectreasonGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentrejectreasonGetAutocompleteV2ResponseMPayload from a JSON string
attachmentrejectreason_get_autocomplete_v2_response_m_payload_instance = AttachmentrejectreasonGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AttachmentrejectreasonGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
attachmentrejectreason_get_autocomplete_v2_response_m_payload_dict = attachmentrejectreason_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of AttachmentrejectreasonGetAutocompleteV2ResponseMPayload from a dict
attachmentrejectreason_get_autocomplete_v2_response_m_payload_from_dict = AttachmentrejectreasonGetAutocompleteV2ResponseMPayload.from_dict(attachmentrejectreason_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


