# AuthenticationexternalGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/authenticationexternal/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_authenticationexternal** | [**List[AuthenticationexternalAutocompleteElementResponse]**](AuthenticationexternalAutocompleteElementResponse.md) | An array of Authenticationexternal autocomplete element response. | 

## Example

```python
from eZmaxApi.models.authenticationexternal_get_autocomplete_v2_response_m_payload import AuthenticationexternalGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationexternalGetAutocompleteV2ResponseMPayload from a JSON string
authenticationexternal_get_autocomplete_v2_response_m_payload_instance = AuthenticationexternalGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AuthenticationexternalGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
authenticationexternal_get_autocomplete_v2_response_m_payload_dict = authenticationexternal_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of AuthenticationexternalGetAutocompleteV2ResponseMPayload from a dict
authenticationexternal_get_autocomplete_v2_response_m_payload_from_dict = AuthenticationexternalGetAutocompleteV2ResponseMPayload.from_dict(authenticationexternal_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


