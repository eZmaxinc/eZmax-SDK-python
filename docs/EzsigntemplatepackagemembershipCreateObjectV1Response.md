# EzsigntemplatepackagemembershipCreateObjectV1Response

Response for POST /1/object/ezsigntemplatepackagemembership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload**](EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagemembership_create_object_v1_response import EzsigntemplatepackagemembershipCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagemembershipCreateObjectV1Response from a JSON string
ezsigntemplatepackagemembership_create_object_v1_response_instance = EzsigntemplatepackagemembershipCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagemembershipCreateObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplatepackagemembership_create_object_v1_response_dict = ezsigntemplatepackagemembership_create_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepackagemembershipCreateObjectV1Response from a dict
ezsigntemplatepackagemembership_create_object_v1_response_form_dict = ezsigntemplatepackagemembership_create_object_v1_response.from_dict(ezsigntemplatepackagemembership_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


