# EzsigntemplatepackageGetObjectV2Response

Response for GET /2/object/ezsigntemplatepackage/{pkiEzsigntemplatepackageID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepackageGetObjectV2ResponseMPayload**](EzsigntemplatepackageGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_get_object_v2_response import EzsigntemplatepackageGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageGetObjectV2Response from a JSON string
ezsigntemplatepackage_get_object_v2_response_instance = EzsigntemplatepackageGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackageGetObjectV2Response.to_json()

# convert the object into a dict
ezsigntemplatepackage_get_object_v2_response_dict = ezsigntemplatepackage_get_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplatepackageGetObjectV2Response from a dict
ezsigntemplatepackage_get_object_v2_response_form_dict = ezsigntemplatepackage_get_object_v2_response.from_dict(ezsigntemplatepackage_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


