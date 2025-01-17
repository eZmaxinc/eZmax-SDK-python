# EzsigntemplatepackagesignerGetObjectV2Response

Response for GET /2/object/ezsigntemplatepackagesigner/{pkiEzsigntemplatepackagesignerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsigntemplatepackagesignerGetObjectV2ResponseMPayload**](EzsigntemplatepackagesignerGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_get_object_v2_response import EzsigntemplatepackagesignerGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerGetObjectV2Response from a JSON string
ezsigntemplatepackagesigner_get_object_v2_response_instance = EzsigntemplatepackagesignerGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerGetObjectV2Response.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_get_object_v2_response_dict = ezsigntemplatepackagesigner_get_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerGetObjectV2Response from a dict
ezsigntemplatepackagesigner_get_object_v2_response_from_dict = EzsigntemplatepackagesignerGetObjectV2Response.from_dict(ezsigntemplatepackagesigner_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


