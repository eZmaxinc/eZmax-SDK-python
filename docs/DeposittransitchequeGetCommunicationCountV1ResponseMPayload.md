# DeposittransitchequeGetCommunicationCountV1ResponseMPayload

Response for GET /1/object/deposittransitcheque/{pkiDeposittransitchequeID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_communication_count** | **int** | The count of Communication. | 

## Example

```python
from eZmaxApi.models.deposittransitcheque_get_communication_count_v1_response_m_payload import DeposittransitchequeGetCommunicationCountV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DeposittransitchequeGetCommunicationCountV1ResponseMPayload from a JSON string
deposittransitcheque_get_communication_count_v1_response_m_payload_instance = DeposittransitchequeGetCommunicationCountV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DeposittransitchequeGetCommunicationCountV1ResponseMPayload.to_json())

# convert the object into a dict
deposittransitcheque_get_communication_count_v1_response_m_payload_dict = deposittransitcheque_get_communication_count_v1_response_m_payload_instance.to_dict()
# create an instance of DeposittransitchequeGetCommunicationCountV1ResponseMPayload from a dict
deposittransitcheque_get_communication_count_v1_response_m_payload_from_dict = DeposittransitchequeGetCommunicationCountV1ResponseMPayload.from_dict(deposittransitcheque_get_communication_count_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


