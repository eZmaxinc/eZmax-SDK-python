# EzsignbulksendGetFormsDataV1Response

Response for GET /1/object/ezsignbulksend/{pkiEzsignbulksendID}/getFormsData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignbulksendGetFormsDataV1ResponseMPayload**](EzsignbulksendGetFormsDataV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_get_forms_data_v1_response import EzsignbulksendGetFormsDataV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendGetFormsDataV1Response from a JSON string
ezsignbulksend_get_forms_data_v1_response_instance = EzsignbulksendGetFormsDataV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendGetFormsDataV1Response.to_json())

# convert the object into a dict
ezsignbulksend_get_forms_data_v1_response_dict = ezsignbulksend_get_forms_data_v1_response_instance.to_dict()
# create an instance of EzsignbulksendGetFormsDataV1Response from a dict
ezsignbulksend_get_forms_data_v1_response_from_dict = EzsignbulksendGetFormsDataV1Response.from_dict(ezsignbulksend_get_forms_data_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


