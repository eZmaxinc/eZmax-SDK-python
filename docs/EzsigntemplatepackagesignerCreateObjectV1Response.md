# EzsigntemplatepackagesignerCreateObjectV1Response

Response for POST /1/object/ezsigntemplatepackagesigner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepackagesignerCreateObjectV1ResponseMPayload**](EzsigntemplatepackagesignerCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_create_object_v1_response import EzsigntemplatepackagesignerCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerCreateObjectV1Response from a JSON string
ezsigntemplatepackagesigner_create_object_v1_response_instance = EzsigntemplatepackagesignerCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackagesignerCreateObjectV1Response.to_json()

# convert the object into a dict
ezsigntemplatepackagesigner_create_object_v1_response_dict = ezsigntemplatepackagesigner_create_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerCreateObjectV1Response from a dict
ezsigntemplatepackagesigner_create_object_v1_response_form_dict = ezsigntemplatepackagesigner_create_object_v1_response.from_dict(ezsigntemplatepackagesigner_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


