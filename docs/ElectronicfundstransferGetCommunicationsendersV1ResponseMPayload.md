# ElectronicfundstransferGetCommunicationsendersV1ResponseMPayload

Response for GET /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getCommunicationsenders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationsenders** | [**List[CustomCommunicationsenderResponse]**](CustomCommunicationsenderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.electronicfundstransfer_get_communicationsenders_v1_response_m_payload import ElectronicfundstransferGetCommunicationsendersV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicfundstransferGetCommunicationsendersV1ResponseMPayload from a JSON string
electronicfundstransfer_get_communicationsenders_v1_response_m_payload_instance = ElectronicfundstransferGetCommunicationsendersV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ElectronicfundstransferGetCommunicationsendersV1ResponseMPayload.to_json())

# convert the object into a dict
electronicfundstransfer_get_communicationsenders_v1_response_m_payload_dict = electronicfundstransfer_get_communicationsenders_v1_response_m_payload_instance.to_dict()
# create an instance of ElectronicfundstransferGetCommunicationsendersV1ResponseMPayload from a dict
electronicfundstransfer_get_communicationsenders_v1_response_m_payload_from_dict = ElectronicfundstransferGetCommunicationsendersV1ResponseMPayload.from_dict(electronicfundstransfer_get_communicationsenders_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


