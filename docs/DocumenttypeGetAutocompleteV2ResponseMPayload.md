# DocumenttypeGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/documenttype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttype** | [**List[DocumenttypeAutocompleteElementResponse]**](DocumenttypeAutocompleteElementResponse.md) | An array of Documenttype autocomplete element response. | 

## Example

```python
from eZmaxApi.models.documenttype_get_autocomplete_v2_response_m_payload import DocumenttypeGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypeGetAutocompleteV2ResponseMPayload from a JSON string
documenttype_get_autocomplete_v2_response_m_payload_instance = DocumenttypeGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DocumenttypeGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
documenttype_get_autocomplete_v2_response_m_payload_dict = documenttype_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of DocumenttypeGetAutocompleteV2ResponseMPayload from a dict
documenttype_get_autocomplete_v2_response_m_payload_from_dict = DocumenttypeGetAutocompleteV2ResponseMPayload.from_dict(documenttype_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


