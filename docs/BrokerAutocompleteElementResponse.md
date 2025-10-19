# BrokerAutocompleteElementResponse

A Broker AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_broker_id** | **int** | The unique ID of the Broker. | 
**fki_department_id** | **int** | The unique ID of the Department | 
**s_broker_name** | **str** | The name of the Broker | 
**b_broker_isactive** | **bool** | Whether the Broker is active or not | 

## Example

```python
from eZmaxApi.models.broker_autocomplete_element_response import BrokerAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerAutocompleteElementResponse from a JSON string
broker_autocomplete_element_response_instance = BrokerAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(BrokerAutocompleteElementResponse.to_json())

# convert the object into a dict
broker_autocomplete_element_response_dict = broker_autocomplete_element_response_instance.to_dict()
# create an instance of BrokerAutocompleteElementResponse from a dict
broker_autocomplete_element_response_from_dict = BrokerAutocompleteElementResponse.from_dict(broker_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


