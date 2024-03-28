# EzsigntemplatesignerEditObjectV1Response

Response for PUT /1/object/ezsigntemplatesigner/{pkiEzsigntemplatesignerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_edit_object_v1_response import EzsigntemplatesignerEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerEditObjectV1Response from a JSON string
ezsigntemplatesigner_edit_object_v1_response_instance = EzsigntemplatesignerEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignerEditObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplatesigner_edit_object_v1_response_dict = ezsigntemplatesigner_edit_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatesignerEditObjectV1Response from a dict
ezsigntemplatesigner_edit_object_v1_response_form_dict = ezsigntemplatesigner_edit_object_v1_response.from_dict(ezsigntemplatesigner_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


