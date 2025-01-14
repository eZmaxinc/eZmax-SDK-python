# WebsocketResponseGetWebsocketIDV1

Response for Websocket GetWebsocketID V1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_websocket_messagetype** | **str** | The Type of message | 
**m_payload** | [**WebsocketResponseGetWebsocketIDV1MPayload**](WebsocketResponseGetWebsocketIDV1MPayload.md) |  | 

## Example

```python
from eZmaxApi.models.websocket_response_get_websocket_idv1 import WebsocketResponseGetWebsocketIDV1

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketResponseGetWebsocketIDV1 from a JSON string
websocket_response_get_websocket_idv1_instance = WebsocketResponseGetWebsocketIDV1.from_json(json)
# print the JSON string representation of the object
print(WebsocketResponseGetWebsocketIDV1.to_json())

# convert the object into a dict
websocket_response_get_websocket_idv1_dict = websocket_response_get_websocket_idv1_instance.to_dict()
# create an instance of WebsocketResponseGetWebsocketIDV1 from a dict
websocket_response_get_websocket_idv1_from_dict = WebsocketResponseGetWebsocketIDV1.from_dict(websocket_response_get_websocket_idv1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


