# BrokertypeGetAutocompleteV2Response

Response for GET /2/object/brokertype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BrokertypeGetAutocompleteV2ResponseMPayload**](BrokertypeGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.brokertype_get_autocomplete_v2_response import BrokertypeGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of BrokertypeGetAutocompleteV2Response from a JSON string
brokertype_get_autocomplete_v2_response_instance = BrokertypeGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(BrokertypeGetAutocompleteV2Response.to_json())

# convert the object into a dict
brokertype_get_autocomplete_v2_response_dict = brokertype_get_autocomplete_v2_response_instance.to_dict()
# create an instance of BrokertypeGetAutocompleteV2Response from a dict
brokertype_get_autocomplete_v2_response_from_dict = BrokertypeGetAutocompleteV2Response.from_dict(brokertype_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


