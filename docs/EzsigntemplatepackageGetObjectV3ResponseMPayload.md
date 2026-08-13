# EzsigntemplatepackageGetObjectV3ResponseMPayload

Payload for GET /3/object/ezsigntemplatepackage/{pkiEzsigntemplatepackageID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatepackage** | [**EzsigntemplatepackageResponseCompoundV3**](EzsigntemplatepackageResponseCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_get_object_v3_response_m_payload import EzsigntemplatepackageGetObjectV3ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageGetObjectV3ResponseMPayload from a JSON string
ezsigntemplatepackage_get_object_v3_response_m_payload_instance = EzsigntemplatepackageGetObjectV3ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackageGetObjectV3ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatepackage_get_object_v3_response_m_payload_dict = ezsigntemplatepackage_get_object_v3_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepackageGetObjectV3ResponseMPayload from a dict
ezsigntemplatepackage_get_object_v3_response_m_payload_from_dict = EzsigntemplatepackageGetObjectV3ResponseMPayload.from_dict(ezsigntemplatepackage_get_object_v3_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


