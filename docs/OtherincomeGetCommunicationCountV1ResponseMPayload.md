# OtherincomeGetCommunicationCountV1ResponseMPayload

Response for GET /1/object/otherincome/{pkiOtherincomeID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_communication_count** | **int** | The count of Communication. | 

## Example

```python
from eZmaxApi.models.otherincome_get_communication_count_v1_response_m_payload import OtherincomeGetCommunicationCountV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of OtherincomeGetCommunicationCountV1ResponseMPayload from a JSON string
otherincome_get_communication_count_v1_response_m_payload_instance = OtherincomeGetCommunicationCountV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(OtherincomeGetCommunicationCountV1ResponseMPayload.to_json())

# convert the object into a dict
otherincome_get_communication_count_v1_response_m_payload_dict = otherincome_get_communication_count_v1_response_m_payload_instance.to_dict()
# create an instance of OtherincomeGetCommunicationCountV1ResponseMPayload from a dict
otherincome_get_communication_count_v1_response_m_payload_from_dict = OtherincomeGetCommunicationCountV1ResponseMPayload.from_dict(otherincome_get_communication_count_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


