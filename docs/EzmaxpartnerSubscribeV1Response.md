# EzmaxpartnerSubscribeV1Response

Request for POST /1/module/ezmaxmaillinglist/subscribe

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_external_id** | **str** |  | 

## Example

```python
from eZmaxApi.models.ezmaxpartner_subscribe_v1_response import EzmaxpartnerSubscribeV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerSubscribeV1Response from a JSON string
ezmaxpartner_subscribe_v1_response_instance = EzmaxpartnerSubscribeV1Response.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerSubscribeV1Response.to_json())

# convert the object into a dict
ezmaxpartner_subscribe_v1_response_dict = ezmaxpartner_subscribe_v1_response_instance.to_dict()
# create an instance of EzmaxpartnerSubscribeV1Response from a dict
ezmaxpartner_subscribe_v1_response_from_dict = EzmaxpartnerSubscribeV1Response.from_dict(ezmaxpartner_subscribe_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


