# EzsigntemplatedocumentEditObjectV1Response

Response for PUT /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**a_obj_warning** | [**List[CommonResponseWarning]**](CommonResponseWarning.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_edit_object_v1_response import EzsigntemplatedocumentEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentEditObjectV1Response from a JSON string
ezsigntemplatedocument_edit_object_v1_response_instance = EzsigntemplatedocumentEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatedocumentEditObjectV1Response.to_json()

# convert the object into a dict
ezsigntemplatedocument_edit_object_v1_response_dict = ezsigntemplatedocument_edit_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentEditObjectV1Response from a dict
ezsigntemplatedocument_edit_object_v1_response_form_dict = ezsigntemplatedocument_edit_object_v1_response.from_dict(ezsigntemplatedocument_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


