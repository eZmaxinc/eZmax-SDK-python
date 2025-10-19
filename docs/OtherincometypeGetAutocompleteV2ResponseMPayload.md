# OtherincometypeGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/otherincometype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_otherincometype** | [**List[OtherincometypeAutocompleteElementResponse]**](OtherincometypeAutocompleteElementResponse.md) | An array of Otherincometype autocomplete element response. | 

## Example

```python
from eZmaxApi.models.otherincometype_get_autocomplete_v2_response_m_payload import OtherincometypeGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of OtherincometypeGetAutocompleteV2ResponseMPayload from a JSON string
otherincometype_get_autocomplete_v2_response_m_payload_instance = OtherincometypeGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(OtherincometypeGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
otherincometype_get_autocomplete_v2_response_m_payload_dict = otherincometype_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of OtherincometypeGetAutocompleteV2ResponseMPayload from a dict
otherincometype_get_autocomplete_v2_response_m_payload_from_dict = OtherincometypeGetAutocompleteV2ResponseMPayload.from_dict(otherincometype_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


