# EzsigndiscussionDeleteObjectV1Response

Response for DELETE /1/object/ezsigndiscussion/{pkiEzsigndiscussionID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigndiscussion_delete_object_v1_response import EzsigndiscussionDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndiscussionDeleteObjectV1Response from a JSON string
ezsigndiscussion_delete_object_v1_response_instance = EzsigndiscussionDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print EzsigndiscussionDeleteObjectV1Response.to_json()

# convert the object into a dict
ezsigndiscussion_delete_object_v1_response_dict = ezsigndiscussion_delete_object_v1_response_instance.to_dict()
# create an instance of EzsigndiscussionDeleteObjectV1Response from a dict
ezsigndiscussion_delete_object_v1_response_form_dict = ezsigndiscussion_delete_object_v1_response.from_dict(ezsigndiscussion_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


