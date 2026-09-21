# OfficetaxreportGetCommunicationCountV1Response

Response for GET /1/object/officetaxreport/{pkiOfficetaxreportID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**OfficetaxreportGetCommunicationCountV1ResponseMPayload**](OfficetaxreportGetCommunicationCountV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.officetaxreport_get_communication_count_v1_response import OfficetaxreportGetCommunicationCountV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of OfficetaxreportGetCommunicationCountV1Response from a JSON string
officetaxreport_get_communication_count_v1_response_instance = OfficetaxreportGetCommunicationCountV1Response.from_json(json)
# print the JSON string representation of the object
print(OfficetaxreportGetCommunicationCountV1Response.to_json())

# convert the object into a dict
officetaxreport_get_communication_count_v1_response_dict = officetaxreport_get_communication_count_v1_response_instance.to_dict()
# create an instance of OfficetaxreportGetCommunicationCountV1Response from a dict
officetaxreport_get_communication_count_v1_response_from_dict = OfficetaxreportGetCommunicationCountV1Response.from_dict(officetaxreport_get_communication_count_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


