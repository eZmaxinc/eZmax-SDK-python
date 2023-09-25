# EzmaxproductGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/ezmaxproduct/getAutocomplete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezmaxproduct** | [**List[EzmaxproductAutocompleteElementResponse]**](EzmaxproductAutocompleteElementResponse.md) | An array of Ezmaxproduct autocomplete element response. | [optional] 

## Example

```python
from eZmaxApi.models.ezmaxproduct_get_autocomplete_v2_response_m_payload import EzmaxproductGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxproductGetAutocompleteV2ResponseMPayload from a JSON string
ezmaxproduct_get_autocomplete_v2_response_m_payload_instance = EzmaxproductGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzmaxproductGetAutocompleteV2ResponseMPayload.to_json()

# convert the object into a dict
ezmaxproduct_get_autocomplete_v2_response_m_payload_dict = ezmaxproduct_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of EzmaxproductGetAutocompleteV2ResponseMPayload from a dict
ezmaxproduct_get_autocomplete_v2_response_m_payload_form_dict = ezmaxproduct_get_autocomplete_v2_response_m_payload.from_dict(ezmaxproduct_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


