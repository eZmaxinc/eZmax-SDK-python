# EzsignbulksendtransmissionGetFormsDataV1Response

Response for GET /1/object/ezsignbulksendtransmission/{pkiEzsignbulksendtransmissionID}/getFormsData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload**](EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendtransmission_get_forms_data_v1_response import EzsignbulksendtransmissionGetFormsDataV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendtransmissionGetFormsDataV1Response from a JSON string
ezsignbulksendtransmission_get_forms_data_v1_response_instance = EzsignbulksendtransmissionGetFormsDataV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendtransmissionGetFormsDataV1Response.to_json())

# convert the object into a dict
ezsignbulksendtransmission_get_forms_data_v1_response_dict = ezsignbulksendtransmission_get_forms_data_v1_response_instance.to_dict()
# create an instance of EzsignbulksendtransmissionGetFormsDataV1Response from a dict
ezsignbulksendtransmission_get_forms_data_v1_response_form_dict = ezsignbulksendtransmission_get_forms_data_v1_response.from_dict(ezsignbulksendtransmission_get_forms_data_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


