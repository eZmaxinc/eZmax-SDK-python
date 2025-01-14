# EzsigntemplateCopyV1Response

Response for POST /1/object/ezsigntemplate/{pkiEzsigntemplateID}/copy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplateCopyV1ResponseMPayload**](EzsigntemplateCopyV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_copy_v1_response import EzsigntemplateCopyV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateCopyV1Response from a JSON string
ezsigntemplate_copy_v1_response_instance = EzsigntemplateCopyV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateCopyV1Response.to_json())

# convert the object into a dict
ezsigntemplate_copy_v1_response_dict = ezsigntemplate_copy_v1_response_instance.to_dict()
# create an instance of EzsigntemplateCopyV1Response from a dict
ezsigntemplate_copy_v1_response_from_dict = EzsigntemplateCopyV1Response.from_dict(ezsigntemplate_copy_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


