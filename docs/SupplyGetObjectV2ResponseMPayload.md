# SupplyGetObjectV2ResponseMPayload

Payload for GET /2/object/supply/{pkiSupplyID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_supply** | [**SupplyResponseCompound**](SupplyResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.supply_get_object_v2_response_m_payload import SupplyGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyGetObjectV2ResponseMPayload from a JSON string
supply_get_object_v2_response_m_payload_instance = SupplyGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SupplyGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
supply_get_object_v2_response_m_payload_dict = supply_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of SupplyGetObjectV2ResponseMPayload from a dict
supply_get_object_v2_response_m_payload_from_dict = SupplyGetObjectV2ResponseMPayload.from_dict(supply_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


