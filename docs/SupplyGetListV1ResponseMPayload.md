# SupplyGetListV1ResponseMPayload

Payload for GET /1/object/supply/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_row_returned** | **int** | The number of rows returned | 
**i_row_filtered** | **int** | The number of rows matching your filters (if any) or the total number of rows | 
**a_obj_supply** | [**List[SupplyListElement]**](SupplyListElement.md) |  | 

## Example

```python
from eZmaxApi.models.supply_get_list_v1_response_m_payload import SupplyGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyGetListV1ResponseMPayload from a JSON string
supply_get_list_v1_response_m_payload_instance = SupplyGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SupplyGetListV1ResponseMPayload.to_json())

# convert the object into a dict
supply_get_list_v1_response_m_payload_dict = supply_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of SupplyGetListV1ResponseMPayload from a dict
supply_get_list_v1_response_m_payload_from_dict = SupplyGetListV1ResponseMPayload.from_dict(supply_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


