# EzsigntemplatepackagesignerGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsigntemplatepackagesigner/{pkiEzsigntemplatepackagesignerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatepackagesigner** | [**EzsigntemplatepackagesignerResponseCompound**](EzsigntemplatepackagesignerResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_get_object_v2_response_m_payload import EzsigntemplatepackagesignerGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerGetObjectV2ResponseMPayload from a JSON string
ezsigntemplatepackagesigner_get_object_v2_response_m_payload_instance = EzsigntemplatepackagesignerGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_get_object_v2_response_m_payload_dict = ezsigntemplatepackagesigner_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerGetObjectV2ResponseMPayload from a dict
ezsigntemplatepackagesigner_get_object_v2_response_m_payload_from_dict = EzsigntemplatepackagesignerGetObjectV2ResponseMPayload.from_dict(ezsigntemplatepackagesigner_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


