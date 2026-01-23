# RealestateassociationGetAutocompleteV2Response

Response for GET /2/object/realestateassociation/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**RealestateassociationGetAutocompleteV2ResponseMPayload**](RealestateassociationGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.realestateassociation_get_autocomplete_v2_response import RealestateassociationGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of RealestateassociationGetAutocompleteV2Response from a JSON string
realestateassociation_get_autocomplete_v2_response_instance = RealestateassociationGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(RealestateassociationGetAutocompleteV2Response.to_json())

# convert the object into a dict
realestateassociation_get_autocomplete_v2_response_dict = realestateassociation_get_autocomplete_v2_response_instance.to_dict()
# create an instance of RealestateassociationGetAutocompleteV2Response from a dict
realestateassociation_get_autocomplete_v2_response_from_dict = RealestateassociationGetAutocompleteV2Response.from_dict(realestateassociation_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


