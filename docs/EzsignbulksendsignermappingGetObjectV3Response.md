# EzsignbulksendsignermappingGetObjectV3Response

Response for GET /3/object/ezsignbulksendsignermapping/{pkiEzsignbulksendsignermappingID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignbulksendsignermappingGetObjectV3ResponseMPayload**](EzsignbulksendsignermappingGetObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendsignermapping_get_object_v3_response import EzsignbulksendsignermappingGetObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendsignermappingGetObjectV3Response from a JSON string
ezsignbulksendsignermapping_get_object_v3_response_instance = EzsignbulksendsignermappingGetObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendsignermappingGetObjectV3Response.to_json())

# convert the object into a dict
ezsignbulksendsignermapping_get_object_v3_response_dict = ezsignbulksendsignermapping_get_object_v3_response_instance.to_dict()
# create an instance of EzsignbulksendsignermappingGetObjectV3Response from a dict
ezsignbulksendsignermapping_get_object_v3_response_from_dict = EzsignbulksendsignermappingGetObjectV3Response.from_dict(ezsignbulksendsignermapping_get_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


