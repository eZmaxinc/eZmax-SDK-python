# EzsigntemplatesignerGetObjectV3ResponseMPayload

Payload for GET /3/object/ezsigntemplatesigner/{pkiEzsigntemplatesignerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatesigner** | [**EzsigntemplatesignerResponseCompoundV3**](EzsigntemplatesignerResponseCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_get_object_v3_response_m_payload import EzsigntemplatesignerGetObjectV3ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerGetObjectV3ResponseMPayload from a JSON string
ezsigntemplatesigner_get_object_v3_response_m_payload_instance = EzsigntemplatesignerGetObjectV3ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignerGetObjectV3ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatesigner_get_object_v3_response_m_payload_dict = ezsigntemplatesigner_get_object_v3_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatesignerGetObjectV3ResponseMPayload from a dict
ezsigntemplatesigner_get_object_v3_response_m_payload_from_dict = EzsigntemplatesignerGetObjectV3ResponseMPayload.from_dict(ezsigntemplatesigner_get_object_v3_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


