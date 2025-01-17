# SessionhistoryGetListV1ResponseMPayload

Payload for GET /1/object/sessionhistory/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_row_returned** | **int** | The number of rows returned | 
**i_row_filtered** | **int** | The number of rows matching your filters (if any) or the total number of rows | 
**a_obj_sessionhistory** | [**List[SessionhistoryListElement]**](SessionhistoryListElement.md) |  | 

## Example

```python
from eZmaxApi.models.sessionhistory_get_list_v1_response_m_payload import SessionhistoryGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SessionhistoryGetListV1ResponseMPayload from a JSON string
sessionhistory_get_list_v1_response_m_payload_instance = SessionhistoryGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SessionhistoryGetListV1ResponseMPayload.to_json())

# convert the object into a dict
sessionhistory_get_list_v1_response_m_payload_dict = sessionhistory_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of SessionhistoryGetListV1ResponseMPayload from a dict
sessionhistory_get_list_v1_response_m_payload_from_dict = SessionhistoryGetListV1ResponseMPayload.from_dict(sessionhistory_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


