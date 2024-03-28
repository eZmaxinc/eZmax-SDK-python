# EzsigntemplatepackageGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/ezsigntemplatepackage/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatepackage** | [**List[EzsigntemplatepackageAutocompleteElementResponse]**](EzsigntemplatepackageAutocompleteElementResponse.md) | An array of Ezsigntemplatepackage autocomplete element response. | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_get_autocomplete_v2_response_m_payload import EzsigntemplatepackageGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageGetAutocompleteV2ResponseMPayload from a JSON string
ezsigntemplatepackage_get_autocomplete_v2_response_m_payload_instance = EzsigntemplatepackageGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackageGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatepackage_get_autocomplete_v2_response_m_payload_dict = ezsigntemplatepackage_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepackageGetAutocompleteV2ResponseMPayload from a dict
ezsigntemplatepackage_get_autocomplete_v2_response_m_payload_form_dict = ezsigntemplatepackage_get_autocomplete_v2_response_m_payload.from_dict(ezsigntemplatepackage_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


