# TranqcontractGetCommunicationCountV1ResponseMPayload

Response for GET /1/object/tranqcontract/{pkiTranqcontractID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_communication_count** | **int** | The count of Communication. | 

## Example

```python
from eZmaxApi.models.tranqcontract_get_communication_count_v1_response_m_payload import TranqcontractGetCommunicationCountV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TranqcontractGetCommunicationCountV1ResponseMPayload from a JSON string
tranqcontract_get_communication_count_v1_response_m_payload_instance = TranqcontractGetCommunicationCountV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(TranqcontractGetCommunicationCountV1ResponseMPayload.to_json())

# convert the object into a dict
tranqcontract_get_communication_count_v1_response_m_payload_dict = tranqcontract_get_communication_count_v1_response_m_payload_instance.to_dict()
# create an instance of TranqcontractGetCommunicationCountV1ResponseMPayload from a dict
tranqcontract_get_communication_count_v1_response_m_payload_from_dict = TranqcontractGetCommunicationCountV1ResponseMPayload.from_dict(tranqcontract_get_communication_count_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


