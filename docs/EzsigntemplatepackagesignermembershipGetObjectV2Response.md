# EzsigntemplatepackagesignermembershipGetObjectV2Response

Response for GET /2/object/ezsigntemplatepackagesignermembership/{pkiEzsigntemplatepackagesignermembershipID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepackagesignermembershipGetObjectV2ResponseMPayload**](EzsigntemplatepackagesignermembershipGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesignermembership_get_object_v2_response import EzsigntemplatepackagesignermembershipGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignermembershipGetObjectV2Response from a JSON string
ezsigntemplatepackagesignermembership_get_object_v2_response_instance = EzsigntemplatepackagesignermembershipGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignermembershipGetObjectV2Response.to_json())

# convert the object into a dict
ezsigntemplatepackagesignermembership_get_object_v2_response_dict = ezsigntemplatepackagesignermembership_get_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplatepackagesignermembershipGetObjectV2Response from a dict
ezsigntemplatepackagesignermembership_get_object_v2_response_from_dict = EzsigntemplatepackagesignermembershipGetObjectV2Response.from_dict(ezsigntemplatepackagesignermembership_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


