# EzsigntemplatepackagesignerEditObjectV1Response

Response for PUT /1/object/ezsigntemplatepackagesigner/{pkiEzsigntemplatepackagesignerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_edit_object_v1_response import EzsigntemplatepackagesignerEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerEditObjectV1Response from a JSON string
ezsigntemplatepackagesigner_edit_object_v1_response_instance = EzsigntemplatepackagesignerEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerEditObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_edit_object_v1_response_dict = ezsigntemplatepackagesigner_edit_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerEditObjectV1Response from a dict
ezsigntemplatepackagesigner_edit_object_v1_response_form_dict = ezsigntemplatepackagesigner_edit_object_v1_response.from_dict(ezsigntemplatepackagesigner_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


