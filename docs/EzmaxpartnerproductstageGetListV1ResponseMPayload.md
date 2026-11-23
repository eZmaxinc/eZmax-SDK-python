# EzmaxpartnerproductstageGetListV1ResponseMPayload

Payload for GET /1/object/ezmaxpartnerproductstage/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_row_returned** | **int** | The number of rows returned | 
**i_row_filtered** | **int** | The number of rows matching your filters (if any) or the total number of rows | 
**a_obj_ezmaxpartnerproductstage** | [**List[EzmaxpartnerproductstageListElement]**](EzmaxpartnerproductstageListElement.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxpartnerproductstage_get_list_v1_response_m_payload import EzmaxpartnerproductstageGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerproductstageGetListV1ResponseMPayload from a JSON string
ezmaxpartnerproductstage_get_list_v1_response_m_payload_instance = EzmaxpartnerproductstageGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerproductstageGetListV1ResponseMPayload.to_json())

# convert the object into a dict
ezmaxpartnerproductstage_get_list_v1_response_m_payload_dict = ezmaxpartnerproductstage_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of EzmaxpartnerproductstageGetListV1ResponseMPayload from a dict
ezmaxpartnerproductstage_get_list_v1_response_m_payload_from_dict = EzmaxpartnerproductstageGetListV1ResponseMPayload.from_dict(ezmaxpartnerproductstage_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


