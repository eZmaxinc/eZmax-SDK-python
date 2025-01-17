# TranqcontractGetCommunicationsendersV1Response

Response for GET /1/object/tranqcontract/{pkiTranqcontractID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**TranqcontractGetCommunicationsendersV1ResponseMPayload**](TranqcontractGetCommunicationsendersV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.tranqcontract_get_communicationsenders_v1_response import TranqcontractGetCommunicationsendersV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of TranqcontractGetCommunicationsendersV1Response from a JSON string
tranqcontract_get_communicationsenders_v1_response_instance = TranqcontractGetCommunicationsendersV1Response.from_json(json)
# print the JSON string representation of the object
print(TranqcontractGetCommunicationsendersV1Response.to_json())

# convert the object into a dict
tranqcontract_get_communicationsenders_v1_response_dict = tranqcontract_get_communicationsenders_v1_response_instance.to_dict()
# create an instance of TranqcontractGetCommunicationsendersV1Response from a dict
tranqcontract_get_communicationsenders_v1_response_from_dict = TranqcontractGetCommunicationsendersV1Response.from_dict(tranqcontract_get_communicationsenders_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


