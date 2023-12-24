# UsergroupGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/usergroup/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_usergroup** | [**List[UsergroupAutocompleteElementResponse]**](UsergroupAutocompleteElementResponse.md) | An array of Usergroup autocomplete element response. | 

## Example

```python
from eZmaxApi.models.usergroup_get_autocomplete_v2_response_m_payload import UsergroupGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupGetAutocompleteV2ResponseMPayload from a JSON string
usergroup_get_autocomplete_v2_response_m_payload_instance = UsergroupGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print UsergroupGetAutocompleteV2ResponseMPayload.to_json()

# convert the object into a dict
usergroup_get_autocomplete_v2_response_m_payload_dict = usergroup_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of UsergroupGetAutocompleteV2ResponseMPayload from a dict
usergroup_get_autocomplete_v2_response_m_payload_form_dict = usergroup_get_autocomplete_v2_response_m_payload.from_dict(usergroup_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


