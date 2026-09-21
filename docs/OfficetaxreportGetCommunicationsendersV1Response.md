# OfficetaxreportGetCommunicationsendersV1Response

Response for GET /1/object/officetaxreport/{pkiOfficetaxreportID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**OfficetaxreportGetCommunicationsendersV1ResponseMPayload**](OfficetaxreportGetCommunicationsendersV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.officetaxreport_get_communicationsenders_v1_response import OfficetaxreportGetCommunicationsendersV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of OfficetaxreportGetCommunicationsendersV1Response from a JSON string
officetaxreport_get_communicationsenders_v1_response_instance = OfficetaxreportGetCommunicationsendersV1Response.from_json(json)
# print the JSON string representation of the object
print(OfficetaxreportGetCommunicationsendersV1Response.to_json())

# convert the object into a dict
officetaxreport_get_communicationsenders_v1_response_dict = officetaxreport_get_communicationsenders_v1_response_instance.to_dict()
# create an instance of OfficetaxreportGetCommunicationsendersV1Response from a dict
officetaxreport_get_communicationsenders_v1_response_from_dict = OfficetaxreportGetCommunicationsendersV1Response.from_dict(officetaxreport_get_communicationsenders_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


