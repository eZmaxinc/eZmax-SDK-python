# EzmaxinvoicingGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/ezmaxinvoicing/getAutocomplete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezmaxinvoicing** | [**List[EzmaxinvoicingAutocompleteElementResponse]**](EzmaxinvoicingAutocompleteElementResponse.md) | An array of Ezmaxinvoicing autocomplete element response. | 

## Example

```python
from eZmaxApi.models.ezmaxinvoicing_get_autocomplete_v2_response_m_payload import EzmaxinvoicingGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingGetAutocompleteV2ResponseMPayload from a JSON string
ezmaxinvoicing_get_autocomplete_v2_response_m_payload_instance = EzmaxinvoicingGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzmaxinvoicingGetAutocompleteV2ResponseMPayload.to_json()

# convert the object into a dict
ezmaxinvoicing_get_autocomplete_v2_response_m_payload_dict = ezmaxinvoicing_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of EzmaxinvoicingGetAutocompleteV2ResponseMPayload from a dict
ezmaxinvoicing_get_autocomplete_v2_response_m_payload_form_dict = ezmaxinvoicing_get_autocomplete_v2_response_m_payload.from_dict(ezmaxinvoicing_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


