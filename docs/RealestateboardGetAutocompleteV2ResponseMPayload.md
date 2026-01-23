# RealestateboardGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/realestateboard/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_realestateboard** | [**List[RealestateboardAutocompleteElementResponse]**](RealestateboardAutocompleteElementResponse.md) | An array of Realestateboard autocomplete element response. | 

## Example

```python
from eZmaxApi.models.realestateboard_get_autocomplete_v2_response_m_payload import RealestateboardGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RealestateboardGetAutocompleteV2ResponseMPayload from a JSON string
realestateboard_get_autocomplete_v2_response_m_payload_instance = RealestateboardGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(RealestateboardGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
realestateboard_get_autocomplete_v2_response_m_payload_dict = realestateboard_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of RealestateboardGetAutocompleteV2ResponseMPayload from a dict
realestateboard_get_autocomplete_v2_response_m_payload_from_dict = RealestateboardGetAutocompleteV2ResponseMPayload.from_dict(realestateboard_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


