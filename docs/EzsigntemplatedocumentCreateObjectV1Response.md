# EzsigntemplatedocumentCreateObjectV1Response

Response for POST /1/object/ezsigntemplatedocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatedocumentCreateObjectV1ResponseMPayload**](EzsigntemplatedocumentCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_create_object_v1_response import EzsigntemplatedocumentCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentCreateObjectV1Response from a JSON string
ezsigntemplatedocument_create_object_v1_response_instance = EzsigntemplatedocumentCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentCreateObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplatedocument_create_object_v1_response_dict = ezsigntemplatedocument_create_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentCreateObjectV1Response from a dict
ezsigntemplatedocument_create_object_v1_response_form_dict = ezsigntemplatedocument_create_object_v1_response.from_dict(ezsigntemplatedocument_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


