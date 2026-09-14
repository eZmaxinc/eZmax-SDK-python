# DisclosureGetCommunicationListV1Response

Response for GET /1/object/disclosure/{pkiDisclosureID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DisclosureGetCommunicationListV1ResponseMPayload**](DisclosureGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.disclosure_get_communication_list_v1_response import DisclosureGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureGetCommunicationListV1Response from a JSON string
disclosure_get_communication_list_v1_response_instance = DisclosureGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print(DisclosureGetCommunicationListV1Response.to_json())

# convert the object into a dict
disclosure_get_communication_list_v1_response_dict = disclosure_get_communication_list_v1_response_instance.to_dict()
# create an instance of DisclosureGetCommunicationListV1Response from a dict
disclosure_get_communication_list_v1_response_from_dict = DisclosureGetCommunicationListV1Response.from_dict(disclosure_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


