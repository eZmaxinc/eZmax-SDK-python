# BrandingGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/branding/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_branding** | [**List[BrandingAutocompleteElementResponse]**](BrandingAutocompleteElementResponse.md) | An array of Branding object containing the description, ID and active status about the element. | 

## Example

```python
from eZmaxApi.models.branding_get_autocomplete_v2_response_m_payload import BrandingGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingGetAutocompleteV2ResponseMPayload from a JSON string
branding_get_autocomplete_v2_response_m_payload_instance = BrandingGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print BrandingGetAutocompleteV2ResponseMPayload.to_json()

# convert the object into a dict
branding_get_autocomplete_v2_response_m_payload_dict = branding_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of BrandingGetAutocompleteV2ResponseMPayload from a dict
branding_get_autocomplete_v2_response_m_payload_form_dict = branding_get_autocomplete_v2_response_m_payload.from_dict(branding_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


