# OfficetaxreportGetCommunicationsendersV1ResponseMPayload

Response for GET /1/object/officetaxreport/{pkiOfficetaxreportID}/getCommunicationsenders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationsenders** | [**List[CustomCommunicationsenderResponse]**](CustomCommunicationsenderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.officetaxreport_get_communicationsenders_v1_response_m_payload import OfficetaxreportGetCommunicationsendersV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of OfficetaxreportGetCommunicationsendersV1ResponseMPayload from a JSON string
officetaxreport_get_communicationsenders_v1_response_m_payload_instance = OfficetaxreportGetCommunicationsendersV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(OfficetaxreportGetCommunicationsendersV1ResponseMPayload.to_json())

# convert the object into a dict
officetaxreport_get_communicationsenders_v1_response_m_payload_dict = officetaxreport_get_communicationsenders_v1_response_m_payload_instance.to_dict()
# create an instance of OfficetaxreportGetCommunicationsendersV1ResponseMPayload from a dict
officetaxreport_get_communicationsenders_v1_response_m_payload_from_dict = OfficetaxreportGetCommunicationsendersV1ResponseMPayload.from_dict(officetaxreport_get_communicationsenders_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


