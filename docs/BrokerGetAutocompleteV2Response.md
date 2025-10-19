# BrokerGetAutocompleteV2Response

Response for GET /2/object/broker/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BrokerGetAutocompleteV2ResponseMPayload**](BrokerGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.broker_get_autocomplete_v2_response import BrokerGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerGetAutocompleteV2Response from a JSON string
broker_get_autocomplete_v2_response_instance = BrokerGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(BrokerGetAutocompleteV2Response.to_json())

# convert the object into a dict
broker_get_autocomplete_v2_response_dict = broker_get_autocomplete_v2_response_instance.to_dict()
# create an instance of BrokerGetAutocompleteV2Response from a dict
broker_get_autocomplete_v2_response_from_dict = BrokerGetAutocompleteV2Response.from_dict(broker_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


