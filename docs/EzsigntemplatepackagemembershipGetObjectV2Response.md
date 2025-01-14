# EzsigntemplatepackagemembershipGetObjectV2Response

Response for GET /2/object/ezsigntemplatepackagemembership/{pkiEzsigntemplatepackagemembershipID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload**](EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagemembership_get_object_v2_response import EzsigntemplatepackagemembershipGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagemembershipGetObjectV2Response from a JSON string
ezsigntemplatepackagemembership_get_object_v2_response_instance = EzsigntemplatepackagemembershipGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagemembershipGetObjectV2Response.to_json())

# convert the object into a dict
ezsigntemplatepackagemembership_get_object_v2_response_dict = ezsigntemplatepackagemembership_get_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplatepackagemembershipGetObjectV2Response from a dict
ezsigntemplatepackagemembership_get_object_v2_response_from_dict = EzsigntemplatepackagemembershipGetObjectV2Response.from_dict(ezsigntemplatepackagemembership_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


