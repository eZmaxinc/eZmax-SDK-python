# EzsigntemplatepackagemembershipGetObjectV3Response

Response for GET /3/object/ezsigntemplatepackagemembership/{pkiEzsigntemplatepackagemembershipID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepackagemembershipGetObjectV3ResponseMPayload**](EzsigntemplatepackagemembershipGetObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagemembership_get_object_v3_response import EzsigntemplatepackagemembershipGetObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagemembershipGetObjectV3Response from a JSON string
ezsigntemplatepackagemembership_get_object_v3_response_instance = EzsigntemplatepackagemembershipGetObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagemembershipGetObjectV3Response.to_json())

# convert the object into a dict
ezsigntemplatepackagemembership_get_object_v3_response_dict = ezsigntemplatepackagemembership_get_object_v3_response_instance.to_dict()
# create an instance of EzsigntemplatepackagemembershipGetObjectV3Response from a dict
ezsigntemplatepackagemembership_get_object_v3_response_from_dict = EzsigntemplatepackagemembershipGetObjectV3Response.from_dict(ezsigntemplatepackagemembership_get_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


