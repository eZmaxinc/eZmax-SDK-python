# ElectronicfundstransferGetListV1ResponseMPayload

Payload for GET /1/object/electronicfundstransfer/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_row_returned** | **int** | The number of rows returned | 
**i_row_filtered** | **int** | The number of rows matching your filters (if any) or the total number of rows | 
**a_obj_electronicfundstransfer** | [**List[ElectronicfundstransferListElement]**](ElectronicfundstransferListElement.md) |  | 

## Example

```python
from eZmaxApi.models.electronicfundstransfer_get_list_v1_response_m_payload import ElectronicfundstransferGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicfundstransferGetListV1ResponseMPayload from a JSON string
electronicfundstransfer_get_list_v1_response_m_payload_instance = ElectronicfundstransferGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ElectronicfundstransferGetListV1ResponseMPayload.to_json())

# convert the object into a dict
electronicfundstransfer_get_list_v1_response_m_payload_dict = electronicfundstransfer_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of ElectronicfundstransferGetListV1ResponseMPayload from a dict
electronicfundstransfer_get_list_v1_response_m_payload_from_dict = ElectronicfundstransferGetListV1ResponseMPayload.from_dict(electronicfundstransfer_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


