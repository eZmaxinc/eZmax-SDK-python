# SupplyCreateObjectV1Response

Response for POST /1/object/supply

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**SupplyCreateObjectV1ResponseMPayload**](SupplyCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.supply_create_object_v1_response import SupplyCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyCreateObjectV1Response from a JSON string
supply_create_object_v1_response_instance = SupplyCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(SupplyCreateObjectV1Response.to_json())

# convert the object into a dict
supply_create_object_v1_response_dict = supply_create_object_v1_response_instance.to_dict()
# create an instance of SupplyCreateObjectV1Response from a dict
supply_create_object_v1_response_from_dict = SupplyCreateObjectV1Response.from_dict(supply_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


