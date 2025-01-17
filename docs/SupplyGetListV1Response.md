# SupplyGetListV1Response

Response for GET /1/object/supply/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**SupplyGetListV1ResponseMPayload**](SupplyGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.supply_get_list_v1_response import SupplyGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyGetListV1Response from a JSON string
supply_get_list_v1_response_instance = SupplyGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(SupplyGetListV1Response.to_json())

# convert the object into a dict
supply_get_list_v1_response_dict = supply_get_list_v1_response_instance.to_dict()
# create an instance of SupplyGetListV1Response from a dict
supply_get_list_v1_response_from_dict = SupplyGetListV1Response.from_dict(supply_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


