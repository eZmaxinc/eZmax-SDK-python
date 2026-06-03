# EzmaxmaillinglistSubscribeV1Response

Response for POST /1/module/ezmaxmaillinglist/subscribe

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezmaxmaillinglist_subscribe_v1_response import EzmaxmaillinglistSubscribeV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxmaillinglistSubscribeV1Response from a JSON string
ezmaxmaillinglist_subscribe_v1_response_instance = EzmaxmaillinglistSubscribeV1Response.from_json(json)
# print the JSON string representation of the object
print(EzmaxmaillinglistSubscribeV1Response.to_json())

# convert the object into a dict
ezmaxmaillinglist_subscribe_v1_response_dict = ezmaxmaillinglist_subscribe_v1_response_instance.to_dict()
# create an instance of EzmaxmaillinglistSubscribeV1Response from a dict
ezmaxmaillinglist_subscribe_v1_response_from_dict = EzmaxmaillinglistSubscribeV1Response.from_dict(ezmaxmaillinglist_subscribe_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


