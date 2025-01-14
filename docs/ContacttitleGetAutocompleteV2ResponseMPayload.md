# ContacttitleGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/contacttitle/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_contacttitle** | [**List[ContacttitleAutocompleteElementResponse]**](ContacttitleAutocompleteElementResponse.md) | An array of Contacttitle autocomplete element response. | 

## Example

```python
from eZmaxApi.models.contacttitle_get_autocomplete_v2_response_m_payload import ContacttitleGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ContacttitleGetAutocompleteV2ResponseMPayload from a JSON string
contacttitle_get_autocomplete_v2_response_m_payload_instance = ContacttitleGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ContacttitleGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
contacttitle_get_autocomplete_v2_response_m_payload_dict = contacttitle_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of ContacttitleGetAutocompleteV2ResponseMPayload from a dict
contacttitle_get_autocomplete_v2_response_m_payload_from_dict = ContacttitleGetAutocompleteV2ResponseMPayload.from_dict(contacttitle_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


