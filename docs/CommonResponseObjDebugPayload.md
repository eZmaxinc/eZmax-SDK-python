# CommonResponseObjDebugPayload

This is a debug object containing debugging information on the actual function

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_version_min** | **int** | The minimum version of the function that can be called | 
**i_version_max** | **int** | The maximum version of the function that can be called | 
**a_required_permission** | **List[int]** | An array of permissions required to access this function.  If the value \&quot;0\&quot; is present in the array, anyone can call this function.  You must have one of the permission to access the function. You don&#39;t need to have all of them. | 
**b_version_deprecated** | **bool** | Wheter the current route is deprecated or not | 

## Example

```python
from eZmaxApi.models.common_response_obj_debug_payload import CommonResponseObjDebugPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResponseObjDebugPayload from a JSON string
common_response_obj_debug_payload_instance = CommonResponseObjDebugPayload.from_json(json)
# print the JSON string representation of the object
print CommonResponseObjDebugPayload.to_json()

# convert the object into a dict
common_response_obj_debug_payload_dict = common_response_obj_debug_payload_instance.to_dict()
# create an instance of CommonResponseObjDebugPayload from a dict
common_response_obj_debug_payload_form_dict = common_response_obj_debug_payload.from_dict(common_response_obj_debug_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


