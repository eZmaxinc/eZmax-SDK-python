# EzsignsigningreasonGetListV1ResponseMPayload

Payload for GET /1/object/ezsignsigningreason/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_row_returned** | **int** | The number of rows returned | 
**i_row_filtered** | **int** | The number of rows matching your filters (if any) or the total number of rows | 
**a_obj_ezsignsigningreason** | [**List[EzsignsigningreasonListElement]**](EzsignsigningreasonListElement.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsigningreason_get_list_v1_response_m_payload import EzsignsigningreasonGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsigningreasonGetListV1ResponseMPayload from a JSON string
ezsignsigningreason_get_list_v1_response_m_payload_instance = EzsignsigningreasonGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignsigningreasonGetListV1ResponseMPayload.to_json()

# convert the object into a dict
ezsignsigningreason_get_list_v1_response_m_payload_dict = ezsignsigningreason_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignsigningreasonGetListV1ResponseMPayload from a dict
ezsignsigningreason_get_list_v1_response_m_payload_form_dict = ezsignsigningreason_get_list_v1_response_m_payload.from_dict(ezsignsigningreason_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


