# EzsignpageConsultV1Response

Response for POST /1/object/ezsignpage/{pkiEzsignpageID}/consult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignpage_consult_v1_response import EzsignpageConsultV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignpageConsultV1Response from a JSON string
ezsignpage_consult_v1_response_instance = EzsignpageConsultV1Response.from_json(json)
# print the JSON string representation of the object
print EzsignpageConsultV1Response.to_json()

# convert the object into a dict
ezsignpage_consult_v1_response_dict = ezsignpage_consult_v1_response_instance.to_dict()
# create an instance of EzsignpageConsultV1Response from a dict
ezsignpage_consult_v1_response_form_dict = ezsignpage_consult_v1_response.from_dict(ezsignpage_consult_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


