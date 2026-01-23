# InfrastructureregionGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/infrastructureregion/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_infrastructureregion** | [**List[InfrastructureregionAutocompleteElementResponse]**](InfrastructureregionAutocompleteElementResponse.md) | An array of Infrastructureregion autocomplete element response. | 

## Example

```python
from eZmaxApi.models.infrastructureregion_get_autocomplete_v2_response_m_payload import InfrastructureregionGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InfrastructureregionGetAutocompleteV2ResponseMPayload from a JSON string
infrastructureregion_get_autocomplete_v2_response_m_payload_instance = InfrastructureregionGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InfrastructureregionGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
infrastructureregion_get_autocomplete_v2_response_m_payload_dict = infrastructureregion_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of InfrastructureregionGetAutocompleteV2ResponseMPayload from a dict
infrastructureregion_get_autocomplete_v2_response_m_payload_from_dict = InfrastructureregionGetAutocompleteV2ResponseMPayload.from_dict(infrastructureregion_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


