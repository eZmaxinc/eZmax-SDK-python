# OtherincomeGetCommunicationCountV1Response

Response for GET /1/object/otherincome/{pkiOtherincomeID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**OtherincomeGetCommunicationCountV1ResponseMPayload**](OtherincomeGetCommunicationCountV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.otherincome_get_communication_count_v1_response import OtherincomeGetCommunicationCountV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of OtherincomeGetCommunicationCountV1Response from a JSON string
otherincome_get_communication_count_v1_response_instance = OtherincomeGetCommunicationCountV1Response.from_json(json)
# print the JSON string representation of the object
print(OtherincomeGetCommunicationCountV1Response.to_json())

# convert the object into a dict
otherincome_get_communication_count_v1_response_dict = otherincome_get_communication_count_v1_response_instance.to_dict()
# create an instance of OtherincomeGetCommunicationCountV1Response from a dict
otherincome_get_communication_count_v1_response_from_dict = OtherincomeGetCommunicationCountV1Response.from_dict(otherincome_get_communication_count_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


