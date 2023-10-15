# UserlogintypeGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/userlogintype/getAutocomplete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_userlogintype** | [**List[UserlogintypeAutocompleteElementResponse]**](UserlogintypeAutocompleteElementResponse.md) | An array of Userlogintype autocomplete element response. | 

## Example

```python
from eZmaxApi.models.userlogintype_get_autocomplete_v2_response_m_payload import UserlogintypeGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UserlogintypeGetAutocompleteV2ResponseMPayload from a JSON string
userlogintype_get_autocomplete_v2_response_m_payload_instance = UserlogintypeGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print UserlogintypeGetAutocompleteV2ResponseMPayload.to_json()

# convert the object into a dict
userlogintype_get_autocomplete_v2_response_m_payload_dict = userlogintype_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of UserlogintypeGetAutocompleteV2ResponseMPayload from a dict
userlogintype_get_autocomplete_v2_response_m_payload_form_dict = userlogintype_get_autocomplete_v2_response_m_payload.from_dict(userlogintype_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


