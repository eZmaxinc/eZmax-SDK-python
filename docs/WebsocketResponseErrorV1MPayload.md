# WebsocketResponseErrorV1MPayload

Payload for Websocket Error V1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_error_message** | **str** | The message giving details about the error | 
**e_error_code** | [**FieldEErrorCode**](FieldEErrorCode.md) |  | 

## Example

```python
from eZmaxApi.models.websocket_response_error_v1_m_payload import WebsocketResponseErrorV1MPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketResponseErrorV1MPayload from a JSON string
websocket_response_error_v1_m_payload_instance = WebsocketResponseErrorV1MPayload.from_json(json)
# print the JSON string representation of the object
print WebsocketResponseErrorV1MPayload.to_json()

# convert the object into a dict
websocket_response_error_v1_m_payload_dict = websocket_response_error_v1_m_payload_instance.to_dict()
# create an instance of WebsocketResponseErrorV1MPayload from a dict
websocket_response_error_v1_m_payload_form_dict = websocket_response_error_v1_m_payload.from_dict(websocket_response_error_v1_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


