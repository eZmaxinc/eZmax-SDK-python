# EzsigntemplatesignerCreateObjectV1Response

Response for POST /1/object/ezsigntemplatesigner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatesignerCreateObjectV1ResponseMPayload**](EzsigntemplatesignerCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_create_object_v1_response import EzsigntemplatesignerCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerCreateObjectV1Response from a JSON string
ezsigntemplatesigner_create_object_v1_response_instance = EzsigntemplatesignerCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatesignerCreateObjectV1Response.to_json()

# convert the object into a dict
ezsigntemplatesigner_create_object_v1_response_dict = ezsigntemplatesigner_create_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatesignerCreateObjectV1Response from a dict
ezsigntemplatesigner_create_object_v1_response_form_dict = ezsigntemplatesigner_create_object_v1_response.from_dict(ezsigntemplatesigner_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


