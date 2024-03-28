# UserGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/user/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_user** | [**List[UserAutocompleteElementResponse]**](UserAutocompleteElementResponse.md) | An array of User autocomplete element response. | 

## Example

```python
from eZmaxApi.models.user_get_autocomplete_v2_response_m_payload import UserGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetAutocompleteV2ResponseMPayload from a JSON string
user_get_autocomplete_v2_response_m_payload_instance = UserGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UserGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
user_get_autocomplete_v2_response_m_payload_dict = user_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of UserGetAutocompleteV2ResponseMPayload from a dict
user_get_autocomplete_v2_response_m_payload_form_dict = user_get_autocomplete_v2_response_m_payload.from_dict(user_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


