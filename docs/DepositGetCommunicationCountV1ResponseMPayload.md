# DepositGetCommunicationCountV1ResponseMPayload

Response for GET /1/object/deposit/{pkiDepositID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_communication_count** | **int** | The count of Communication. | 

## Example

```python
from eZmaxApi.models.deposit_get_communication_count_v1_response_m_payload import DepositGetCommunicationCountV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DepositGetCommunicationCountV1ResponseMPayload from a JSON string
deposit_get_communication_count_v1_response_m_payload_instance = DepositGetCommunicationCountV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DepositGetCommunicationCountV1ResponseMPayload.to_json())

# convert the object into a dict
deposit_get_communication_count_v1_response_m_payload_dict = deposit_get_communication_count_v1_response_m_payload_instance.to_dict()
# create an instance of DepositGetCommunicationCountV1ResponseMPayload from a dict
deposit_get_communication_count_v1_response_m_payload_from_dict = DepositGetCommunicationCountV1ResponseMPayload.from_dict(deposit_get_communication_count_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


