# SupplyEditObjectV1Response

Response for PUT /1/object/supply/{pkiSupplyID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from eZmaxApi.models.supply_edit_object_v1_response import SupplyEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyEditObjectV1Response from a JSON string
supply_edit_object_v1_response_instance = SupplyEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(SupplyEditObjectV1Response.to_json())

# convert the object into a dict
supply_edit_object_v1_response_dict = supply_edit_object_v1_response_instance.to_dict()
# create an instance of SupplyEditObjectV1Response from a dict
supply_edit_object_v1_response_from_dict = SupplyEditObjectV1Response.from_dict(supply_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


