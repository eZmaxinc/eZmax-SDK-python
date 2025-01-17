# ElectronicfundstransferGetCommunicationCountV1Response

Response for GET /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**ElectronicfundstransferGetCommunicationCountV1ResponseMPayload**](ElectronicfundstransferGetCommunicationCountV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.electronicfundstransfer_get_communication_count_v1_response import ElectronicfundstransferGetCommunicationCountV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicfundstransferGetCommunicationCountV1Response from a JSON string
electronicfundstransfer_get_communication_count_v1_response_instance = ElectronicfundstransferGetCommunicationCountV1Response.from_json(json)
# print the JSON string representation of the object
print(ElectronicfundstransferGetCommunicationCountV1Response.to_json())

# convert the object into a dict
electronicfundstransfer_get_communication_count_v1_response_dict = electronicfundstransfer_get_communication_count_v1_response_instance.to_dict()
# create an instance of ElectronicfundstransferGetCommunicationCountV1Response from a dict
electronicfundstransfer_get_communication_count_v1_response_from_dict = ElectronicfundstransferGetCommunicationCountV1Response.from_dict(electronicfundstransfer_get_communication_count_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


