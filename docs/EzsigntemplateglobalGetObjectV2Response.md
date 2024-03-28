# EzsigntemplateglobalGetObjectV2Response

Response for GET /2/object/ezsigntemplateglobal/{pkiEzsigntemplateglobalID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplateglobalGetObjectV2ResponseMPayload**](EzsigntemplateglobalGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateglobal_get_object_v2_response import EzsigntemplateglobalGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateglobalGetObjectV2Response from a JSON string
ezsigntemplateglobal_get_object_v2_response_instance = EzsigntemplateglobalGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateglobalGetObjectV2Response.to_json())

# convert the object into a dict
ezsigntemplateglobal_get_object_v2_response_dict = ezsigntemplateglobal_get_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplateglobalGetObjectV2Response from a dict
ezsigntemplateglobal_get_object_v2_response_form_dict = ezsigntemplateglobal_get_object_v2_response.from_dict(ezsigntemplateglobal_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


