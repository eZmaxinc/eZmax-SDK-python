# CommonGetListV1ResponseMPayload

Generic List Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_row_returned** | **int** | The number of rows returned | 
**i_row_filtered** | **int** | The number of rows matching your filters (if any) or the total number of rows | 

## Example

```python
from eZmaxApi.models.common_get_list_v1_response_m_payload import CommonGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CommonGetListV1ResponseMPayload from a JSON string
common_get_list_v1_response_m_payload_instance = CommonGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CommonGetListV1ResponseMPayload.to_json())

# convert the object into a dict
common_get_list_v1_response_m_payload_dict = common_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of CommonGetListV1ResponseMPayload from a dict
common_get_list_v1_response_m_payload_form_dict = common_get_list_v1_response_m_payload.from_dict(common_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


