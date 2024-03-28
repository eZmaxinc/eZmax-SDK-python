# EzsigndocumentGetCompletedElementsV1Response

Response for GET /1/object/ezsigndocument/{pkiEzsigndocumentID}/getCompletedElements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigndocumentGetCompletedElementsV1ResponseMPayload**](EzsigndocumentGetCompletedElementsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_completed_elements_v1_response import EzsigndocumentGetCompletedElementsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetCompletedElementsV1Response from a JSON string
ezsigndocument_get_completed_elements_v1_response_instance = EzsigndocumentGetCompletedElementsV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetCompletedElementsV1Response.to_json())

# convert the object into a dict
ezsigndocument_get_completed_elements_v1_response_dict = ezsigndocument_get_completed_elements_v1_response_instance.to_dict()
# create an instance of EzsigndocumentGetCompletedElementsV1Response from a dict
ezsigndocument_get_completed_elements_v1_response_form_dict = ezsigndocument_get_completed_elements_v1_response.from_dict(ezsigndocument_get_completed_elements_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


