# EzsigntemplatesignatureGetObjectV4ResponseMPayload

Payload for GET /4/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatesignature** | [**EzsigntemplatesignatureResponseCompoundV4**](EzsigntemplatesignatureResponseCompoundV4.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_get_object_v4_response_m_payload import EzsigntemplatesignatureGetObjectV4ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureGetObjectV4ResponseMPayload from a JSON string
ezsigntemplatesignature_get_object_v4_response_m_payload_instance = EzsigntemplatesignatureGetObjectV4ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureGetObjectV4ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatesignature_get_object_v4_response_m_payload_dict = ezsigntemplatesignature_get_object_v4_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatesignatureGetObjectV4ResponseMPayload from a dict
ezsigntemplatesignature_get_object_v4_response_m_payload_from_dict = EzsigntemplatesignatureGetObjectV4ResponseMPayload.from_dict(ezsigntemplatesignature_get_object_v4_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


