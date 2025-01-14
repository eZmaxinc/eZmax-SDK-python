# SupplyEditObjectV1Request

Request for PUT /1/object/supply/{pkiSupplyID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_supply** | [**SupplyRequestCompound**](SupplyRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.supply_edit_object_v1_request import SupplyEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyEditObjectV1Request from a JSON string
supply_edit_object_v1_request_instance = SupplyEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(SupplyEditObjectV1Request.to_json())

# convert the object into a dict
supply_edit_object_v1_request_dict = supply_edit_object_v1_request_instance.to_dict()
# create an instance of SupplyEditObjectV1Request from a dict
supply_edit_object_v1_request_from_dict = SupplyEditObjectV1Request.from_dict(supply_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


