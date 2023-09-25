# WebsocketResponseInformationV1

Response for Websocket Information V1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_websocket_messagetype** | **str** | The Type of message | 
**m_payload** | [**WebsocketResponseInformationV1MPayload**](WebsocketResponseInformationV1MPayload.md) |  | 

## Example

```python
from eZmaxApi.models.websocket_response_information_v1 import WebsocketResponseInformationV1

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketResponseInformationV1 from a JSON string
websocket_response_information_v1_instance = WebsocketResponseInformationV1.from_json(json)
# print the JSON string representation of the object
print WebsocketResponseInformationV1.to_json()

# convert the object into a dict
websocket_response_information_v1_dict = websocket_response_information_v1_instance.to_dict()
# create an instance of WebsocketResponseInformationV1 from a dict
websocket_response_information_v1_form_dict = websocket_response_information_v1.from_dict(websocket_response_information_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


