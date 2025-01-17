# SupplyGetObjectV2Response

Response for GET /2/object/supply/{pkiSupplyID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**SupplyGetObjectV2ResponseMPayload**](SupplyGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.supply_get_object_v2_response import SupplyGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyGetObjectV2Response from a JSON string
supply_get_object_v2_response_instance = SupplyGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(SupplyGetObjectV2Response.to_json())

# convert the object into a dict
supply_get_object_v2_response_dict = supply_get_object_v2_response_instance.to_dict()
# create an instance of SupplyGetObjectV2Response from a dict
supply_get_object_v2_response_from_dict = SupplyGetObjectV2Response.from_dict(supply_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


