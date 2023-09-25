# CommonResponseObjDebugPayloadGetList

This is a debug object containing debugging information on the actual function

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_version_min** | **int** | The minimum version of the function that can be called | 
**i_version_max** | **int** | The maximum version of the function that can be called | 
**a_required_permission** | **List[int]** | An array of permissions required to access this function.  If the value \&quot;0\&quot; is present in the array, anyone can call this function.  You must have one of the permission to access the function. You don&#39;t need to have all of them. | 
**b_version_deprecated** | **bool** | Wheter the current route is deprecated or not | 
**a_filter** | [**CommonResponseFilter**](CommonResponseFilter.md) |  | 
**a_order_by** | **Dict[str, str]** | List of available values for *eOrderBy* | 
**i_row_max** | **int** | The maximum numbers of results to be returned | [default to 10000]
**i_row_offset** | **int** | The starting element from where to start retrieving the results. For example if you started at iRowOffset&#x3D;0 and asked for iRowMax&#x3D;100, to get the next 100 results, you could specify iRowOffset&#x3D;100&amp;iRowMax&#x3D;100, | [default to 0]

## Example

```python
from eZmaxApi.models.common_response_obj_debug_payload_get_list import CommonResponseObjDebugPayloadGetList

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResponseObjDebugPayloadGetList from a JSON string
common_response_obj_debug_payload_get_list_instance = CommonResponseObjDebugPayloadGetList.from_json(json)
# print the JSON string representation of the object
print CommonResponseObjDebugPayloadGetList.to_json()

# convert the object into a dict
common_response_obj_debug_payload_get_list_dict = common_response_obj_debug_payload_get_list_instance.to_dict()
# create an instance of CommonResponseObjDebugPayloadGetList from a dict
common_response_obj_debug_payload_get_list_form_dict = common_response_obj_debug_payload_get_list.from_dict(common_response_obj_debug_payload_get_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


