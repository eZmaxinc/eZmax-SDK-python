# DisclosureGetListV1ResponseMPayload

Payload for GET /1/object/disclosure/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_row_returned** | **int** | The number of rows returned | 
**i_row_filtered** | **int** | The number of rows matching your filters (if any) or the total number of rows | 
**a_obj_disclosure** | [**List[DisclosureListElement]**](DisclosureListElement.md) |  | 

## Example

```python
from eZmaxApi.models.disclosure_get_list_v1_response_m_payload import DisclosureGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureGetListV1ResponseMPayload from a JSON string
disclosure_get_list_v1_response_m_payload_instance = DisclosureGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DisclosureGetListV1ResponseMPayload.to_json())

# convert the object into a dict
disclosure_get_list_v1_response_m_payload_dict = disclosure_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of DisclosureGetListV1ResponseMPayload from a dict
disclosure_get_list_v1_response_m_payload_from_dict = DisclosureGetListV1ResponseMPayload.from_dict(disclosure_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


