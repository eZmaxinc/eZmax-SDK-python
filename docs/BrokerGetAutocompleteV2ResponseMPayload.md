# BrokerGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/broker/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_broker** | [**List[BrokerAutocompleteElementResponse]**](BrokerAutocompleteElementResponse.md) | An array of Broker autocomplete element response. | 

## Example

```python
from eZmaxApi.models.broker_get_autocomplete_v2_response_m_payload import BrokerGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerGetAutocompleteV2ResponseMPayload from a JSON string
broker_get_autocomplete_v2_response_m_payload_instance = BrokerGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BrokerGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
broker_get_autocomplete_v2_response_m_payload_dict = broker_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of BrokerGetAutocompleteV2ResponseMPayload from a dict
broker_get_autocomplete_v2_response_m_payload_from_dict = BrokerGetAutocompleteV2ResponseMPayload.from_dict(broker_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


