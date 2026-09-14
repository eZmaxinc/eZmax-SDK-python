# CommissionadvanceGetCommunicationrecipientsV1Response

Response for GET /1/object/commissionadvance/{pkiCommissionadvanceID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CommissionadvanceGetCommunicationrecipientsV1ResponseMPayload**](CommissionadvanceGetCommunicationrecipientsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.commissionadvance_get_communicationrecipients_v1_response import CommissionadvanceGetCommunicationrecipientsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionadvanceGetCommunicationrecipientsV1Response from a JSON string
commissionadvance_get_communicationrecipients_v1_response_instance = CommissionadvanceGetCommunicationrecipientsV1Response.from_json(json)
# print the JSON string representation of the object
print(CommissionadvanceGetCommunicationrecipientsV1Response.to_json())

# convert the object into a dict
commissionadvance_get_communicationrecipients_v1_response_dict = commissionadvance_get_communicationrecipients_v1_response_instance.to_dict()
# create an instance of CommissionadvanceGetCommunicationrecipientsV1Response from a dict
commissionadvance_get_communicationrecipients_v1_response_from_dict = CommissionadvanceGetCommunicationrecipientsV1Response.from_dict(commissionadvance_get_communicationrecipients_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


