# AttachmentrejectreasonGetAutocompleteV2Response

Response for GET /2/object/attachmentrejectreason/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AttachmentrejectreasonGetAutocompleteV2ResponseMPayload**](AttachmentrejectreasonGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.attachmentrejectreason_get_autocomplete_v2_response import AttachmentrejectreasonGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentrejectreasonGetAutocompleteV2Response from a JSON string
attachmentrejectreason_get_autocomplete_v2_response_instance = AttachmentrejectreasonGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(AttachmentrejectreasonGetAutocompleteV2Response.to_json())

# convert the object into a dict
attachmentrejectreason_get_autocomplete_v2_response_dict = attachmentrejectreason_get_autocomplete_v2_response_instance.to_dict()
# create an instance of AttachmentrejectreasonGetAutocompleteV2Response from a dict
attachmentrejectreason_get_autocomplete_v2_response_from_dict = AttachmentrejectreasonGetAutocompleteV2Response.from_dict(attachmentrejectreason_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


