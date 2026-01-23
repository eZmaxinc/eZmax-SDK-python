# RealestateassociationGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/realestateassociation/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_realestateassociation** | [**List[RealestateassociationAutocompleteElementResponse]**](RealestateassociationAutocompleteElementResponse.md) | An array of Realestateassociation autocomplete element response. | 

## Example

```python
from eZmaxApi.models.realestateassociation_get_autocomplete_v2_response_m_payload import RealestateassociationGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RealestateassociationGetAutocompleteV2ResponseMPayload from a JSON string
realestateassociation_get_autocomplete_v2_response_m_payload_instance = RealestateassociationGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(RealestateassociationGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
realestateassociation_get_autocomplete_v2_response_m_payload_dict = realestateassociation_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of RealestateassociationGetAutocompleteV2ResponseMPayload from a dict
realestateassociation_get_autocomplete_v2_response_m_payload_from_dict = RealestateassociationGetAutocompleteV2ResponseMPayload.from_dict(realestateassociation_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


