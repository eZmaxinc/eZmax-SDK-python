# LeadGetCommunicationsendersV1Response

Response for GET /1/object/lead/{pkiLeadID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**LeadGetCommunicationsendersV1ResponseMPayload**](LeadGetCommunicationsendersV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.lead_get_communicationsenders_v1_response import LeadGetCommunicationsendersV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of LeadGetCommunicationsendersV1Response from a JSON string
lead_get_communicationsenders_v1_response_instance = LeadGetCommunicationsendersV1Response.from_json(json)
# print the JSON string representation of the object
print(LeadGetCommunicationsendersV1Response.to_json())

# convert the object into a dict
lead_get_communicationsenders_v1_response_dict = lead_get_communicationsenders_v1_response_instance.to_dict()
# create an instance of LeadGetCommunicationsendersV1Response from a dict
lead_get_communicationsenders_v1_response_from_dict = LeadGetCommunicationsendersV1Response.from_dict(lead_get_communicationsenders_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


