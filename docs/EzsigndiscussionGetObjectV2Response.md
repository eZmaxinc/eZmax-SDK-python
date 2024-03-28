# EzsigndiscussionGetObjectV2Response

Response for GET /2/object/ezsigndiscussion/{pkiEzsigndiscussionID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigndiscussionGetObjectV2ResponseMPayload**](EzsigndiscussionGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndiscussion_get_object_v2_response import EzsigndiscussionGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndiscussionGetObjectV2Response from a JSON string
ezsigndiscussion_get_object_v2_response_instance = EzsigndiscussionGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndiscussionGetObjectV2Response.to_json())

# convert the object into a dict
ezsigndiscussion_get_object_v2_response_dict = ezsigndiscussion_get_object_v2_response_instance.to_dict()
# create an instance of EzsigndiscussionGetObjectV2Response from a dict
ezsigndiscussion_get_object_v2_response_form_dict = ezsigndiscussion_get_object_v2_response.from_dict(ezsigndiscussion_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


