# LeadGetCommunicationListV1Response

Response for GET /1/object/lead/{pkiLeadID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**LeadGetCommunicationListV1ResponseMPayload**](LeadGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.lead_get_communication_list_v1_response import LeadGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of LeadGetCommunicationListV1Response from a JSON string
lead_get_communication_list_v1_response_instance = LeadGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print(LeadGetCommunicationListV1Response.to_json())

# convert the object into a dict
lead_get_communication_list_v1_response_dict = lead_get_communication_list_v1_response_instance.to_dict()
# create an instance of LeadGetCommunicationListV1Response from a dict
lead_get_communication_list_v1_response_from_dict = LeadGetCommunicationListV1Response.from_dict(lead_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


