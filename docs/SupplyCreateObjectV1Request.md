# SupplyCreateObjectV1Request

Request for POST /1/object/supply

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_supply** | [**List[SupplyRequestCompound]**](SupplyRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.supply_create_object_v1_request import SupplyCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyCreateObjectV1Request from a JSON string
supply_create_object_v1_request_instance = SupplyCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(SupplyCreateObjectV1Request.to_json())

# convert the object into a dict
supply_create_object_v1_request_dict = supply_create_object_v1_request_instance.to_dict()
# create an instance of SupplyCreateObjectV1Request from a dict
supply_create_object_v1_request_from_dict = SupplyCreateObjectV1Request.from_dict(supply_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


