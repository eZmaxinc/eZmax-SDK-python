# TaxassignmentGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/taxassignment/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_taxassignment** | [**List[TaxassignmentAutocompleteElementResponse]**](TaxassignmentAutocompleteElementResponse.md) | An array of Taxassignment autocomplete element response. | 

## Example

```python
from eZmaxApi.models.taxassignment_get_autocomplete_v2_response_m_payload import TaxassignmentGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TaxassignmentGetAutocompleteV2ResponseMPayload from a JSON string
taxassignment_get_autocomplete_v2_response_m_payload_instance = TaxassignmentGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(TaxassignmentGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
taxassignment_get_autocomplete_v2_response_m_payload_dict = taxassignment_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of TaxassignmentGetAutocompleteV2ResponseMPayload from a dict
taxassignment_get_autocomplete_v2_response_m_payload_from_dict = TaxassignmentGetAutocompleteV2ResponseMPayload.from_dict(taxassignment_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


