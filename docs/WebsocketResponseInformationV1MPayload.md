# WebsocketResponseInformationV1MPayload

Payload for Websocket Information V1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_information_message** | **str** | Information message | 

## Example

```python
from eZmaxApi.models.websocket_response_information_v1_m_payload import WebsocketResponseInformationV1MPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketResponseInformationV1MPayload from a JSON string
websocket_response_information_v1_m_payload_instance = WebsocketResponseInformationV1MPayload.from_json(json)
# print the JSON string representation of the object
print(WebsocketResponseInformationV1MPayload.to_json())

# convert the object into a dict
websocket_response_information_v1_m_payload_dict = websocket_response_information_v1_m_payload_instance.to_dict()
# create an instance of WebsocketResponseInformationV1MPayload from a dict
websocket_response_information_v1_m_payload_from_dict = WebsocketResponseInformationV1MPayload.from_dict(websocket_response_information_v1_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


