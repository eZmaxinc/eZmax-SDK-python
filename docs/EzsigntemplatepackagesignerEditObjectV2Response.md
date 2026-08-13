# EzsigntemplatepackagesignerEditObjectV2Response

Response for PUT /2/object/ezsigntemplatepackagesigner/{pkiEzsigntemplatepackagesignerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_edit_object_v2_response import EzsigntemplatepackagesignerEditObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerEditObjectV2Response from a JSON string
ezsigntemplatepackagesigner_edit_object_v2_response_instance = EzsigntemplatepackagesignerEditObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerEditObjectV2Response.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_edit_object_v2_response_dict = ezsigntemplatepackagesigner_edit_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerEditObjectV2Response from a dict
ezsigntemplatepackagesigner_edit_object_v2_response_from_dict = EzsigntemplatepackagesignerEditObjectV2Response.from_dict(ezsigntemplatepackagesigner_edit_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


