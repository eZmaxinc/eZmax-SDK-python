# EzsigntemplatepackageGetObjectV3Response

Response for GET /3/object/ezsigntemplatepackage/{pkiEzsigntemplatepackageID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepackageGetObjectV3ResponseMPayload**](EzsigntemplatepackageGetObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_get_object_v3_response import EzsigntemplatepackageGetObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageGetObjectV3Response from a JSON string
ezsigntemplatepackage_get_object_v3_response_instance = EzsigntemplatepackageGetObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackageGetObjectV3Response.to_json())

# convert the object into a dict
ezsigntemplatepackage_get_object_v3_response_dict = ezsigntemplatepackage_get_object_v3_response_instance.to_dict()
# create an instance of EzsigntemplatepackageGetObjectV3Response from a dict
ezsigntemplatepackage_get_object_v3_response_from_dict = EzsigntemplatepackageGetObjectV3Response.from_dict(ezsigntemplatepackage_get_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


