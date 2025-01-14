# SupplyGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/supply/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_supply** | [**List[SupplyAutocompleteElementResponse]**](SupplyAutocompleteElementResponse.md) | An array of Supply autocomplete element response. | 

## Example

```python
from eZmaxApi.models.supply_get_autocomplete_v2_response_m_payload import SupplyGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyGetAutocompleteV2ResponseMPayload from a JSON string
supply_get_autocomplete_v2_response_m_payload_instance = SupplyGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SupplyGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
supply_get_autocomplete_v2_response_m_payload_dict = supply_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of SupplyGetAutocompleteV2ResponseMPayload from a dict
supply_get_autocomplete_v2_response_m_payload_from_dict = SupplyGetAutocompleteV2ResponseMPayload.from_dict(supply_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


