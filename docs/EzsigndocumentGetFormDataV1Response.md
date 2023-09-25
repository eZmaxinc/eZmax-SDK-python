# EzsigndocumentGetFormDataV1Response

Response for GET /1/object/ezsigndocument/{pkiEzsigndocument}/getFormData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigndocumentGetFormDataV1ResponseMPayload**](EzsigndocumentGetFormDataV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_form_data_v1_response import EzsigndocumentGetFormDataV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetFormDataV1Response from a JSON string
ezsigndocument_get_form_data_v1_response_instance = EzsigndocumentGetFormDataV1Response.from_json(json)
# print the JSON string representation of the object
print EzsigndocumentGetFormDataV1Response.to_json()

# convert the object into a dict
ezsigndocument_get_form_data_v1_response_dict = ezsigndocument_get_form_data_v1_response_instance.to_dict()
# create an instance of EzsigndocumentGetFormDataV1Response from a dict
ezsigndocument_get_form_data_v1_response_form_dict = ezsigndocument_get_form_data_v1_response.from_dict(ezsigndocument_get_form_data_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


