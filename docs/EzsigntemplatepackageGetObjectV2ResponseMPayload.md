# EzsigntemplatepackageGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsigntemplatepackage/{pkiEzsigntemplatepackageID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatepackage** | [**EzsigntemplatepackageResponseCompound**](EzsigntemplatepackageResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_get_object_v2_response_m_payload import EzsigntemplatepackageGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageGetObjectV2ResponseMPayload from a JSON string
ezsigntemplatepackage_get_object_v2_response_m_payload_instance = EzsigntemplatepackageGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackageGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
ezsigntemplatepackage_get_object_v2_response_m_payload_dict = ezsigntemplatepackage_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepackageGetObjectV2ResponseMPayload from a dict
ezsigntemplatepackage_get_object_v2_response_m_payload_form_dict = ezsigntemplatepackage_get_object_v2_response_m_payload.from_dict(ezsigntemplatepackage_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


