# UsergroupexternalGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/usergroupexternal/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_usergroupexternal** | [**List[UsergroupexternalAutocompleteElementResponse]**](UsergroupexternalAutocompleteElementResponse.md) | An array of Usergroupexternal autocomplete element response. | 

## Example

```python
from eZmaxApi.models.usergroupexternal_get_autocomplete_v2_response_m_payload import UsergroupexternalGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalGetAutocompleteV2ResponseMPayload from a JSON string
usergroupexternal_get_autocomplete_v2_response_m_payload_instance = UsergroupexternalGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
usergroupexternal_get_autocomplete_v2_response_m_payload_dict = usergroupexternal_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of UsergroupexternalGetAutocompleteV2ResponseMPayload from a dict
usergroupexternal_get_autocomplete_v2_response_m_payload_from_dict = UsergroupexternalGetAutocompleteV2ResponseMPayload.from_dict(usergroupexternal_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


